#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Retangulo(object):

    def __init__(self, base, altura):
        self.base = base
        self.height = altura

    @property
    def area(self):
        return self.base * self.altura

    @property
    def perimeter(self):
        return (self.base * 2) + (self.altura * 2)