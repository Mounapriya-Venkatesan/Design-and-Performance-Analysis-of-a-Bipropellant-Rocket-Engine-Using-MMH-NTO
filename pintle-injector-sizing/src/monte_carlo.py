import random
import statistics
from injector_sizing import InjectorInputs, size_pintle_injector

def percentile(data, p):
    s = sorted(data)
    k = (len(s)-1) * (p/100)
    f = int(k)
    c = min(f+1, len(s)-1)
    if f == c:
        return s[f]
    return s[f] + (k - f) * (s[c] - s[f])

def monte_carlo(n=2000, seed=7):
    random.seed(seed)

    pintle = []
    outer = []
    gap = []

    for _ in range(n):
        # Example uncertainties (edit as you like)
        thrust = random.gauss(30000, 300)          # ±1% approx
        isp = random.gauss(315, 3)                 # ±1%
        of = random.gauss(2.16, 0.05)
        pc = random.gauss(20, 1.0)                 # ±5%
        dp_frac = random.gauss(0.15, 0.01)
        rho_fuel = random.gauss(880, 10)
        rho_ox = random.gauss(1440, 15)
        cd_fuel = random.gauss(0.90, 0.03)
        cd_ox = random.gauss(0.90, 0.03)

        # keep within physical bounds
        dp_frac = min(max(dp_frac, 0.05), 0.30)
        cd_fuel = min(max(cd_fuel, 0.6), 1.0)
        cd_ox = min(max(cd_ox, 0.6), 1.0)
        pc = max(pc, 1.0)

        inp = InjectorInputs(
            thrust_N=thrust, isp_s=isp, of_ratio=of,
            chamber_pressure_bar=pc, dp_fraction=dp_frac,
            rho_fuel_kg_m3=rho_fuel, rho_ox_kg_m3=rho_ox,
            cd_fuel=cd_fuel, cd_ox=cd_ox
        )
        r = size_pintle_injector(inp)
        pintle.append(r.pintle_diameter_m * 1000)
        outer.append(r.outer_diameter_m * 1000)
        gap.append(r.annular_gap_width_m * 1000)

    def summary(x):
        return {
            "mean": statistics.mean(x),
            "std": statistics.pstdev(x),
            "p5": percentile(x, 5),
            "p50": percentile(x, 50),
            "p95": percentile(x, 95),
        }

    print("\n=== Monte Carlo Results (mm) ===")
    print("Pintle d:", summary(pintle))
    print("Outer d :", summary(outer))
    print("Gap     :", summary(gap))

if __name__ == "__main__":
    monte_carlo()