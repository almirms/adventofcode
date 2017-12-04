# -*- coding: UTF-8 -*-
import hashlib


def calcular_zeros(string_entrada, qtde_zeros):
    zeros_concatenados = '0' * qtde_zeros

    hash_infinito = ''
    i = 0
    while hash_infinito != zeros_concatenados:
        i += 1
        hash_infinito = (hashlib.md5((string_entrada + str(i)).encode('utf-8')).hexdigest())[:qtde_zeros]

    return "pra começar com " + str(qtde_zeros) + " zeros na precisa de " + str(i) + " iterações"


entrada = "ckczppom"
print(calcular_zeros(entrada, 5))
print(calcular_zeros(entrada, 6))
