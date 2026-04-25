# Nectar

A lightweight python package that analyzes weather station temperature data from Colorado Climate Center (https://climate.colostate.edu/data_access_new.html) and data from Project Feederwatch (https://feederwatch.org/) to compare estimated flowering day of year and estimated hummingbird arrival day of year for four species of migratory hummingbirds in Colorado.  

# DATA
The raw FeederWatch dataset (~1.6 GB) is not included in this repository due to GitHub file size limits.
Users must download it separately from (https://feederwatch.org/explore/raw-dataset-requests/) and place it in the data/ directory before running the scripts.

> **Data source:**   
> Colorado Climate Center Station Data provided by Colorado State University
> 
> Project Feederwatch Data provided by Cornell Lab of Ornithology

# Problems and Motivation
Scientists are already witnessing the impacts of global temperature increase on wildlife populations. More specifically, on migratory wildlife populations, including species of hummingbirds. Migratory hummingbirds, including the broad-tailed hummingbird _(Selasphorus Platycercus)_, black-chinned hummingbird _(Archilochus alexandri)_, Rufous hummingbird _(Selasphorus rufus)_, and calliope hummingbird _(Stellula calliope)_ use the Rocky Mountain region between April through August, before returning to their wintering grounds. However, with increasing temperatures across this region, it is hypothesized that peak flowering is occurring earlier than historically recorded. In turn, hummingbirds arriving during typical migration periods miss peak flowering, and thus lack adequate food availability. For this project, I am focusing on a subset of the Mountain West Region and analyzing temporal mismatch occuring in the Front Range of Colorado: Boulder, Castle Rock, and Fort Collins. 

# Usage

Nectar is intended to be used for scientists and wildlife officials to determine temporal mismatch between hummingbird arrivalals and flowering bloom time. This package outputs a dataframe with an average estimated hummingbird arrival day of year (DOY), an estimated flowering DOY for all of the existing data years provided, the number of days of temporal mismatch, and the mean temporal mismatch over all of the years analyzed. Additionally, the plotting functionality provides a visual representation of how migration and estimated bloom evolve over time. This analysis can be used to help better understand trends over time. 

## Installation - this does not work yet

```bash
pip install -e .
```

Or from source:

```bash
git clone [(https://github.com/chandnir2/atoc4815_nectar.git)]
cd nectar
pip install -e .
```

## Quick Start -- this does not work yet

```python
from lorenz_project import Lorenz63

model = Lorenz63(sigma=10, rho=28, beta=8/3)
trajectory = model.run([1, 1, 1], dt=0.01, n_steps=5000)
```

## Command Line - this does not work yet

```bash
run-nectar    # generates data/flowering_vs_arrival.png and data/mismatch.png
```

## Files

- `clean_my_data.py` — Lorenz63 model class
- `mismatch_analysis.py` — Forward Euler integrator
- `plotting.py` — Ensemble visualization
- `run_nectar.py` — Driver script

## License

MIT
