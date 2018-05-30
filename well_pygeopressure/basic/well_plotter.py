# -*- coding: utf-8 -*-
"""
A control for plotting well log data

Created on Sun Jan 21 2018
"""
from __future__ import (division, absolute_import, print_function,
                        with_statement, unicode_literals)

__author__ = "Yu Hao"


class WellPlotter(object):
    def __init__(self, fig, well_log):
        self.fig = fig
        self.well_log = well_log

    def plot_well_log(self, clear=True):
        if clear is True:
            self.fig.clf()
        if not self.fig.get_axes(): # empty
            self.fig.add_subplot(111)
        ax = self.fig.get_axes()[0]
        ax.invert_yaxis()
        ax.plot(self.well_log.data, self.well_log.depth)
        ax.set(xlabel="{}({})".format(self.well_log.descr, self.well_log.units),
               ylabel="Depth(m)",
               title=self.well_log.name,
               ylim=[self.well_log.stop, 0])
