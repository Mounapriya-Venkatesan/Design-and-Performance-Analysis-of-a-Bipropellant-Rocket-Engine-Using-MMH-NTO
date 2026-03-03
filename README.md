# 🚀 Design and Performance Analysis of a Bipropellant Rocket Engine (MMH/NTO)

![Field](https://img.shields.io/badge/Field-Rocket%20Propulsion-orange)
![Cycle](https://img.shields.io/badge/Cycle-Pressure--Fed-green)
![Propellant](https://img.shields.io/badge/Propellants-MMH%20%2F%20NTO-purple)
![Thrust](https://img.shields.io/badge/Thrust-30%20kN-blue)
![Mission](https://img.shields.io/badge/Mission-Lunar%20Descent-red)

---

## 📌 Project Overview

This repository presents a **complete conceptual design and analytical performance evaluation** of a **30 kN pressure-fed hypergolic bipropellant rocket engine** using **Monomethylhydrazine (MMH)** and **Nitrogen Tetroxide (NTO)**.

The engine is designed for **robotic lunar descent operations**, balancing:

- Performance
- Reliability
- Structural simplicity
- Thermal safety
- Manufacturability

The project integrates propulsion theory, thermodynamics, fluid mechanics, heat transfer, and system-level design into a structured engineering workflow.

---

# 🛰 Mission Objective

Design a throttleable pressure-fed engine capable of:

- ΔV ≈ 1800 m/s (Lunar descent)
- Vacuum thrust: 30 kN
- Throttle range: 3:1
- High reliability (hypergolic ignition)
- Regenerative thermal protection

---

# ⚙️ Engine Summary

| Parameter | Value |
|------------|--------|
| Propellants | MMH / NTO |
| Cycle | Pressure-Fed |
| Vacuum Thrust | 30 kN |
| Chamber Pressure | 20 bar |
| Expansion Ratio | 30–50 |
| Specific Impulse (Vac) | ~315 s |
| Mixture Ratio (O/F) | 2.16 |
| Cooling Method | Regenerative |
| Pressurant | Helium (200 bar storage) |

---

# 🔬 Analytical Foundations

### Rocket Equation

$$
\Delta V = I_{sp} \cdot g_0 \cdot \ln \left(\frac{m_{wet}}{m_{dry}}\right)
$$

---

### Throat Area

$$
A_t = \frac{\pi}{4} d_t^2
$$

---

### Chamber Volume

$$
V_c = A_t \cdot L^*
$$

---

### Nozzle Exit Diameter

$$
d_e = d_t \sqrt{\varepsilon}
$$

---

### Injector Sizing

$$
A = \frac{\dot{m}}{\sqrt{2 \rho \Delta P}}
$$

---

### Heat Flux Estimate

$$
q'' = \frac{1}{2} P_c v_e
$$

---

# 🧪 Combustion Analysis (NASA CEA)

Thermodynamic modeling performed using **NASA Chemical Equilibrium with Applications (CEA)**.

Outputs include:

- Isp vs O/F analysis  
- Characteristic velocity (C*)  
- Chamber temperature (Tc)  
- Exhaust species breakdown  

Peak performance observed near **O/F ≈ 2.1–2.2**.

---

# 💉 Injector Design

A **single-element pintle injector** was selected for:

- Deep throttling capability  
- Hypergolic reliability  
- Stable spray formation  
- Apollo LMDE heritage  

Includes:

- Analytical area sizing  
- Pintle diameter determination  
- Annular gap calculation  
- Pressure drop optimization  
- Parametric sweeps & uncertainty analysis  

---

# ❄️ Thermal Management

Regenerative cooling implemented using MMH fuel.

Features:

- Throat heat flux estimation  
- Wall thickness approximation  
- Copper alloy liner (GRCop-84)  
- Structural jacket (Inconel/Stainless)  

Designed to maintain wall temperatures < 900 K.

---

# 📂 Repository Structure
## 📂 Repository Structure

```
├── docs/
│   ├── Mission & System Design
│   ├── Pressurization System Design
│   ├── Liquid Engine Design
│   ├── Combustion Analysis (CEA)
│   ├── Cooling System Design
│   └── Figures
│
├── pintle-injector-sizing/
│   ├── Analytical sizing scripts
│   ├── Parametric sweeps
│   ├── Monte Carlo uncertainty
│   └── Visualization tools
│
└── report/
    └── Full technical report (PDF)
```

# 🛠 Tools & Methods

- NASA CEA
- Python analytical modeling
- SolidWorks CAD
- Parametric sweeps & uncertainty analysis
- System-level trade studies

---

# 📈 Engineering Scope Covered

- Mass budgeting  
- ΔV derivation  
- Pressure-fed system design  
- Helium sizing  
- Injector fluid dynamics  
- Combustion thermodynamics  
- Nozzle expansion trade studies  
- Heat transfer modeling  
- Thermal structural considerations  

---

# 🎯 Design Philosophy

This engine architecture emphasizes:

- High reliability (no turbopumps)
- Moderate chamber pressure (20 bar)
- Analytical transparency
- Manufacturing feasibility
- Mission-appropriate scaling

---

# 👩‍🚀 Author

**Mounapriya Venkatesan**  
Graduate Student – Space Studies  
Rice University  

---

*This repository represents a system-level propulsion engineering design exercise integrating multidisciplinary aerospace principles.*
