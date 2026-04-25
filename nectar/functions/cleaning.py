from nectar.config import FEEDERWATCH_RAW, OUTPUT_DIR
import pandas as pd
import numpy as np
from pathlib import Path


def clean_feederwatch(input_csv=None, output_csv=None):

    # -------------------------
    # DEFAULT PATHS FROM CONFIG
    # -------------------------
    if input_csv is None:
        input_csv = FEEDERWATCH_RAW

    if output_csv is None:
        output_csv = OUTPUT_DIR / "clean_feederwatch.csv"

    print(f"Loading: {input_csv}")

    # -------------------------
    # READ RAW DATA
    # -------------------------
    df = pd.read_csv(input_csv)

    # -------------------------
    # FILTER DATA
    # -------------------------
    species_list = ['calhum', 'brthum', 'bkchum', 'rufhum']
    states_list = ['US-AZ', 'US-CO', 'US-ID', 'US-MT', 'US-NV', 'US-NM', 'US-UT', 'US-WY']
    obs_months = [2, 3, 4]

    fw = df.loc[
        (df['SPECIES_CODE'].isin(species_list)) &
        (df['SUBNATIONAL1_CODE'].isin(states_list)) &
        (df['Month'].isin(obs_months)),
        ['LATITUDE', 'LONGITUDE', 'SUBNATIONAL1_CODE',
         'Month', 'Day', 'Year', 'SPECIES_CODE']
    ].copy()

    # -------------------------
    # CREATE DATE + DOY
    # -------------------------
    fw['DATE'] = pd.to_datetime(fw[['Year', 'Month', 'Day']])
    fw['DOY'] = fw['DATE'].dt.dayofyear

    # -------------------------
    # ENSURE OUTPUT DIR EXISTS
    # -------------------------
    Path(output_csv).parent.mkdir(parents=True, exist_ok=True)

    # -------------------------
    # SAVE CLEAN DATA
    # -------------------------
    fw.to_csv(output_csv, index=False)

    print(f"Saved cleaned data to: {output_csv}")

    return fw


# -------------------------
# CLI ENTRY POINT
# -------------------------
def main():
    print("RUNNING CLEANING PIPELINE")
    clean_feederwatch()


if __name__ == "__main__":
    main()