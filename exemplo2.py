#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Quadrado(object):

    def __init__(self, lado):
        self.lado = lado

    @property
    def area(self):
        return self.side ** 2