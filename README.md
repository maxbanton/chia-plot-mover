# chia-plot-mover
Little tool to help to move plots across hard drives.
Assuming you are plotting to one (or multiple) drive and want to move plots to multiple destination drives.
Script is automatically looking for space across specified list of destinations to move plots on.

## Install
Python 3.7 or newer is required. Should be in place if you already using official chia client.
Tested on Ubuntu 20.04

Semi automated:
```bash
git clone https://github.com/maxbanton/chia-plot-mover.git
cd chia-plot-mover
sh install.sh
cp config-example.yaml config.yaml # Fill config.yaml with your values
```

Manual:
```bash
git clone https://github.com/maxbanton/chia-plot-mover.git
cd chia-plot-mover
python -m venv .venv
source .venv/bin/activate
pip install poetry
poetry install
cp config-example.yaml config.yaml # Fill config.yaml with your values
```

## Run
Tip: Since plotting is long running process, running plot mover in screen session would be preferable

```bash
sh start.sh
```

## Donate
You can send any amount of chia if you find this tool useful. Thanks!
```bash
xch122s5zr5y3d53q348dnx2htaktq5huqmme3xvsmsqgte2rqjcev4srzttyw
```
