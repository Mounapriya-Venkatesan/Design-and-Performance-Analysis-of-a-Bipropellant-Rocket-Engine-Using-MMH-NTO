from __future__ import annotations
import math
import argparse
from dataclasses import dataclass

G0 = 9.81  # m/s^2


@dataclass
class InjectorInputs:
    thrust_N: float
    isp_s: float
    of_ratio: float
    chamber_pressure_bar: float
    dp_fraction: float
    rho_fuel_kg_m3: float
    rho_ox_kg_m3: float
    cd_fuel: float = 1.0   # discharge coefficient (0.6–0.95 typical)
    cd_ox: float = 1.0


@dataclass
class InjectorResults:
    ve_m_s: float
    mdot_total_kg_s: float
    mdot_fuel_kg_s: float
    mdot_ox_kg_s: float
    pc_Pa: float
    dp_Pa: float
    area_fuel_m2: float
    area_ox_m2: float
    v_inj_fuel_m_s: float
    v_inj_ox_m_s: float
    pintle_diameter_m: float
    outer_diameter_m: float
    annular_gap_width_m: float


def _validate(inp: InjectorInputs) -> None:
    if inp.thrust_N <= 0: raise ValueError("thrust_N must be > 0")
    if inp.isp_s <= 0: raise ValueError("isp_s must be > 0")
    if inp.of_ratio <= 0: raise ValueError("of_ratio must be > 0")
    if inp.chamber_pressure_bar <= 0: raise ValueError("chamber_pressure_bar must be > 0")
    if not (0 < inp.dp_fraction < 1): raise ValueError("dp_fraction must be between 0 and 1")
    if inp.rho_fuel_kg_m3 <= 0 or inp.rho_ox_kg_m3 <= 0: raise ValueError("densities must be > 0")
    if not (0 < inp.cd_fuel <= 1): raise ValueError("cd_fuel must be (0,1]")
    if not (0 < inp.cd_ox <= 1): raise ValueError("cd_ox must be (0,1]")


def size_pintle_injector(inp: InjectorInputs) -> InjectorResults:
    """
    Adds:
    - Discharge coefficient correction: A = mdot / (Cd * sqrt(2 rho ΔP))
    - Annular gap width: g = (d_outer - d_pintle)/2
    """
    _validate(inp)

    ve = inp.isp_s * G0
    mdot_total = inp.thrust_N / ve

    mdot_ox = mdot_total * (inp.of_ratio / (1.0 + inp.of_ratio))
    mdot_fuel = mdot_total - mdot_ox

    pc = inp.chamber_pressure_bar * 1e5  # bar -> Pa
    dp = inp.dp_fraction * pc

    # Areas with Cd correction
    # A = mdot / (Cd * sqrt(2 rho dp))
    area_fuel = mdot_fuel / (inp.cd_fuel * math.sqrt(2.0 * inp.rho_fuel_kg_m3 * dp))
    area_ox = mdot_ox / (inp.cd_ox * math.sqrt(2.0 * inp.rho_ox_kg_m3 * dp))

    # Ideal injection velocities (does not include Cd losses; Cd affects required area)
    v_fuel = math.sqrt(2.0 * dp / inp.rho_fuel_kg_m3)
    v_ox = math.sqrt(2.0 * dp / inp.rho_ox_kg_m3)

    # Pintle diameter from fuel area
    d_pintle = 2.0 * math.sqrt(area_fuel / math.pi)

    # Outer diameter for annulus area: Aox = (pi/4)*(d_outer^2 - d_pintle^2)
    d_outer = math.sqrt((4.0 / math.pi) * area_ox + d_pintle**2)

    # Annular gap width (radial)
    gap = 0.5 * (d_outer - d_pintle)

    return InjectorResults(
        ve_m_s=ve,
        mdot_total_kg_s=mdot_total,
        mdot_fuel_kg_s=mdot_fuel,
        mdot_ox_kg_s=mdot_ox,
        pc_Pa=pc,
        dp_Pa=dp,
        area_fuel_m2=area_fuel,
        area_ox_m2=area_ox,
        v_inj_fuel_m_s=v_fuel,
        v_inj_ox_m_s=v_ox,
        pintle_diameter_m=d_pintle,
        outer_diameter_m=d_outer,
        annular_gap_width_m=gap,
    )


def _fmt_mm(m: float) -> str:
    return f"{m*1000:.2f} mm"


def main() -> int:
    p = argparse.ArgumentParser(description="Pintle injector sizing (pressure-fed) with Cd + gap width.")
    p.add_argument("--thrust", type=float, default=30000)
    p.add_argument("--isp", type=float, default=315)
    p.add_argument("--of", type=float, default=2.16)
    p.add_argument("--pc_bar", type=float, default=20)
    p.add_argument("--dp_frac", type=float, default=0.15)
    p.add_argument("--rho_fuel", type=float, default=880)
    p.add_argument("--rho_ox", type=float, default=1440)
    p.add_argument("--cd_fuel", type=float, default=0.9)
    p.add_argument("--cd_ox", type=float, default=0.9)
    args = p.parse_args()

    inp = InjectorInputs(
        thrust_N=args.thrust,
        isp_s=args.isp,
        of_ratio=args.of,
        chamber_pressure_bar=args.pc_bar,
        dp_fraction=args.dp_frac,
        rho_fuel_kg_m3=args.rho_fuel,
        rho_ox_kg_m3=args.rho_ox,
        cd_fuel=args.cd_fuel,
        cd_ox=args.cd_ox,
    )

    r = size_pintle_injector(inp)

    print("\n=== Pintle Injector Sizing Results ===")
    print(f"mdot_total      : {r.mdot_total_kg_s:.3f} kg/s")
    print(f"mdot_fuel       : {r.mdot_fuel_kg_s:.3f} kg/s")
    print(f"mdot_ox         : {r.mdot_ox_kg_s:.3f} kg/s")
    print(f"Pc              : {r.pc_Pa/1e5:.2f} bar")
    print(f"ΔP              : {r.dp_Pa/1e5:.2f} bar")
    print(f"A_fuel          : {r.area_fuel_m2:.6e} m^2 (Cd corrected)")
    print(f"A_ox            : {r.area_ox_m2:.6e} m^2 (Cd corrected)")
    print(f"pintle diameter : {_fmt_mm(r.pintle_diameter_m)}")
    print(f"outer diameter  : {_fmt_mm(r.outer_diameter_m)}")
    print(f"annular gap     : {_fmt_mm(r.annular_gap_width_m)}  (radial)\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())