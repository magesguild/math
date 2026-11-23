#!/usr/bin/env python3
"""
PRISM Cloud API Client — Lightweight REST interface for Project PRISM.
Mage's Guild Psychonautics LLC (https://www.magesguild.io)

Zero external dependencies (uses standard library urllib and json).
"""

import json
import os
import urllib.request
import urllib.error
import time

DEFAULT_API_URL = os.environ.get(
    "PRISM_API_URL", "https://www.magesguild.io/api/prism/eval"
)
CHEMISTRY_API_URL = os.environ.get(
    "PRISM_CHEM_API_URL", "https://www.magesguild.io/api/prism/chemistry/eval"
)


def prism_eval(expr: str, session_id: str = "validation") -> dict:
    """
    Evaluates a mathematical, matrix, qudit, or fluid expression on the
    unauthenticated Project PRISM REST API.
    
    Returns:
        dict: {"status": "ok", "result": str, "error": None, "latency_us": float}
    """
    payload = json.dumps({"expr": expr, "session_id": session_id}).encode("utf-8")
    req = urllib.request.Request(
        DEFAULT_API_URL,
        data=payload,
        headers={"Content-Type": "application/json", "User-Agent": "prism-validator/1.0"},
    )
    t0 = time.perf_counter()
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            if "latency_us" not in data:
                data["latency_us"] = (time.perf_counter() - t0) * 1e6
            return data
    except urllib.error.HTTPError as e:
        err_msg = e.read().decode("utf-8", errors="ignore")
        return {"status": "error", "result": None, "error": f"HTTP {e.code}: {err_msg}", "latency_us": 0.0}
    except Exception as e:
        return {"status": "error", "result": None, "error": str(e), "latency_us": 0.0}


def prism_eval_float(expr: str, session_id: str = "validation") -> float:
    """Evaluates an expression and returns the result parsed as float."""
    res = prism_eval(expr, session_id)
    if res.get("status") != "ok" or res.get("result") is None:
        raise RuntimeError(f"PRISM eval failed for '{expr}': {res.get('error')}")
    try:
        return float(res["result"])
    except ValueError:
        raise ValueError(f"Could not parse PRISM result '{res['result']}' as float")


def prism_chemistry_eval(num_qubits: int, terms: list) -> dict:
    """
    Evaluates an Ising / Pauli Hamiltonian on the unauthenticated PRISM Chemistry API.
    terms: list of [pauli_string, coefficient], e.g. [["Z0 Z1", -1.0], ["Z1 Z2", -1.0]]
    """
    payload = json.dumps({"num_qubits": num_qubits, "terms": terms}).encode("utf-8")
    req = urllib.request.Request(
        CHEMISTRY_API_URL,
        data=payload,
        headers={"Content-Type": "application/json", "User-Agent": "prism-validator/1.0"},
    )
    t0 = time.perf_counter()
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            if "latency_us" not in data:
                data["latency_us"] = (time.perf_counter() - t0) * 1e6
            return data
    except Exception as e:
        return {"status": "error", "ground_state_energy": None, "optimal_bitstring": None, "error": str(e), "latency_us": 0.0}


if __name__ == "__main__":
    print("Testing Project PRISM unauthenticated API connectivity...")
    test_res = prism_eval("4 * pi^3 + pi^2 + pi")
    print(f"Status: {test_res.get('status')}")
    print(f"Result: {test_res.get('result')}")
    print(f"Server-Side Latency: {test_res.get('latency_us', 0):.2f} µs")
