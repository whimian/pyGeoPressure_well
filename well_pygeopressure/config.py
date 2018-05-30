# -*- coding: utf-8 -*-
from __future__ import unicode_literals

__author__ = "Yu Hao"

import os
import json
from builtins import str
from pathlib2 import Path


class Configuration(object):
    def __init__(self):
        # self.json_file = json_file
        self.data_root = None
        self.current_survey = None
        self.setting_abs_path = None

    def from_json(self, json_file):
        with open(str(json_file), "r") as fl:
            self.json_dict = json.load(fl)
        self.data_root = self.json_dict["data_root"]
        self.current_survey = self.json_dict["current_survey"]

    def to_json(self, json_file):
        dict_to_dump = {}
        dict_to_dump["data_root"] = self.data_root
        dict_to_dump["current_survey"] = self.current_survey
        with open(str(json_file), "w") as fl:
            json.dump(dict_to_dump, fl, indent=4)

    @property
    def survey_dir(self):
        return Path(self.data_root) / self.current_survey

    @property
    def seismic_dir(self):
        return Path(self.data_root) / self.current_survey / 'Seismics'

    @property
    def well_dir(self):
        return Path(self.data_root) / self.current_survey / 'Wellinfo'

    @property
    def surface_dir(self):
        return Path(self.data_root) / self.current_survey / 'Surfaces'

CONF = Configuration()
