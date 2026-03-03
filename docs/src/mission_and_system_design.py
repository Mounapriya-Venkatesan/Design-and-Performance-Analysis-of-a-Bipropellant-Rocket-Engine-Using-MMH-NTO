# src/mission_and_system_design.py
# Mission + System Design calculations for a pressure-fed MMH/NTO lunar descent engine
# No external libraries needed.

from dataclasses import dataclass
import math


@dataclass
class MissionSystemInputs:
    # Mission requirement
    delta_v_mps: float = 1800.0  # m/s (LLO -> surface descent estimate)

    # Performance assumption
    isp_s: float = 315.0         # s (vacuum Isp)
    g0_mps2: float = 9.80665     # m/s^2

    # Mass assumption
    m_dry_kg: float = 1200.0     # kg

    # Engine sizing assumption
    thrust_N: float = 30_000.0   # N

    # System architecture assumption (for reporting only)
    pc_bar: float = 20.0         # bar (chamber pressure)
    dp_fraction: float = 0.15    # injector pressure drop fraction f, ΔP = f * Pc


@dataclass
class MissionSystemOutputs:
    # Mission mass sizing
    mass_ratio: float
    m_wet_kg: float
    m_prop_kg: float
    prop_fraction: float

    # Engine sizing
    ve_mps: float
    mdot_kgps: float
    burn_time_s: float

    # Injector ΔP (system-level)
    pc_Pa: float
    dp_Pa: float


def mission_and_system_design(inp: MissionSystemInputs) -> MissionSystemOutputs:
    # Basic validation
    if inp.delta_v_mps <= 0:
        raise ValueError("delta_v_mps must be > 0")
    if inp.isp_s <= 0 or inp.g0_mps2 <= 0:
        raise ValueError("isp_s and g0_mps2 must be > 0")
    if inp.m_dry_kg <= 0:
        raise ValueError("m_dry_kg must be > 0")
    if inp.thrust_N <= 0:
        raise ValueError("thrust_N must be > 0")
    if inp.pc_bar <= 0 or inp.dp_fraction <= 0:
        raise ValueError("pc_bar and dp_fraction must be > 0")

    # --- 1) Mass sizing from rocket equation ---
    # ΔV = Isp * g0 * ln(m_wet / m_dry)
    mass_ratio = math.exp(inp.delta_v_mps / (inp.isp_s * inp.g0_mps2))
    m_wet = mass_ratio * inp.m_dry_kg
    m_prop = m_wet - inp.m_dry_kg
    prop_fraction = m_prop / m_wet

    # --- 2) Engine sizing ---
    # Effective exhaust velocity
    ve = inp.isp_s * inp.g0_mps2  # m/s
    # Total mass flow rate
    mdot = inp.thrust_N / ve      # kg/s
    # Burn time estimate
    burn_time = m_prop / mdot     # s

    # --- 3) System-level injector pressure drop (reporting) ---
    pc_Pa = inp.pc_bar * 1e5      # bar -> Pa
    dp_Pa = inp.dp_fraction * pc_Pa

    return MissionSystemOutputs(
        mass_ratio=mass_ratio,
        m_wet_kg=m_wet,
        m_prop_kg=m_prop,
        prop_fraction=prop_fraction,
        ve_mps=ve,
        mdot_kgps=mdot,
        burn_time_s=burn_time,
        pc_Pa=pc_Pa,
        dp_Pa=dp_Pa,
    )


def pretty_print(inp: MissionSystemInputs, out: MissionSystemOutputs) -> None:
    print("\n=== Mission & System Design: Results ===")
    print(f"ΔV requirement:            {inp.delta_v_mps:.1f} m/s")
    print(f"Isp (vac):                 {inp.isp_s:.1f} s")
    print(f"Thrust (vac):              {inp.thrust_N/1000:.1f} kN")
    print(f"Dry mass:                  {inp.m_dry_kg:.1f} kg")

    print("\n--- Mass Sizing (Rocket Equation) ---")
    print(f"Mass ratio (m_wet/m_dry):  {out.mass_ratio:.4f}")
    print(f"Wet mass:                  {out.m_wet_kg:.1f} kg")
    print(f"Propellant mass:           {out.m_prop_kg:.1f} kg")
    print(f"Propellant fraction:       {out.prop_fraction:.3f}")

    print("\n--- Engine Sizing ---")
    print(f"Effective exhaust vel ve:  {out.ve_mps:.1f} m/s")
    print(f"Total mass flow mdot:      {out.mdot_kgps:.3f} kg/s")
    print(f"Estimated burn time:       {out.burn_time_s:.1f} s")

    print("\n--- System Pressure Drops (for injector sizing) ---")
    print(f"Chamber pressure Pc:       {out.pc_Pa/1e5:.2f} bar")
    print(f"Injector ΔP = f*Pc:        {out.dp_Pa/1e5:.2f} bar (f = {inp.dp_fraction:.2f})")


if __name__ == "__main__":
    inputs = MissionSystemInputs()
    outputs = mission_and_system_design(inputs)
    pretty_print(inputs, outputs)