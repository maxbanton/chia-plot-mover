[![Stand With Ukraine](https://raw.githubusercontent.com/vshymanskyy/StandWithUkraine/main/banner2-direct.svg)](https://vshymanskyy.github.io/StandWithUkraine)

# Chia Plot Mover
Little tool to help to move plots across hard drives.
Assuming you are plotting to one (or multiple) drive and want to move plots to multiple destination drives.
Script is automatically look for space across specified list of destinations to move plots on.
Can work with multiple plots at the same time, it will be helpful if speed of creating plots is higher then speed of moving plots to the destinaton
directories.

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
