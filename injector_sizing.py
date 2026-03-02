"""
Pintle Injector Sizing Tool (Pressure-Fed Hypergolic Engine)

Implements the standard sizing sequence used in your report:
1) total mass flow from thrust and Isp
2) split fuel/oxidizer based on O/F
3) injector pressure drop as fraction of chamber pressure
4) required injection areas
5) injection velocities
6) pintle (fuel) diameter
7) approximate outer diameter for annular oxidizer region

Reference: equations and sizing logic from your report. (MMH/NTO pintle injector sizing) 
"""

from __future__ import annotations

import math
import argparse
from dataclasses import dataclass


G0 = 9.81  # m/s^2


@dataclass
class InjectorInputs:
    thrust_N: float                 # N
    isp_s: float                    # s
    of_ratio: float                 # O/F
    chamber_pressure_bar: float     # bar
    dp_fraction: float              # fraction of Pc (e.g., 0.15)
    rho_fuel_kg_m3: float           # kg/m^3
    rho_ox_kg_m3: float             # kg/m^3


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


def _validate(inp: InjectorInputs) -> None:
    if inp.thrust_N <= 0:
        raise ValueError("thrust_N must be > 0")
    if inp.isp_s <= 0:
        raise ValueError("isp_s must be > 0")
    if inp.of_ratio <= 0:
        raise ValueError("of_ratio must be > 0")
    if inp.chamber_pressure_bar <= 0:
        raise ValueError("chamber_pressure_bar must be > 0")
    if not (0 < inp.dp_fraction < 1):
        raise ValueError("dp_fraction must be between 0 and 1 (e.g., 0.10 to 0.20)")
    if inp.rho_fuel_kg_m3 <= 0 or inp.rho_ox_kg_m3 <= 0:
        raise ValueError("propellant densities must be > 0")


def size_pintle_injector(inp: InjectorInputs) -> InjectorResults:
    """
    Core sizing routine (matches the report's sequence).
    """
    _validate(inp)

    # Effective exhaust velocity
    ve = inp.isp_s * G0

    # Total mass flow
    mdot_total = inp.thrust_N / ve

    # Split fuel/oxidizer using O/F
    mdot_ox = mdot_total * (inp.of_ratio / (1.0 + inp.of_ratio))
    mdot_fuel = mdot_total - mdot_ox

    # Pressures
    pc = inp.chamber_pressure_bar * 1e5  # bar -> Pa
    dp = inp.dp_fraction * pc

    # Required injection areas
    # A = mdot / sqrt(2*rho*dp)
    area_fuel = mdot_fuel / math.sqrt(2.0 * inp.rho_fuel_kg_m3 * dp)
    area_ox = mdot_ox / math.sqrt(2.0 * inp.rho_ox_kg_m3 * dp)

    # Injection velocities (ideal)
    v_fuel = math.sqrt(2.0 * dp / inp.rho_fuel_kg_m3)
    v_ox = math.sqrt(2.0 * dp / inp.rho_ox_kg_m3)

    # Pintle diameter from fuel area (circular)
    # Afuel = (pi/4)*d^2  -> d = 2*sqrt(A/pi)
    d_pintle = 2.0 * math.sqrt(area_fuel / math.pi)

    # Approximate "outer diameter" containing annular oxidizer area + pintle cross-section
    # A_total = A_ox + A_pintle = (pi/4)*d_outer^2
    a_pintle = (math.pi / 4.0) * d_pintle**2
    d_outer = math.sqrt((4.0 / math.pi) * (area_ox + a_pintle))

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
    )


def _fmt_m(val_m: float) -> str:
    return f"{val_m:.6f} m ({val_m*1000:.2f} mm)"


def main() -> int:
    p = argparse.ArgumentParser(description="Pintle injector sizing (pressure-fed).")
    p.add_argument("--thrust", type=float, default=30000, help="Thrust [N]")
    p.add_argument("--isp", type=float, default=315, help="Isp [s]")
    p.add_argument("--of", type=float, default=2.16, help="Mixture ratio O/F [-]")
    p.add_argument("--pc_bar", type=float, default=20, help="Chamber pressure [bar]")
    p.add_argument("--dp_frac", type=float, default=0.15, help="ΔP fraction of Pc [-] (0-1)")
    p.add_argument("--rho_fuel", type=float, default=880, help="Fuel density [kg/m^3] (MMH ~880)")
    p.add_argument("--rho_ox", type=float, default=1440, help="Ox density [kg/m^3] (NTO ~1440)")

    args = p.parse_args()

    inp = InjectorInputs(
        thrust_N=args.thrust,
        isp_s=args.isp,
        of_ratio=args.of,
        chamber_pressure_bar=args.pc_bar,
        dp_fraction=args.dp_frac,
        rho_fuel_kg_m3=args.rho_fuel,
        rho_ox_kg_m3=args.rho_ox,
    )

    r = size_pintle_injector(inp)

    print("\n=== Pintle Injector Sizing Results ===")
    print(f"ve                : {r.ve_m_s:.1f} m/s")
    print(f"mdot_total         : {r.mdot_total_kg_s:.3f} kg/s")
    print(f"mdot_fuel          : {r.mdot_fuel_kg_s:.3f} kg/s")
    print(f"mdot_ox            : {r.mdot_ox_kg_s:.3f} kg/s")
    print(f"Pc                 : {r.pc_Pa/1e5:.2f} bar")
    print(f"ΔP_injector        : {r.dp_Pa/1e5:.2f} bar")
    print(f"A_fuel             : {r.area_fuel_m2:.6e} m^2")
    print(f"A_ox               : {r.area_ox_m2:.6e} m^2")
    print(f"v_inj_fuel (ideal) : {r.v_inj_fuel_m_s:.2f} m/s")
    print(f"v_inj_ox   (ideal) : {r.v_inj_ox_m_s:.2f} m/s")
    print(f"Pintle diameter    : {_fmt_m(r.pintle_diameter_m)}")
    print(f"Outer diameter est.: {_fmt_m(r.outer_diameter_m)}\n")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())