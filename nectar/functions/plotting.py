import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from nectar.config import OUTPUT_DIR, PLOT_TIMING, PLOT_MISMATCH


# ............................................
# MAIN PLOTTING FUNCTION
# ............................................
def run_plots(results_df=None):
    """
    If results_df is None:
        loads mismatch_results.csv from OUTPUT_DIR
    Otherwise:
        uses passed-in dataframe (pipeline mode)
    """

    # ----------------------------------------
    # LOAD DATA IF NOT PROVIDED
    # ----------------------------------------
    if results_df is None:
        results_df = pd.read_csv(
            OUTPUT_DIR / "mismatch_results.csv",
            index_col=0
        )

    results_df = results_df.dropna()

    years = results_df.index if results_df.index.name == "Year" else range(len(results_df))

    # ----------------------------------------
    # FIGURE 1: TIMING COMPARISON
    # ----------------------------------------
    plt.figure(figsize=(10, 6))

    plt.plot(years, results_df["flowering_doy"],
             marker="o", label="Flowering (GDD)", color="#d33682")

    plt.plot(years, results_df["arrival_doy"],
             marker="s", label="Hummingbird arrival", color="#2aa198")

    plt.title("Phenological Timing Over Time")
    plt.xlabel("Year")
    plt.ylabel("Day of Year")
    plt.legend()
    plt.grid(alpha=0.3)

    plt.tight_layout()

    plt.savefig(PLOT_TIMING, dpi=300)
    plt.close()

    # ----------------------------------------
    # FIGURE 2: MISMATCH OVER TIME
    # ----------------------------------------
    plt.figure(figsize=(10, 6))

    plt.plot(years, results_df["mismatch_days"],
             marker="o", color="crimson", label="Mismatch (Arrival - Flowering)")

    plt.axhline(0, linestyle="--", color="black")

    # trend line
    z = np.polyfit(range(len(results_df)), results_df["mismatch_days"], 1)
    p = np.poly1d(z)

    plt.plot(years, p(range(len(results_df))),
             linestyle="--", color="gray", label="Trend")

    plt.title("Phenological Mismatch Over Time")
    plt.xlabel("Year")
    plt.ylabel("Days")
    plt.legend()
    plt.grid(alpha=0.3)

    plt.tight_layout()

    plt.savefig(PLOT_MISMATCH, dpi=300)
    plt.close()

    print(f"Plots saved to: {OUTPUT_DIR}")

    return results_df


# ............................................
# RUN DIRECTLY
# ............................................
if __name__ == "__main__":
    run_plots()