from pathlib import Path

# ................................
# BASE DIRECTORY (PROJECT ROOT)
# ................................
BASE_DIR = Path(__file__).resolve().parent

# ................................
# DATA
# ................................
feederwatch_files = sorted((BASE_DIR / "data").glob("feederwatch_*_raw.csv"))

if not feederwatch_files:
    raise FileNotFoundError("No feederwatch_*_raw.csv file found in data/")

FEEDERWATCH_RAW = feederwatch_files[-1]
print("Using feederwatch file:", FEEDERWATCH_RAW)

STATION_DIR = BASE_DIR / "data" / "sample" #adjust this for new station data

# ................................
# OUTPUTS
# ................................
OUTPUT_DIR = BASE_DIR / "outputs"

FEEDERWATCH_CLEAN = OUTPUT_DIR / "clean_feederwatch.csv"
FLOWERING_FILE = OUTPUT_DIR / "flowering_times.csv"
MISMATCH_FILE = OUTPUT_DIR / "mismatch_results.csv"

PLOT_TIMING = OUTPUT_DIR / "phenology_timing.png"
PLOT_MISMATCH = OUTPUT_DIR / "mismatch_trend.png"

# ................................
# MODEL PARAMETERS
# ................................
BASE_TEMP_F = 40
FLOWERING_GDD = 100

print("configuration complete:", BASE_DIR)
