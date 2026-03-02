import os
import matplotlib.pyplot as plt
from injector_sizing import InjectorInputs, size_pintle_injector

FIG_DIR = os.path.join(os.path.dirname(__file__), "..", "figures")
os.makedirs(FIG_DIR, exist_ok=True)


def sweep_of():
    of_values = [1.6 + 0.02*i for i in range(51)]  # 1.6 to 2.6
    pintle_mm = []
    outer_mm = []
    gap_mm = []

    for of in of_values:
        inp = InjectorInputs(
            thrust_N=30000, isp_s=315, of_ratio=of,
            chamber_pressure_bar=20, dp_fraction=0.15,
            rho_fuel_kg_m3=880, rho_ox_kg_m3=1440,
            cd_fuel=0.9, cd_ox=0.9
        )
        r = size_pintle_injector(inp)
        pintle_mm.append(r.pintle_diameter_m * 1000)
        outer_mm.append(r.outer_diameter_m * 1000)
        gap_mm.append(r.annular_gap_width_m * 1000)

    plt.figure()
    plt.plot(of_values, pintle_mm, label="Pintle d (mm)")
    plt.plot(of_values, outer_mm, label="Outer d (mm)")
    plt.plot(of_values, gap_mm, label="Gap (mm)")
    plt.xlabel("Mixture Ratio (O/F)")
    plt.ylabel("Dimension (mm)")
    plt.legend()
    out = os.path.join(FIG_DIR, "sweep_of.png")
    plt.savefig(out, dpi=200, bbox_inches="tight")
    print(f"Saved: {out}")


def sweep_pc():
    pc_values = [10 + i for i in range(21)]  # 10 to 30 bar
    gap_mm = []

    for pc in pc_values:
        inp = InjectorInputs(
            thrust_N=30000, isp_s=315, of_ratio=2.16,
            chamber_pressure_bar=pc, dp_fraction=0.15,
            rho_fuel_kg_m3=880, rho_ox_kg_m3=1440,
            cd_fuel=0.9, cd_ox=0.9
        )
        r = size_pintle_injector(inp)
        gap_mm.append(r.annular_gap_width_m * 1000)

    plt.figure()
    plt.plot(pc_values, gap_mm)
    plt.xlabel("Chamber Pressure Pc (bar)")
    plt.ylabel("Annular Gap Width (mm)")
    out = os.path.join(FIG_DIR, "sweep_pc.png")
    plt.savefig(out, dpi=200, bbox_inches="tight")
    print(f"Saved: {out}")


if __name__ == "__main__":
    sweep_of()
    sweep_pc()