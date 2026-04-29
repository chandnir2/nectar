import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from nectar.config import OUTPUT_DIR, PLOT_TIMING, PLOT_MISMATCH


# ............................................
# MAIN PLOTTING FUNCTION
# ............................................
def run_plots(results_df=None):
    """
    Generate phenology and mismatch plots from analysis results.

    This function creates two figures:
    1. Flowering vs hummingbird arrival timing over time
    2. Temporal mismatch (arrival - flowering) with trend line

    If no dataframe is provided, results are loaded from:
    OUTPUT_DIR/mismatch_results.csv

    Parameters
    ----------
    results_df : pd.DataFrame, optional
        Precomputed mismatch results. If None, the function loads
        saved results from folder

    Returns
    -------
    pd.DataFrame
        Cleaned mismatch dataset used for plotting, with NaN rows removed.

    Outputs
    -------
    Saves two figures:
    - PLOT_TIMING: flowering and arrival timing comparison
    - PLOT_MISMATCH: temporal mismatch over time
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




def plot_species_dist(data):
    '''
    Plots the distribution of cleaned feederwatch data by unique species type stored in
    'SPECIES_CODE'

    
    Inputs:
    ------------
    Accepts Pandas DataFrame input from clean_feederwatch or merge_clean_feederwatch.
    DataFrame must contain column 'SPECIES_CODE'


    Returns:
    ------------
    Plots Bar plot with code labels on the x axis and counts on the y axis

    Returns the species counts sorted by highest frequency as a Pandas DataFrame.
    
    '''

    plt.bar(data['SPECIES_CODE'].unique(), data['SPECIES_CODE'].value_counts(sort=False).values)
    # For each unique type of bird found using .unique(), plot how many data points in the data set consist of those birds
    # Works by looking at the unique species codes and then plotting the counts that align with those codes.
    # sort=False so that value_counts() does not reorder the Species Code by most frequent result

    plt.title('Bird Species Distribution')
    plt.xlabel('Species Code')
    plt.ylabel('Number of Species Measurements in Data')
    plt.show()

    return pd.DataFrame(data['SPECIES_CODE'].value_counts())




def plot_location_dist(data):
    '''
    Plots the distribution of cleaned feederwatch data by unique location type stored in
    'SUBNATIONAL1_CODE'

    
    Inputs:
    ------------
    Accepts Pandas DataFrame input from clean_feederwatch or merge_clean_feederwatch.
    DataFrame must contain column 'SUBNATIONAL1_CODE'

    
    Returns:
    ------------
    Plots Bar plot with code labels on the x axis and counts on the y axis

    Returns the location counts sorted by highest frequency as a Pandas DataFrame.
    
    '''
    
    plt.bar(data['SUBNATIONAL1_CODE'].unique(), data['SUBNATIONAL1_CODE'].value_counts(sort=False).values)
    
    plt.title('Bird Location Distribution')
    plt.xlabel('Subnational Location Code')
    plt.ylabel('Number of Location Measurements in Data')
    plt.show()

    return pd.DataFrame(data['SUBNATIONAL1_CODE'].value_counts())



# ............................................
# RUN DIRECTLY
# ............................................
if __name__ == "__main__":
    run_plots()