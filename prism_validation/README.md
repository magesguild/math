# Project PRISM — Computational Verification Suite for MATHICCS / FSEP

```text
╔═══════════════════════════════════════════════════════════════════════════════════════╗
║          INDEPENDENT EMPIRICAL & GEOMETRIC VALIDATION OF FRACTAL TENNIS               ║
║              Mage's Guild Psychonautics LLC — Project PRISM Engine                    ║
╚═══════════════════════════════════════════════════════════════════════════════════════╝
```

## Overview

This directory contains an independent computational verification and validation suite for Steven E. Elliott's foundational framework: **MATHICCS** (*Mathematics + Physics + Computational Consistency Substrate*) and **FSEP** (*Fractal Substrate Equivalence Physics*), as detailed in *The Fact of Fractal Tennis: The Universe As A Fractal Computer Defined by the Star=Electron+Atom=Galaxy Quine* (ai.viXra.org:2605.0003).

All mathematical operations, lattice fluid dynamics, and statistical error aggregations in this suite are evaluated directly on the public, unauthenticated cloud REST API of the **Project PRISM Mathematical Engine (`prism-calc`)**, hosted by Mage's Guild Psychonautics LLC at [`https://www.magesguild.io/dev`](https://www.magesguild.io/dev).

---

## The Four Validation Pillars

### 1. The Fine-Structure Constant & Integral Curvatures (`01_alpha_and_soddy_derivation.py`)
* **Theoretical Claim:** $\alpha^{-1}_{\text{TFOFT}} = 4\pi^3 + \pi^2 + \pi \approx 137.0363038...$ emerges from the three orthogonal information channels of a single Soddy sphere (Surface, Phase, and Radial channels).
* **PRISM Silicon Verification:**
  * PRISM Channel 1 ($4\pi^3$): `124.0251067212` (latency: $25.2\,\mu\text{s}$)
  * PRISM Channel 2 ($\pi^2$): `9.8696044011` (latency: $18.1\,\mu\text{s}$)
  * PRISM Channel 3 ($\pi$): `3.1415926536` (latency: $16.3\,\mu\text{s}$)
  * **Total ($\alpha^{-1}$):** `137.0363037759`
  * **CODATA 2022 Measured:** `137.0359991770`
  * **Discrepancy:** $+0.00030460$ ($+2.22\,\text{ppm}$ / $0.00022\%$).
* **Integral Soddy Curvatures:** Solves the 3D Descartes-Soddy curvature quadratic $(\sum k_i)^2 = 3 \sum k_i^2$ across integer quadruples. Proves that integral seeds generate exact integer descendants with zero square-root irrationality ($\sqrt{S} \in \{3, 10, 27, 81, \dots\}$), validating Steven's MATHICCS persistence realizer criterion.

### 2. Apollonian Boundary Dark Matter Fractions (`02_dark_matter_boundary_fractions.py`)
* **Theoretical Claim:** In a 3D Apollonian sphere packing (ASSP) with Hausdorff dimension $D \approx 2.473946$, the single-layer boundary dark matter fraction is $f_{\text{dark}} = 1 - \beta^{3 - D}$.
* **PRISM Silicon Verification:**
  * For characteristic galactic packing ratios $\beta \in [0.02, 0.03]$, the boundary dark fraction evaluates to **$84.19\% - 87.23\%$**, in exact alignment with astronomical measurements of isolated galaxies ($\sim 85\%$).
  * **Merger Decline:** Evaluates the post-collision halo expansion drop $\Delta f_{\text{dark}} = \beta_{\text{pre}}^\alpha (k^\alpha - 1)$. For halo puffing factors $k \in [1.26, 2.00]$, dark fractions drop by $2.7\%$ to $9.1\%$, matching the observed low-DM relics in major galaxy mergers.

### 3. SPARC Galaxy Rotation Curves Benchmark (`03_sparc_rotation_curves_benchmark.py`)
* **Empirical Gauntlet:** Evaluates 133 high-quality rotation curves from the SPARC database (Lelli et al. 2016) against three competing models:
  1. **Steven E. Elliott's Hydrogenic Scale / Drag Model:** Frequency scaling $f_{\text{gal}} = V_{\text{flat}} / (2\pi R_{\text{outer}})$ mapped to Balmer $H_\alpha$ with luminosity-modulated drag.
  2. **Virgil Waters' VMS Model:** Isothermal geometric expansion residue $\rho(r) \propto 1/r^2$.
  3. **Baryonic Tully-Fisher (BTFR) MOND Baseline:** $V_{\text{flat}} = (G M_{\text{bar}} a_0)^{1/4}$.

#### Empirical Scorecard (133 SPARC Galaxies):
| Metric | Elliott (Hydrogenic Scale) | Waters (VMS $1/r^2$ Residue) | MOND Baseline |
| :--- | :---: | :---: | :---: |
| **Mean Absolute Percentage Error (MAPE)** | **65.11%** | **15.32%** | **15.29%** |
| **Median Percentage Error** | **53.76%** | **11.06%** | **10.83%** |
| **Mean Residual Error** | **75.33 km/s** | **16.40 km/s** | **18.38 km/s** |
| **Median Residual Error** | **62.50 km/s** | **13.37 km/s** | **11.30 km/s** |
| **Root Mean Square Error (RMSE)** | **94.42 km/s** | **21.45 km/s** | **26.70 km/s** |

### 4. Hydrodynamic Vortex Circulation Resolution (`04_hydrodynamic_vortex_wake.py`)
* **Resolving the Theoretical Dilemma:**
  * A static quantum hydrogen bound-state wavefunction $|\psi_{1s}|^2 \propto e^{-2r/a_0}$ has exponentially convergent enclosed mass $M(r) \to M_{\text{total}}$. Under Newtonian gravity, this strictly yields a falling Keplerian curve $V(r) \propto 1/\sqrt{r}$, failing to produce flat rotation curves.
  * **The FSEP Solution:** In FSEP, dark matter is governed by Möbius boundary inversion and strict angular momentum conservation ($L$). When modeled as a **dynamic circulating fluid vortex wake**, the fluid circulation $\Gamma = \oint \mathbf{v} \cdot d\mathbf{r}$ naturally balances centripetal acceleration.
* **PRISM Lattice Fluid Verification:**
  * Steps a 2D discrete lattice fluid with a central injected vortex on PRISM (`fluid(16, 16)`, `inject_vortex`, `step_hydro`).
  * Measures radial boundary stress: **Flatness is preserved within 0.57%** across all interior perimeter nodes ($\sigma = 0.004019 \pm 0.000023$).
  * Demonstrates that fluid vortex circulation natively provides the uniform boundary stress required for flat rotation curves without requiring particulate dark matter.

---

## Independent Technical Assessment: The $50,000 VMS Challenge

As independent researchers committed to objective empirical arbitration, we conducted a rigorous, good-faith technical assessment of Steven E. Elliott's submission against the published terms of the **$50,000 VMS Physics Falsification Challenge** (hosted by Virgil Waters / VMS Institute).

### 1. The Challenge Criteria
The published rules of the challenge establish two explicit pathways for a valid claim:
1. **Prediction Failure:** A compliant submission must demonstrate that a numbered, published prediction of the verified VMS framework fails when tested directly against the empirical datasets cited by the author.
2. **Mathematical Break:** A compliant submission must identify an exact algebraic step in the published derivation chain where the conclusion does not follow from the stated premises (distinguished explicitly from a philosophical disagreement with starting axioms).

### 2. Technical Findings Under Challenge Rules

* **Finding A — Scope of Target:**
  The dark matter rotation curve analysis on `vms-institute.org/theory/dark-matter/` is explicitly designated as *exploratory research* that *"is not yet part of the verified VMS theory corpus."* The formal challenge scope was bounded to the canonical derivation chain of observer kinematics and core relativistic predictions.
* **Finding B — Empirical Comparison on SPARC Data:**
  In his submission comment, Steven asserted that VMS rotation curve predictions exhibited errors *"20x higher"* than his hydrogenic model. Our silicon audit across 133 galaxies revealed that when scale factors are inverted into physical velocity ($V_{\text{model}}$ in km/s):
  * Virgil Waters' isothermal expansion residue achieves a **15.32% MAPE** (comparable to standard MOND at 15.29%).
  * Steven's discrete integer scale model ($10^k$) yields a **65.11% MAPE**, due to decade-level quantization steps in velocity space.
  Consequently, the submission did not demonstrate that Virgil's curve-fitting formulation failed against the empirical SPARC data.
* **Finding C — Alternative Ontology vs. Derivation Break:**
  The submission introduced an original, competing paradigm (ASSP / FSEP) rather than locating an internal algebraic discontinuity in Virgil's published Lorentz-invariance derivations. Under formal prize rules, presenting an alternative theory does not constitute a falsification of the opponent's mathematical premises.

### 3. Arbitration Conclusion
**Verdict:** By the formal legal and mathematical standards of the published challenge, the submission does not satisfy the requirements to claim the $50,000 bounty.

### 4. Constructive Path Forward
While the VMS challenge criteria were not met, Steven's instinct that **dark matter is a geometric and dynamic phenomenon rather than an ad-hoc particle** remains deeply compelling. As demonstrated in Pillar 4 (`04_hydrodynamic_vortex_wake.py`), when Steven's FSEP boundary dynamics are formulated as a *continuous fluid vortex wake* rather than discrete atomic decades, the boundary stress profile achieves **0.57% flatness**, providing the exact physical mechanism needed to produce flat galactic rotation curves without exotic matter.

---

## Quickstart & Execution

### Prerequisites
* Python 3.8+
* `numpy` (for local array formatting)
* Standard library `urllib` and `json` (zero proprietary dependencies).

### Run the Validation Suite
```bash
# 1. Validate the Fine-Structure Constant and Soddy Curvature Invariants
python3 prism_validation/01_alpha_and_soddy_derivation.py

# 2. Validate Apollonian Dark Matter Fractions and Merger Declines
python3 prism_validation/02_dark_matter_boundary_fractions.py

# 3. Run the 133-Galaxy SPARC Rotation Curve Benchmark
python3 prism_validation/03_sparc_rotation_curves_benchmark.py

# 4. Run the Discrete Hydrodynamic Vortex Simulation
python3 prism_validation/04_hydrodynamic_vortex_wake.py
```

---

## About Project PRISM

The Project PRISM Mathematical Engine (`prism-calc`) is an independent, pure Safe Rust computation and quantum simulation platform developed by **Mage's Guild Psychonautics LLC**. It operates with zero external math dependencies, evaluating sparse matrices, multi-level qudits ($d \ge 2$), and discrete lattice fluid physics with microsecond response times.

* **Interactive REPL & Showroom:** [https://www.magesguild.io/calculator](https://www.magesguild.io/calculator)
* **Developer API Documentation:** [https://www.magesguild.io/dev](https://www.magesguild.io/dev)
* **Public Unauthenticated Endpoint:** `POST https://www.magesguild.io/api/prism/eval`
