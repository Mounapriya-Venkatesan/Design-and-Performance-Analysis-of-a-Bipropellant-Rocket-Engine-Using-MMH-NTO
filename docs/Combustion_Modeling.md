# 🔥 Combustion Modeling and Thermochemical Analysis  
**MMH / N₂O₄ Pressure-Fed Lunar Descent Engine**

---

## 1. Introduction

Combustion modeling was performed to evaluate the thermochemical performance of the hypergolic propellant pair:

- **Fuel:** Monomethylhydrazine (MMH)  
- **Oxidizer:** Nitrogen Tetroxide (N₂O₄)

Tools used:

- NASA CEA (Chemical Equilibrium with Applications)
- Rocket Propulsion Analysis (RPA)

The objective was to determine:

- Chamber temperature
- Specific impulse (Isp)
- Characteristic velocity (C*)
- Exhaust velocity
- Species equilibrium
- Nozzle expansion performance

---

# 2. Governing Rocket Equations

---

## 2.1 Thrust Equation

For steady 1D flow:

$$
T = \dot{m} v_e + (P_e - P_a) A_e
$$

Where:

- $\dot{m}$ = mass flow rate  
- $v_e$ = exhaust velocity  
- $P_e$ = exit pressure  
- $P_a$ = ambient pressure  
- $A_e$ = exit area  

For vacuum:

$$
P_a \approx 0
$$

Thus:

$$
T_{vac} = \dot{m} v_e + P_e A_e
$$

---

## 2.2 Specific Impulse

Specific impulse is defined as:

$$
I_{sp} = \frac{T}{\dot{m} g_0}
$$

Rearranging:

$$
v_e = I_{sp} g_0
$$

For this engine:

$$
v_e = 315 \times 9.81 = 3090 \ \text{m/s}
$$

---

# 3. Characteristic Velocity (C*)

Characteristic velocity isolates combustion efficiency:

$$
C^* = \frac{P_c A_t}{\dot{m}}
$$

From choked flow theory:

$$
\dot{m} = P_c A_t
\sqrt{
\frac{\gamma}{R T_c}
}
\left(
\frac{2}{\gamma+1}
\right)^{\frac{\gamma+1}{2(\gamma-1)}}
$$

Rearranging gives:

$$
C^* =
\sqrt{
\frac{R T_c}{\gamma}
}
\left(
\frac{\gamma+1}{2}
\right)^{\frac{\gamma+1}{2(\gamma-1)}}
$$

From CEA results:

$$
C^* \approx 1600 \ \text{m/s}
$$

---

# 4. Exhaust Velocity Derivation

For isentropic nozzle expansion:

$$
v_e =
\sqrt{
\frac{2 \gamma}{\gamma - 1}
R T_c
\left[
1 - \left( \frac{P_e}{P_c} \right)^{\frac{\gamma-1}{\gamma}}
\right]
}
$$

For ideal vacuum expansion:

$$
\frac{P_e}{P_c} \rightarrow 0
$$

Thus:

$$
v_{e,max} =
\sqrt{
\frac{2 \gamma}{\gamma - 1}
R T_c
}
$$

RPA predicted:

$$
v_e \approx 3110 \ \text{m/s}
$$

which corresponds to:

$$
I_{sp} \approx 315 \ \text{s}
$$

---

# 5. Mixture Ratio Formulation

Mixture ratio:

$$
O/F = \frac{\dot{m}_{ox}}{\dot{m}_{fuel}}
$$

Total mass flow:

$$
\dot{m}_{total} = \dot{m}_{ox} + \dot{m}_{fuel}
$$

Fuel and oxidizer mass flow split:

$$
\dot{m}_{ox} =
\dot{m}_{total}
\frac{O/F}{1 + O/F}
$$

$$
\dot{m}_{fuel} =
\frac{\dot{m}_{total}}{1 + O/F}
$$

---

# 6. CEA Performance Trends

---

## 📈 Figure 1 – Isp vs Mixture Ratio

![Isp vs O/F](docs/figures/isp_vs_of.png)

- Peak Isp near O/F ≈ 2.1–2.2  
- Selected O/F = 2.16  
- Operation near thermodynamic optimum  

---

## 📈 Figure 2 – C* vs Chamber Pressure

![Cstar vs Pc](docs/figures/cstar_vs_pc.png)

- C* increases slightly with chamber pressure  
- Weak pressure dependence  
- Supports Pc ≈ 20 bar selection  

---

## 📈 Figure 3 – Chamber Temperature vs O/F

![Tc vs O/F](docs/figures/tc_vs_of.png)

- Tc peaks near optimal mixture ratio  
- Tc ≈ 3130–3260 K  
- High thermal load at throat  

---

# 7. Gas Properties from CEA/RPA

From equilibrium analysis:

- Molecular Weight:

$$
M \approx 23 \ \text{g/mol}
$$

- Gas Constant:

$$
R = \frac{R_u}{M}
$$

$$
R = \frac{8.314}{0.023}
= 361 \ \text{J/kg·K}
$$

- Specific Heat Ratio:

$$
\gamma \approx 1.16
$$

---

# 8. Heat Flux Estimation

Estimated throat heat flux:

$$
q'' = 0.5 P_c v_e
$$

Substituting:

$$
q'' \approx 1.4 \times 10^6 \ \text{W/m}^2
$$

This necessitates regenerative cooling.

---

# 9. Validation Against Literature

| Parameter | This Design | Apollo LMDE |
|------------|-------------|-------------|
| Isp (vac) | 315 s | 311 s |
| Pc | 20 bar | 10 bar |
| Propellants | MMH/N₂O₄ | Aerozine/N₂O₄ |

Performance aligns with flight-proven lunar descent engines.

---

# 10. Conclusion

Thermochemical modeling confirms:

- Stable hypergolic combustion  
- Isp ≈ 315 s achievable  
- C* ≈ 1600 m/s  
- Tc > 3000 K  
- Suitable for lunar descent missions  

The combustion analysis validates both propulsion performance and cooling system requirements.
