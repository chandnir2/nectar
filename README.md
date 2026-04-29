# Nectar

A lightweight python package that analyzes weather station temperature data from Colorado Climate Center (https://climate.colostate.edu/data_access_new.html) and data from Project Feederwatch (https://feederwatch.org/) to compare estimated flowering day of year using growing degree days (GDD) and estimated hummingbird arrival day of year for four species of migratory hummingbirds in the Front Range of Colorado.

**!!!!note!!!!** we drive everything in the "nectar/config.py" file. Please adjust paths there to run this toolbox on new data. 

# Data - IMPORTANT CONFIGURATION

The raw FeederWatch dataset (~1.6 GB) is not included in this repository due to GitHub file size limits.
Users must download it separately from (https://feederwatch.org/explore/raw-dataset-requests/) and place it in a new folder named 'data' before running the scripts. The user can not download more than one subset of data from the website. If you wish to look at the entire dataset (1988-2024) please download raw data and concatenate before running script. 

File path: Nectar/data/raw_feederwatch_data*.csv

You may download sample weather station data for Boulder, Fort Collins, and Castle Rock from the GitHub Repo in folder: data/sample

If not using provided sample data:
Please download raw weather station data from (https://climate.colostate.edu/data_access_new.html). Select desired weather stations within Colorado for desired years (aligned with your target Feederwatch data), and place raw station data in a new folder titled station. Each file should represent a single station and contain daily temperature data.

File path: Nectar/data/station/raw_weather_station_data


```text
nectar/
├── nectar/
│   ├── functions/
│   ├── config.py
│   └── run.py
│
├── data/
│   ├── feederwatch_????_raw.csv <-- download from feederwatch please! 
|   ├── sample/sample_station_data.csv <-- testing data
│   └── station/
│
├── outputs/
└── pyproject.toml
```

> **Data source:**   
> Colorado Climate Center Station Data provided by Colorado State University
> 
> Project Feederwatch Data provided by Cornell Lab of Ornithology

# Problems and Motivation
Scientists are already witnessing the impacts of global temperature increase on wildlife populations. More specifically, on migratory wildlife populations, including species of hummingbirds. Migratory hummingbirds, including the broad-tailed hummingbird _(Selasphorus Platycercus)_, black-chinned hummingbird _(Archilochus alexandri)_, Rufous hummingbird _(Selasphorus rufus)_, and calliope hummingbird _(Stellula calliope)_ use the Rocky Mountain region between April through August, before returning to their wintering grounds. However, with increasing temperatures across this region, it is hypothesized that peak flowering is occurring earlier than historically recorded. In turn, hummingbirds arriving during typical migration periods miss peak flowering, and thus lack adequate food availability. For this project, I am focusing on a subset of the Mountain West Region and analyzing temporal mismatch occuring in the Front Range of Colorado: Boulder, Castle Rock, and Fort Collins. 

# Usage

Nectar is intended to be used for scientists and wildlife officials to determine temporal mismatch between hummingbird arrivalals and flowering bloom time. 

This package outputs:
- Daily and cumulative growing degree days (GDD) from 1988-2024
- Estimated flowering DOY of each year
- Estimated hummingbird arrival DOY from year
- Annual mismatch (in days)
- Mean mismatch across all years

Plotting outputs:
- Flowering timing
- Hummingbird arrival timing
- Temporal mismatch over time

## Installation

```bash
pip install -e .
```

Or from source:

```bash
git clone [(https://github.com/chandnir2/nectar.git)]
python -m pip install -e .
cd nectar
```

## Command Line 

```bash
run-nectar    # generates outputs/flowering_vs_arrival.png and data/mismatch.png & csv files
```

## Package files
- `__init__.py` - init file
- `config.py` - configuration script to ensure no hardcoded filepaths
- `run.py` - driver script; runs all functions

## Function files

- `cleaning.py` — read and clean raw Feederwatch data 
- `mismatch_analysis.py` — main functions
- `plotting.py` — plots temporal mismatch, flowering day of year, and hummingbird arrival day of year

## License

MIT
