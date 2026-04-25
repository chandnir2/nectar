import pandas as pd
import numpy as np

from nectar.config import (
    STATION_DIR,
    OUTPUT_DIR,
    BASE_TEMP_F,
    FLOWERING_GDD
)

from nectar.functions.cleaning import clean_feederwatch


# ..................................................
# LOAD WEATHER STATION DATA FOR BOULDER, FORT COLLINS, AND CASLTE ROCK
# ..................................................
def load_station_data(filepath):

    with open(filepath) as f:
        station_name = f.readline().strip().split(",")[0]

    df = pd.read_csv(
        filepath,
        skiprows=1,
        header=None,
        names=["date", "tmax", "tmin"]
    )

    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df = df.replace("M", np.nan)

    df["tmax"] = pd.to_numeric(df["tmax"], errors="coerce")
    df["tmin"] = pd.to_numeric(df["tmin"], errors="coerce")

    df = df.dropna(subset=["tmax", "tmin"]).copy()

    df["tmean"] = (df["tmax"] + df["tmin"]) / 2
    df["station"] = station_name

    return df[["date", "tmean", "station"]]


# ..................................................
# FLOWERING DAY OF YEAR
# ..................................................
def compute_flowering_doy(df_year):

    df_year = df_year.sort_values("date").copy()

    df_year["gdd"] = (df_year["tmean"] - BASE_TEMP_F).clip(lower=0) # can not be negative value
    df_year["gdd_cumul"] = df_year["gdd"].cumsum()

    crossed = df_year[df_year["gdd_cumul"] >= FLOWERING_GDD]

    if crossed.empty:
        return None

    return int(crossed.iloc[0]["date"].dayofyear)


# .....................................................................
# CALCULATE TEMPORAL MISMATCH BETWEEN FLOWERING AND HUMMINGBIRD ARRIVAL
# .....................................................................
def run_mismatch_analysis(fw_df=None, save=True):

    if fw_df is None:
        fw_df = clean_feederwatch()

    # load stations
    dfs = [load_station_data(f) for f in STATION_DIR.glob("*.csv")]

    if not dfs:
        raise RuntimeError("No station files found")

    combined = pd.concat(dfs)

    daily = (
        combined
        .groupby("date")["tmean"]
        .mean()
        .reset_index()
        .sort_values("date")
    )

    daily["year"] = daily["date"].dt.year

    flowering = {
        yr: compute_flowering_doy(group)
        for yr, group in daily.groupby("year")
    }

    flowering_ts = pd.Series(flowering, name="flowering_doy")
    flowering_ts.index.name = "Year"

    arrival_doy = (
        fw_df.groupby("Year")["DOY"]
        .quantile(0.05) # Using 5% quantile for observational data to determine when actual arrival occurs, vs minimum value which is not biologically accurate
        .sort_index()
    )

    common = flowering_ts.index.intersection(arrival_doy.index)

    if len(common) == 0:
        raise RuntimeError("No overlapping years")

    mismatch = arrival_doy.loc[common] - flowering_ts.loc[common]

    results = pd.DataFrame({
        "arrival_doy": arrival_doy.loc[common],
        "flowering_doy": flowering_ts.loc[common],
        "mismatch_days": mismatch
    })

    if save:
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

        flowering_ts.to_frame().to_csv(
            OUTPUT_DIR / "flowering_times.csv"
        )

        results.to_csv(
            OUTPUT_DIR / "mismatch_results.csv"
        )

    print(results)
    print(f"\nMean mismatch: {mismatch.mean():.2f}")

    return results


if __name__ == "__main__":
    run_mismatch_analysis()