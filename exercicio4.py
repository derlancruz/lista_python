#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Pessoa(object):

    def __init__(self, idade, peso, altura):
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self):
        self.age += 1
        if self.age <= 21:
            self.altura += 1.5

    def engordar(self, kg):
        self.peso += kg

    def emagrecer(self, kg):
        self.peso -= kg