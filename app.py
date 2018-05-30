# -*- coding: utf-8 -*-
"""
run script for pygeopressure-well

Created on Sun Jan 21 2018
"""
from __future__ import (division, absolute_import, print_function,
                        with_statement, unicode_literals)
from builtins import str, open

import sys
import getopt
import json

from pathlib2 import Path

from well_pygeopressure.config import CONF

# import pyGeoPressure Core code
def parse_args(argv):
    #-------------------------------------
    # set pyGeoPressure core code path
    core_path = "D:\\HUB\\Python\\PorePressurePrediction"
    try:
        opts, args = getopt.getopt(argv, "hp:", ["path="])
    except getopt.GetoptError:
        print('app.py -p <path to pyGeoPressure core>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('app.py -p <path to pyGeoPressure core>')
            sys.exit()
        elif opt in ("-p", "--corepath"):
            core_path = arg
            print("pyGeoPressure core path：'{}'".format(core_path))
    if core_path not in sys.path:
        sys.path.append(core_path)


def load_setting():
    current_file_path = Path(__file__)
    setting_file_path = Path(Path(current_file_path.parents[0]), "setting")
    # config.CONF.from_json(setting_file_path)
    CONF.from_json(setting_file_path)
    CONF.setting_abs_path = str(setting_file_path)

def main():
    parse_args(sys.argv[1:])
    load_setting()
    # start application
    from well_pygeopressure.main_window import start
    start()

if __name__ == '__main__':
    main()
