# -*- coding: utf-8 -*-
__author__ = 'Joaquin'


class CorpusUnigram:

    def __init__(self):
        self.information = {}

    def add_info(self, info):
        if (info in self.information):
            value = self.information.get(info)
            value += 1
            self.information[info] = value
        else:
            self.information[info] = 1

    def get_info(self, info):
        return self.information[info]

