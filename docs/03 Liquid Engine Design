# 03 – Liquid Engine System Design

## 3.1 Purpose of This Section

This section defines the **engine-level architecture** and sizing relationships that connect mission requirements
to subsystem design choices (pressurization, injector, chamber/nozzle geometry, and cooling).

The goal is to produce a coherent “flow-down” from:
**thrust + Isp targets → mass flow → chamber pressure → injector ΔP → chamber/nozzle geometry → thermal constraints**.

---

## 3.2 Engine Requirements (Top-Level)

| Requirement | Target Value |
|---|---:|
| Vacuum thrust, $T$ | 30 kN |
| Vacuum specific impulse, $I_{sp}$ | 315 s |
| Chamber pressure, $P_c$ | 20 bar |
| Propellants | MMH / NTO |
| Cycle | Pressure-fed |
| Injector type | Pintle |
| Throttle range | 3:1 |

---

## 3.3 Core Performance Relationships

### 3.3.1 Effective Exhaust Velocity

$$
v_e = I_{sp}\,g_0
$$

Using $I_{sp}=315\,\text{s}$ and $g_0=9.80665\,\text{m/s}^2$:

$$
v_e \approx 3090\,\text{m/s}
$$

---

### 3.3.2 Total Mass Flow Rate

$$
\dot{m} = \frac{T}{v_e}
$$

For $T=30{,}000\,\text{N}$:

$$
\dot{m} \approx \frac{30000}{3090} \approx 9.7\,\text{kg/s}
$$

---

### 3.3.3 Mixture Ratio (O/F) Split

Let $r = O/F$:

$$
\dot{m}_{ox} = \dot{m}\,\frac{r}{1+r}
$$

$$
\dot{m}_{fuel} = \dot{m}-\dot{m}_{ox}
$$

This split drives tank sizing, injector sizing, and cooling capacity (fuel is typically used for regenerative cooling).

---

## 3.4 Chamber and Nozzle Geometry

### 3.4.1 Throat Area and Throat Diameter

Throat area:

$$
A_t = \frac{\pi}{4}\,d_t^2
$$

The throat is a key driver for chamber volume, cooling heat flux, and nozzle geometry.

---

### 3.4.2 Expansion Ratio

Define expansion ratio:

$$
\varepsilon = \frac{A_e}{A_t}
$$

Exit area:

$$
A_e = \varepsilon\,A_t
$$

Exit diameter:

$$
d_e = d_t\,\sqrt{\varepsilon}
$$

A larger $\varepsilon$ increases vacuum performance but increases nozzle length and mass. This design uses a moderate expansion ratio consistent with lunar vacuum operation while controlling structural mass.

---

### 3.4.3 Characteristic Length (Combustion Performance)

Chamber volume relates to $L^*$:

$$
V_c = A_t\,L^*
$$

Given chamber cross-sectional area $A_c$, chamber length is:

$$
L_c = \frac{V_c}{A_c}
$$

The chosen $L^*$ ensures sufficient residence time for propellant mixing and combustion completion.

---

## 3.5 Injector Pressure Drop and Feed Pressure Flow-Down

Injector stability commonly uses a pressure drop fraction:

$$
\Delta P_{inj} = f\,P_c
$$

with typical $f = 0.15$ to $0.30$.

Required tank pressure (simplified) is:

$$
P_{tank} \ge P_c + \Delta P_{inj} + \Delta P_{lines}
$$

This equation links pressurization sizing to injector design.

---

## 3.6 Cooling and Materials Considerations (Design Driver)

Combustion temperatures are high (typically > 3000 K for hypergolic bipropellants), requiring:

- high-temperature chamber material selection
- regenerative cooling channel allowance
- thermal margin for long burn duration

Cooling design is treated as a core requirement because it affects:
- chamber wall thickness
- injector face heat soak
- nozzle throat survivability

---

## 3.7 Interfaces and Subsystem Dependencies

This engine design establishes key interfaces:

- **Pressurization system →** sets tank pressure boundary conditions  
- **Injector →** sets mass flow distribution and mixing quality  
- **Chamber/nozzle geometry →** determines performance and heat flux  
- **Cooling system →** ensures survivability at $P_c$ and burn duration  
- **Valves/feed lines →** contribute to pressure losses and reliability  

---

## 3.8 Section Summary

The liquid engine system design converted mission-level targets into engine-level sizing parameters:

- $I_{sp}$ and $T$ define $v_e$ and $\dot{m}$
- $P_c$ and injector drop fraction $f$ define feed system pressure requirements
- throat sizing and $\varepsilon$ define nozzle geometry for vacuum performance
- $L^*$ and chamber sizing provide combustion completion margin

These relationships form the baseline used in later sections for:
injector analytical design, pressurization sizing, nozzle/chamber CAD modeling, and cooling design.
