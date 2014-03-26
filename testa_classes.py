#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from exemplo1 import Bola

class TestaExemplo1(unittest.TestCase):

    def cor_bola(self):
        self.bola = Bola('amarela')

##Isso aqui é opcional, o exercício não pede testes, eu que tou implementano
    def validar_cor_da_bola(self):
        self.bola.cor |should| equal_to('amarela')

    def mudar_cor_da_bola(self):
        self.bola.cor = 'vermelha'
        self.bola.cor |should| equal_to('vermelha')