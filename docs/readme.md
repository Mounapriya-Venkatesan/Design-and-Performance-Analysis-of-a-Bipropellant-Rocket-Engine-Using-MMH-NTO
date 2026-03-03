# 📘 Engine Technical Documentation

### Pressure-Fed MMH/NTO Hypergolic Lunar Descent Engine

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Field](https://img.shields.io/badge/Field-Rocket%20Propulsion-orange)
![Cycle](https://img.shields.io/badge/Cycle-Pressure--Fed-green)
![Mission](https://img.shields.io/badge/Mission-Lunar%20Descent-purple)
![Cooling](https://img.shields.io/badge/Cooling-Regenerative-red)

---

## 🧠 Analytical | Parametric | System-Level Engine Design

This documentation contains the complete analytical and conceptual design workflow for a **30 kN pressure-fed hypergolic bipropellant rocket engine** using **MMH/NTO**.

It transforms classical propulsion theory into a structured engineering system design.

---

# 📂 Documentation Modules

---

## 🛰 1️ Mission & System Design
📄 `01 mission and system design.md`

Covers:

- Lunar descent ΔV (~1800 m/s)
- Rocket equation mass sizing
- Wet / dry mass estimation
- Thrust selection (30 kN)
- Mass flow rate calculation
- Burn time estimation
- Initial CAD geometry

Key Equation:
### Rocket Equation

$$
\Delta V = I_{sp} \cdot g_0 \cdot \ln \left(\frac{m_{wet}}{m_{dry}}\right)
$$

Where:

- $I_{sp}$ = Specific impulse (s)  
- $g_0$ = 9.81 m/s²  
- $m_{wet}$ = Initial mass  
- $m_{dry}$ = Final mass  
---

## 🧯 2️ Pressurization System Design
📄 `pressurization_system_design.md`

- Helium pressurization architecture
- Tank pressure (24 bar)
- Chamber pressure (20 bar)
- Helium storage (200 bar)
- Ideal gas law helium sizing
- System block diagram

---

## 🔥 3️ Liquid Engine System Design
📄 `liquid_engine_system_design.md`

- Chamber sizing via L*
- Throat diameter selection
- Expansion ratio trade study
- Exit diameter derivation
- Performance balancing

Core Relations:

$$
A_t = \frac{\pi}{4} d_t^2
$$

Where:  
- $A_t$ = Throat area  
- $d_t$ = Throat diameter  

---

$$
V_c = A_t \cdot L^*
$$

Where:  
- $V_c$ = Chamber volume  
- $L^*$ = Characteristic length  

---

$$
d_e = d_t \sqrt{\varepsilon}
$$

Where:  
- $d_e$ = Exit diameter  
- $\varepsilon$ = Expansion ratio  
---

## 💉 4️ Injector Analytical Design
📁 `pintle-injector-sizing/`

Implements:

- Mass flow derivation
- O/F split
- Injector pressure drop sizing
- Injection area calculation
- Pintle diameter sizing
- Annular gap determination
- Parametric & uncertainty analysis

Core Equation:

$$
A = \frac{\dot{m}}{\sqrt{2 \rho \Delta P}}
$$

Where:  
- $A$ = Required injection area  
- $\dot{m}$ = Mass flow rate  
- $\rho$ = Propellant density  
- $\Delta P$ = Injector pressure drop  

---

## 🧪 5️ Combustion Analysis (NASA CEA)
📄 `combustion_analysis_cea.md`

Thermodynamic modeling includes:

- Isp vs O/F
- C* vs Chamber Pressure
- Tc vs O/F
- Exhaust species evaluation

Results:

- Isp ≈ 288–315 s
- Tc ≈ 3130 K
- C* ≈ 1600 m/s

---

## ❄️ 6️ Cooling System Design
📄 `cooling_system_design.md`

- Heat flux estimation
- Regenerative cooling architecture
- Wall thickness approximation
- Material selection (GRCop-84, Inconel)
- Thermal safety considerations

Heat Flux Model:

$$
q'' = 0.5 \, P_c \, v_e
$$

Where:  
- $q''$ = Heat flux  
- $P_c$ = Chamber pressure  
- $v_e$ = Exhaust velocity  
---

# 📊 Figures Directory

All plots, CAD renders, and schematics are stored in:

Includes:

- Injector CAD
- Engine CAD
- CEA performance curves
- Pressurization diagram
- Cooling schematic

---

# 🚀 Engine Summary

| Parameter | Value |
|------------|--------|
| Thrust | 30 kN |
| Propellants | MMH / NTO |
| Cycle | Pressure-Fed |
| Chamber Pressure | 20 bar |
| Expansion Ratio | 30–50 |
| Isp (Vacuum) | ~315 s |
| Cooling | Regenerative |
| Throttle | 3:1 |

---

# 🎯 Design Philosophy

This engine design prioritizes:

- Reliability (pressure-fed architecture)
- Thermal robustness
- Analytical transparency
- Manufacturability
- Lunar mission suitability

---

# 🛰 Author

**Mounapriya Venkatesan**  
Graduate Student – Space Studies  
Rice University  





