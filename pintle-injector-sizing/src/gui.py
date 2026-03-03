import tkinter as tk
from tkinter import ttk, messagebox
from injector_sizing import InjectorInputs, size_pintle_injector

DEFAULTS = {
    "thrust": 30000,
    "isp": 315,
    "of": 2.16,
    "pc_bar": 20,
    "dp_frac": 0.15,
    "rho_fuel": 880,
    "rho_ox": 1440,
    "cd_fuel": 0.9,
    "cd_ox": 0.9,
}

def run_calc(entries, output_label):
    try:
        vals = {k: float(e.get()) for k, e in entries.items()}
        inp = InjectorInputs(
            thrust_N=vals["thrust"], isp_s=vals["isp"], of_ratio=vals["of"],
            chamber_pressure_bar=vals["pc_bar"], dp_fraction=vals["dp_frac"],
            rho_fuel_kg_m3=vals["rho_fuel"], rho_ox_kg_m3=vals["rho_ox"],
            cd_fuel=vals["cd_fuel"], cd_ox=vals["cd_ox"]
        )
        r = size_pintle_injector(inp)
        msg = (
            f"Pintle d: {r.pintle_diameter_m*1000:.2f} mm\n"
            f"Outer d : {r.outer_diameter_m*1000:.2f} mm\n"
            f"Gap     : {r.annular_gap_width_m*1000:.2f} mm\n"
            f"mdot    : {r.mdot_total_kg_s:.3f} kg/s\n"
            f"ΔP      : {r.dp_Pa/1e5:.2f} bar"
        )
        output_label.config(text=msg)
    except Exception as ex:
        messagebox.showerror("Error", str(ex))

def main():
    root = tk.Tk()
    root.title("Pintle Injector Sizing Tool")

    frame = ttk.Frame(root, padding=12)
    frame.grid()

    entries = {}
    row = 0
    for key, val in DEFAULTS.items():
        ttk.Label(frame, text=key).grid(column=0, row=row, sticky="w")
        e = ttk.Entry(frame, width=16)
        e.insert(0, str(val))
        e.grid(column=1, row=row, padx=8, pady=2)
        entries[key] = e
        row += 1

    out = ttk.Label(frame, text="", justify="left")
    out.grid(column=0, row=row, columnspan=2, pady=10, sticky="w")

    ttk.Button(frame, text="Compute", command=lambda: run_calc(entries, out)).grid(column=0, row=row+1, columnspan=2)
    root.mainloop()

if __name__ == "__main__":
    main()