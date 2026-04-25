from pathlib import Path

# ................................
# BASE DIRECTORY (PROJECT ROOT)
# ................................
BASE_DIR = Path(__file__).resolve().parent

# ................................
# DATA
# ................................
FEEDERWATCH_RAW = BASE_DIR / "data" / "feederwatch_2021-2024_raw.csv"
STATION_DIR = BASE_DIR / "data" / "station"

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