# -*- coding: utf-8 -*-
"""
Utility functions

Created on Thu Jan 11 2018
"""
from __future__ import (division, absolute_import, print_function,
                        with_statement, unicode_literals)
from future.builtins import int

__author__ = "Yu Hao"

import json
from copy import deepcopy
from shutil import copyfile

from pathlib2 import Path

import pygeopressure as ppp

# -----------------------------------------------------------------------------
# Exceptions
# -----------------------------------------------------------------------------

class DuplicateSurveyNameExeption(Exception):
    def __init__(self):
        self.message = ""
        super(DuplicateSurveyNameExeption, self).__init__(self.message)

# -----------------------------------------------------------------------------
# Classes
# -----------------------------------------------------------------------------

class Seismic(object):
    def __init__(self, name, conf):
        self.name = name
        self.conf = conf
        self.file_path = Path(conf.data_root) / conf.current_survey / \
            'Seismics' / '.{}'.format(name)
        self.inDepth = None
        self.path = None
        self.Property_Type = None
        self.inline_range = None
        self.crline_range = None
        self.z_range = None
        if self.file_path.exists():
            self.from_file()

    @property
    def info_dict(self):
        info_dict = dict()
        info_dict['inDepth'] = self.inDepth
        info_dict['path'] = self.path
        info_dict['Property_Type'] = self.Property_Type
        info_dict['inline_range'] = self.inline_range
        info_dict['crline_range'] = self.crline_range
        info_dict['z_range'] = self.z_range
        return info_dict

    def from_file(self):
        try:
            with open(str(self.file_path), 'r') as fl:
                info_dict = json.load(fl)
                self.inDepth = info_dict['inDepth']
                self.path = info_dict['path']
                self.Property_Type = info_dict['Property_Type']
                self.inline_range = info_dict['inline_range']
                self.crline_range = info_dict['crline_range']
                self.z_range = info_dict['z_range']
        except KeyError:
            print('missing information')

    def from_dict(self, info_dict):
        self.inDepth = info_dict['inDepth']
        self.path = info_dict['path']
        self.Property_Type = info_dict['Property_Type']
        self.inline_range = info_dict['inline_range']
        self.crline_range = info_dict['crline_range']
        self.z_range = info_dict['z_range']

    def to_json_file(self, output_file_name):
        output_file_path = Path(self.conf.data_root) / self.conf.current_survey / \
            'Seismics' / '.{}'.format(output_file_name)
        with open(str(output_file_path), 'w') as fl:
            json.dump(self.info_dict, fl, indent=4)

# =============================================================================
def read_survey_setting(json_file, parent_window):
    "read survey settings into import window widgets"
    threepoint = ppp.ThreePoints(json_file)
    parent_window.a_inline_text.setText(str(threepoint.inline_A))
    parent_window.a_crline_text.setText(str(threepoint.crline_A))
    parent_window.b_inline_text.setText(str(threepoint.inline_B))
    parent_window.b_crline_text.setText(str(threepoint.crline_B))
    parent_window.c_inline_text.setText(str(threepoint.inline_C))
    parent_window.c_crline_text.setText(str(threepoint.crline_C))
    parent_window.a_x_text.setText(str(threepoint.east_A))
    parent_window.a_y_text.setText(str(threepoint.north_A))
    parent_window.b_x_text.setText(str(threepoint.east_B))
    parent_window.b_y_text.setText(str(threepoint.north_B))
    parent_window.c_x_text.setText(str(threepoint.east_C))
    parent_window.c_y_text.setText(str(threepoint.north_C))

    parent_window.inline_0_spinBox.setValue(int(threepoint.startInline))
    parent_window.inline_1_spinBox.setValue(int(threepoint.endInline))
    parent_window.inline_step_spinBox.setValue(int(threepoint.stepInline))

    parent_window.crline_0_spinBox.setValue(int(threepoint.startCrline))
    parent_window.crline_1_spinBox.setValue(int(threepoint.endCrline))
    parent_window.crline_step_spinBox.setValue(int(threepoint.stepCrline))

    parent_window.z_0_spinBox.setValue(int(threepoint.startDepth))
    parent_window.z_1_spinBox.setValue(int(threepoint.endDepth))
    parent_window.z_step_spinBox.setValue(int(threepoint.stepDepth))

def discern_setting_from_gui(parent_window):
    "read survey settings from window widgets as a dict"
    dict_survey = dict()
    dict_survey['name'] = parent_window.surveyNameLineEdit.text()
    dict_survey["point_A"] = [
        int(parent_window.a_inline_text.text()),
        int(parent_window.a_crline_text.text()),
        float(parent_window.a_x_text.text()),
        float(parent_window.a_y_text.text())]
    dict_survey["point_B"] = [
        int(parent_window.b_inline_text.text()),
        int(parent_window.b_crline_text.text()),
        float(parent_window.b_x_text.text()),
        float(parent_window.b_y_text.text())]
    dict_survey["point_C"] = [
        int(parent_window.c_inline_text.text()),
        int(parent_window.c_crline_text.text()),
        float(parent_window.c_x_text.text()),
        float(parent_window.c_y_text.text())]
    dict_survey["inline_range"] = [
        parent_window.inline_0_spinBox.value(),
        parent_window.inline_1_spinBox.value(),
        parent_window.inline_step_spinBox.value()
    ],
    dict_survey["crline_range"] = [
        parent_window.crline_0_spinBox.value(),
        parent_window.crline_1_spinBox.value(),
        parent_window.crline_step_spinBox.value()
    ],
    dict_survey["z_range"] = [
        parent_window.z_0_spinBox.value(),
        parent_window.z_1_spinBox.value(),
        parent_window.z_step_spinBox.value(),
        parent_window.unitComboBox.currentText()
    ]
    # it's a bug of pyqt4
    if isinstance(dict_survey['inline_range'], tuple):
        dict_survey['inline_range'] = dict_survey['inline_range'][0]
        dict_survey['crline_range'] = dict_survey['crline_range'][0]
        # dict_survey['z_range'] = dict_survey['z_range'][0]
    return dict_survey

def create_survey_directory(root_dir, survey_name):
    """
    Create survey folder structure

    Parameters
    ----------
    root_dir : Path
        Root directory for storing surveys
    survey_nam : str
    """
    survey_root = root_dir / survey_name
    try:
        survey_root.mkdir()
        dir_to_create = [root_dir / survey_name / 'Seismics',
                         root_dir / survey_name / 'Wellinfo',
                         root_dir / survey_name / 'Surfaces']
        for directory in dir_to_create:
            directory.mkdir()
        # new folder structure does not require folder dot file
        #     file_path = directory / ".{}".format(str(directory.name).lower())
        #     file_path.touch()
        return survey_root
    except WindowsError:
        raise DuplicateSurveyNameExeption()

def write_survey_file(path_file, survey_dict):
    file_to_write = path_file
    with open(str(file_to_write), "w") as fl:
        json.dump(survey_dict, fl, indent=4)

def create_survey_info_file(survey_root, parent_window):
    """"""
    survey_dict = {
        "name": "F3",
        "inline_range": [int(parent_window.inline_0_spinBox.value),
                         int(parent_window.inline_1_spinBox.value),
                         int(parent_window.inline_step_spinBox.value)],
        "crline_range": [int(parent_window.crline_0_spinBox.value),
                         int(parent_window.crline_1_spinBox.value),
                         int(parent_window.crline_step_spinBox.value)],
        "z_range": [int(parent_window.z_0_spinBox.value),
                    int(parent_window.z_1_spinBox.value),
                    int(parent_window.z_step_spinBox.value),
                    "T"],#!!!!!!!!!!!!!!!!!!!!!!
        "point_A": [int(parent_window.a_inline_text.text),
                    int(parent_window.a_crline_text.text),
                    float(parent_window.a_x_text.text),
                    float(parent_window.a_y_text.text)],
        "point_B": [int(parent_window.b_inline_text.text),
                    int(parent_window.b_crline_text.text),
                    float(parent_window.b_x_text.text),
                    float(parent_window.b_y_text.text)],
        "point_C": [int(parent_window.c_inline_text.text),
                    int(parent_window.c_crline_text.text),
                    float(parent_window.c_x_text.text),
                    float(parent_window.c_y_text.text)]
    }
    survey_file = survey_root.joinpath('.survey')
    with survey_file.open('w') as wf:
        json.dump(survey_dict, wf, indent=4)

# -----------------------------------------------------------------------------
# Traverse folder structure
# -----------------------------------------------------------------------------
def get_available_survey_dir(data_root):
    """
    data_root : Path
    """
    dnames = list()
    for folder in data_root.glob("*/"):
        if list(folder.glob('*.survey')):
            dnames.append(folder.stem)
    return dnames

def get_data_files(dir_path):
    """
    get all dot file with given path

    dir_path: Path
    """
    fnames = list()
    # dir_path = Path(dir_path)
    if dir_path.exists():
        if list(dir_path.glob('.*')):
            for item in list(dir_path.glob('.*')):
                fnames.append(item.name[1:])
    return fnames

# -----------------------------------------------------------------------------
def create_new_seismic_file(name, like, conf):
    """
    create new seismic file including dot info file and segy file according to
    corresponding file
    """
    input_file = Seismic(like, conf)
    input_file.from_file()
    new_info_dict = deepcopy(input_file.info_dict)
    new_segy_path = conf.seismic_dir / "{}.sgy".format(name)
    try:
        copyfile(str(input_file.path), str(new_segy_path))
    except Exception as ex:
        print(ex.message)
    new_info_dict['path'] = str(new_segy_path)
    # create new file
    new_file_object = Seismic(name, conf)
    new_file_object.from_dict(new_info_dict)
    # write to file
    new_file_object.to_json_file(name)
