# -*- coding: UTF-8 -*-
import hashlib


def calcular_zeros(string_entrada, qtde_zeros):
    out_str = ''
    for num in xrange(qtde_zeros):
        out_str += '0'

    hash_infinito = ''
    i = 0
    while hash_infinito != out_str:
        hash_infinito = hashlib.md5((string_entrada + str(i)).encode()).hexdigest()[:qtde_zeros]
        i += 1

    print i - 1

entrada = "ckczppom"
calcular_zeros(entrada, 5)
calcular_zeros(entrada, 6)
