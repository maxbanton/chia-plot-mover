import os
import shutil
import time
from typing import Dict

import yaml

CONFIG_FILE_NAME = 'config.yaml'
SLEEP_PERIOD = 600
MIN_K32_PLOT_SIZE = 108800000000


class PlotMover:
    _config: Dict

    def __init__(self):
        self._config = self._read_config()

    @staticmethod
    def _read_config():
        current_dir = os.path.dirname(__file__)

        config_path = os.path.join(current_dir, '..', CONFIG_FILE_NAME)
        filename = os.path.abspath(os.path.realpath(config_path))

        with open(filename, 'r') as stream:
            try:
                return yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)

    def _look_for_plot(self):
        for dir_ in self._config.get('source'):
            for file in os.listdir(dir_):
                if file.endswith(".plot"):
                    return dir_, file

        return None, None

    def _look_for_space(self, needed_space):
        for dir_ in self._config.get('dest'):
            _, _, free = shutil.disk_usage(dir_)
            if free > needed_space:
                return dir_

    def main(self):
        while True:
            source_dir, plot_file = self._look_for_plot()

            if plot_file:
                plot_path = os.path.join(source_dir, plot_file)
                size = os.path.getsize(plot_path)

                if size < MIN_K32_PLOT_SIZE:
                    raise Exception(f'Plot file {plot_path} size is to small. Is it real plot?')

                dest_dir = self._look_for_space(size)

                if dest_dir:
                    dest_path = os.path.join(dest_dir, plot_file)

                    if os.path.isfile(dest_path):
                        raise Exception(f'Plot file {dest_path} already exists. Duplicate?')

                    shutil.move(plot_path, dest_path)
                    print(f'Plot moved from {plot_path} to {dest_path}')
                else:
                    raise Exception(f'No space can be found for plot {plot_path} of size {size}')
            else:
                print(f'No plots found. Sleep for {SLEEP_PERIOD}s')
                time.sleep(SLEEP_PERIOD)
