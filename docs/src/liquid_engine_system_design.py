# src/liquid_engine_system_design.py
# Liquid Engine System Design Calculations
# Pressure-fed MMH/NTO lunar descent engine

from dataclasses import dataclass
import math


@dataclass
class EngineSystemInputs:
    # Performance targets
    thrust_N: float = 30_000.0
    isp_s: float = 315.0
    g0_mps2: float = 9.80665

    # Chamber conditions
    pc_bar: float = 20.0
    injector_dp_fraction: float = 0.15

    # Geometry assumptions
    expansion_ratio: float = 30.0
    L_star_m: float = 1.0
    chamber_diameter_m: float = 0.075

    # Mixture ratio
    of_ratio: float = 1.6


@dataclass
class EngineSystemOutputs:
    ve_mps: float
    mdot_total_kgps: float
    mdot_ox_kgps: float
    mdot_fuel_kgps: float
    throat_area_m2: float
    throat_diameter_m: float
    exit_diameter_m: float
    chamber_volume_m3: float
    chamber_length_m: float
    injector_dp_bar: float


def liquid_engine_system_design(inp: EngineSystemInputs) -> EngineSystemOutputs:

    # 1️⃣ Effective exhaust velocity
    ve = inp.isp_s * inp.g0_mps2

    # 2️⃣ Total mass flow
    mdot_total = inp.thrust_N / ve

    # 3️⃣ O/F mass split
    mdot_ox = mdot_total * (inp.of_ratio / (1 + inp.of_ratio))
    mdot_fuel = mdot_total - mdot_ox

    # 4️⃣ Throat area from ideal thrust equation approximation
    # Simplified choked-flow relation:
    # mdot = Pc * At / c*
    # Use approximate c* = 1600 m/s for MMH/NTO (typical)
    c_star = 1600.0
    pc_Pa = inp.pc_bar * 1e5

    throat_area = mdot_total * c_star / pc_Pa

    throat_diameter = math.sqrt(4 * throat_area / math.pi)

    # 5️⃣ Exit diameter
    exit_area = inp.expansion_ratio * throat_area
    exit_diameter = math.sqrt(4 * exit_area / math.pi)

    # 6️⃣ Chamber volume
    chamber_volume = throat_area * inp.L_star_m

    chamber_area = math.pi / 4 * inp.chamber_diameter_m**2
    chamber_length = chamber_volume / chamber_area

    # 7️⃣ Injector pressure drop
    injector_dp_bar = inp.injector_dp_fraction * inp.pc_bar

    return EngineSystemOutputs(
        ve_mps=ve,
        mdot_total_kgps=mdot_total,
        mdot_ox_kgps=mdot_ox,
        mdot_fuel_kgps=mdot_fuel,
        throat_area_m2=throat_area,
        throat_diameter_m=throat_diameter,
        exit_diameter_m=exit_diameter,
        chamber_volume_m3=chamber_volume,
        chamber_length_m=chamber_length,
        injector_dp_bar=injector_dp_bar,
    )


if __name__ == "__main__":
    inputs = EngineSystemInputs()
    outputs = liquid_engine_system_design(inputs)

    print("\n=== Liquid Engine System Design Results ===")

    print("\n--- Performance ---")
    print(f"Effective exhaust velocity: {outputs.ve_mps:.1f} m/s")
    print(f"Total mass flow: {outputs.mdot_total_kgps:.3f} kg/s")

    print("\n--- Mixture Split ---")
    print(f"Oxidizer mass flow: {outputs.mdot_ox_kgps:.3f} kg/s")
    print(f"Fuel mass flow: {outputs.mdot_fuel_kgps:.3f} kg/s")

    print("\n--- Geometry ---")
    print(f"Throat diameter: {outputs.throat_diameter_m*1000:.2f} mm")
    print(f"Exit diameter: {outputs.exit_diameter_m*1000:.2f} mm")
    print(f"Chamber length: {outputs.chamber_length_m*1000:.1f} mm")

    print("\n--- Pressure ---")
    print(f"Injector ΔP: {outputs.injector_dp_bar:.2f} bar")