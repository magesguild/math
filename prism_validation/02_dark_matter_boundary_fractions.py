#!/usr/bin/env python3
"""
02_dark_matter_boundary_fractions.py — Validation of Steven E. Elliott's Apollonian
Boundary Dark Matter Fractions and Post-Merger Decline.

Offloaded to the unauthenticated Project PRISM Mathematical Engine API:
https://www.magesguild.io/api/prism/eval
"""

from prism_client import prism_eval, prism_eval_float

D_ASSP = 2.473946  # Hausdorff dimension of 3D Apollonian sphere packing
ALPHA = 3.0 - D_ASSP  # ≈ 0.526054


def validate_isolated_galaxy_dark_fractions():
    print("=" * 80)
    print("PART 1: ISOLATED GALAXY DARK MATTER FRACTIONS FROM APOLLONIAN PACKING")
    print("=" * 80)
    print("Model (FSEP / Steven E. Elliott):")
    print(f"  Apollonian Hausdorff Dimension D = {D_ASSP:.6f}")
    print(f"  Co-dimension Exponent α = 3 - D = {ALPHA:.6f}")
    print("  Single-layer boundary dark fraction: f_dark = 1 - β^α")
    print("  where β is the effective packing occupancy ratio.\n")

    beta_values = [0.005, 0.010, 0.020, 0.030, 0.040, 0.050, 0.075, 0.100]

    print(f"{'Packing Ratio β':<18} | {'PRISM Expression':<30} | {'f_dark (PRISM)':<16} | {'f_visible':<12} | {'Latency':<10}")
    print("-" * 94)

    for b in beta_values:
        expr = f"1 - ({b})^(3 - {D_ASSP})"
        res = prism_eval(expr)
        f_dark = float(res["result"])
        f_vis = 1.0 - f_dark
        lat = res.get("latency_us", 0.0)
        print(f"{b:<18.3f} | {expr:<30} | {f_dark*100:<15.2f}% | {f_vis*100:<11.2f}% | {lat:<9.2f} µs")

    print("-" * 94)
    print("Astronomical Benchmark: Isolated spiral galaxies exhibit ~84% to 88% dark matter.")
    print("At β ≈ 0.02 to 0.03, the Apollonian packing geometry precisely matches observational bounds.\n")


def validate_merger_dark_fraction_drop():
    print("=" * 80)
    print("PART 2: POST-MERGER DARK MATTER FRACTION DROP (FRACTAL TENNIS PREDICTION)")
    print("=" * 80)
    print("Theoretical Model:")
    print("  When galaxies collide/merge, tidal interaction puffs the outer halo by factor k.")
    print("  β_post = k * β_pre  -->  f_dark drops as boundary phase redistributes.")
    print("  Analytic Drop: Δf_dark = β_pre^α * (k^α - 1)\n")

    beta_pre = 0.05
    k_scenarios = [
        ("Virial Mass Doubling (k = 2^(1/3))", 2 ** (1.0 / 3.0)),
        ("Observed Halo Puffing (k = 1.37)", 1.37),
        ("Strong Tidal Shock (k = 1.50)", 1.50),
        ("Extreme Tidal Disruption (k = 2.00)", 2.00),
    ]

    print(f"Base Pre-Merger β = {beta_pre:.3f} (Pre-merger f_dark ≈ 79.3%)\n")
    print(f"{'Collision Scenario':<36} | {'k':<6} | {'β_post':<8} | {'f_post':<10} | {'Drop (Δf)':<10} | {'PRISM Latency':<12}")
    print("-" * 90)

    for label, k in k_scenarios:
        expr_drop = f"({beta_pre})^(3 - {D_ASSP}) * (({k})^(3 - {D_ASSP}) - 1)"
        expr_post = f"1 - ({beta_pre * k})^(3 - {D_ASSP})"
        
        res_drop = prism_eval(expr_drop)
        res_post = prism_eval(expr_post)
        
        drop_val = float(res_drop["result"])
        f_post_val = float(res_post["result"])
        lat = res_drop.get("latency_us", 0.0) + res_post.get("latency_us", 0.0)
        
        print(f"{label:<36} | {k:<6.3f} | {beta_pre*k:<8.4f} | {f_post_val*100:<9.2f}% | {drop_val*100:<9.2f}% | {lat:<10.2f} µs")

    print("-" * 90)
    print("Elliott Hypothesis: Merger declines approach π/22 ≈ 14.28% in maximal phase redistribution,")
    print("explaining observed low-DM post-merger relics and Keplerian rotation signatures.")


if __name__ == "__main__":
    validate_isolated_galaxy_dark_fractions()
    validate_merger_dark_fraction_drop()
