# -*- coding: UTF-8 -*-
import hashlib


def calcular_zeros(string_entrada, qtde_zeros):
    zeros_concatenados = ''
    for num in xrange(qtde_zeros):
        zeros_concatenados += '0'

    hash_infinito = ''
    i = 0
    while hash_infinito != zeros_concatenados:
        hash_infinito = (hashlib.md5((string_entrada + str(i))).hexdigest())[:qtde_zeros]
        i += 1

    print "começa com " + str(qtde_zeros) + " zeros na posicao: " + str(i - 1)

entrada = "ckczppom"
calcular_zeros(entrada, 5)
calcular_zeros(entrada, 6)
