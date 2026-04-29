from nectar.config import FEEDERWATCH_RAW, OUTPUT_DIR
import pandas as pd
import numpy as np
from pathlib import Path


def clean_feederwatch(input_csv=None, output_csv=None):

    """
    Clean and filter Project FeederWatch hummingbird observation data.

    This function:
    - Loads raw FeederWatch CSV data
    - Filters for selected hummingbird species, U.S. mountain states,
      and spring months (Feb–Apr)
    - Creates a datetime column and day-of-year (DOY)
    - Saves cleaned dataset to folder within project

    Parameters
    ----------
    input_csv : str or Path, optional
        Path to raw FeederWatch dataset. If None, uses FEEDERWATCH_RAW
        from config.

    output_csv : str or Path, optional
        Path to save cleaned dataset. If None, defaults to
        OUTPUT_DIR/clean_feederwatch.csv

        If  output_csv = 'NoSave', the clean_feederwatch function will return the dataframe
        without saving to a csv file.

    Returns
    -------
    pd.DataFrame
        Cleaned FeederWatch dataset containing:
        - LATITUDE
        - LONGITUDE
        - SUBNATIONAL1_CODE
        - Month, Day, Year
        - SPECIES_CODE
        - DATE
        - DOY
    """

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
    if output_csv != 'NoSave':
        fw.to_csv(output_csv, index=False)

        print(f"Saved cleaned data to: {output_csv}")

    return fw



def merge_clean_feederwatch(input_csv_files, output_csv):
    '''
    This function is designed to clean multiple RAW Feederwatch data csv files at the same time.
    Calls clean_feederwatch for each csv without saving, then combines the csv
    files together before saving them as an output csv with all data combined.
    

    Inputs:
    ----------
    input_csv_files :
        Accepts a list of paths / str to csv files for RAW feederwatch data.

    
    outputcsv :
        Path to save clean dataset of datasets merged together.
        
        If outputcsv = 'NoSave', the dataframe will be returned but will not save to a csv


    Returns:
    ----------
    pd.DataFrame
        Cleaned FeederWatch dataset containing:
        - LATITUDE
        - LONGITUDE
        - SUBNATIONAL1_CODE
        - Month, Day, Year
        - SPECIES_CODE
        - DATE
        - DOY

    '''
    dataframe_list = []

    for file in input_csv_files:
        df = clean_feederwatch(file, output_csv='NoSave') # Sets df to pd.Dataframe return for clean_feederwatch. Doesn't save
        dataframe_list.append(df) # Appends to list of cleaned data csv


    # Combine all of the csv files in input_csv_files
    merged_df = pd.concat(dataframe_list, axis=0, ignore_index=False)
    # Same column names, so stack on axis=0
    # ignore_index False because column names are important for Feederwatch cleaning



    # Ensure save path exists
    Path(output_csv).parent.mkdir(parents=True, exist_ok=True)


    # Save cleaned data
    if output_csv != 'NoSave':
        merged_df.to_csv(output_csv, index=False)

        print(f"Saved cleaned data to: {output_csv}")

    
    # Return the merged dataframe
    return merged_df




# -------------------------
# CLI ENTRY POINT
# -------------------------
def main():
    print("RUNNING CLEANING PIPELINE")
    clean_feederwatch()


if __name__ == "__main__":
    main()