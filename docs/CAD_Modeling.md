# 10. CAD Modeling and Final Assembly

The 3D CAD models were developed to validate geometric feasibility, injector integration, structural compatibility, and assembly alignment for the pressure-fed MMH/N₂O₄ lunar descent engine.

The modeling process followed a parametric approach derived from RPA and analytical sizing calculations.

---

## 10.1 Chamber and Nozzle Model

![Chamber and Nozzle CAD](docs/figures/chamber_nozzle_cad.png)

**Figure 7:** CAD model of the combustion chamber and nozzle generated based on RPA-defined geometry.

The chamber and nozzle geometry were generated using:

- Chamber pressure: 20 bar  
- Characteristic length: \( L^* \)  
- Throat diameter: \( d_t \)  
- Expansion ratio: \( \varepsilon \)

### Governing Relations

Throat area:

$$
A_t = \frac{\pi}{4} d_t^2
$$

Chamber volume:

$$
V_c = A_t \cdot L^*
$$

Exit diameter:

$$
d_e = d_t \sqrt{\varepsilon}
$$

The bell nozzle was vacuum-optimized for lunar operation and designed to minimize divergence losses while maintaining structural feasibility.

---

## 10.2 Pintle Injector Schematic

![Pintle Injector](docs/figures/pintle_design.png)

**Figure 8:** Pintle injector schematic showing central core and outer annular oxidizer ring.

The injector design consists of:

- Central fuel pintle
- Annular oxidizer flow passage
- Flanged mounting interface

Annular gap defined as:

$$
g = \frac{d_{outer} - d_{pintle}}{2}
$$

This configuration enables:

- Stable radial mixing
- Throttle capability
- Reduced combustion instability risk

---

## 10.3 Final Engine Assembly View
![Sectioned Assembly](docs/figures/engine_section.png)

**Figure 9:** Full 3D engine assembly showing flanged injector top, combustion chamber, and parabolic nozzle.

**Figure 10:** Sectioned view revealing internal hollow nozzle and combustion chamber geometry.

The full assembly integrates:

- Injector head and feed interface
- Combustion chamber
- Converging-diverging nozzle
- Structural flange connections

The sectioned view confirms:

- Proper injector alignment
- Smooth internal flow transition
- Continuous chamber-to-throat contour
- Hollow structural design for mass reduction

---

## Structural Verification

Thin-wall stress approximation:

$$
\sigma = \frac{P_c r}{t}
$$

Wall thickness requirement:

$$
t = \frac{P_c r}{\sigma_{allow}}
$$

Material assumptions:

- Liner: Copper alloy (high thermal conductivity)
- Jacket: Inconel 718
- Safety factor > 1.5

---

## Summary

The CAD modeling phase validates:

- Geometric feasibility
- Thermochemical-derived sizing
- Injector integration
- Structural viability
- Manufacturability potential

The assembled model confirms readiness for:

- Structural FEA
- Thermal analysis
- Flow simulation
- Detailed manufacturing review

This completes the geometric validation phase of the pressure-fed bipropellant engine design.
