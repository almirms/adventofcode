# -*- coding: UTF-8 -*-
import os
import comum
from itertools import izip


def contem_pelo_menos_tres_vogais(string):
    vogais = ('a', 'e', 'i', 'o', 'u')
    vogais_na_string = 0

    for vogal in vogais:
        vogais_na_string += string.count(vogal)

    if vogais_na_string > 2:
        return True
    return False


def nao_contem_bad_string(string):
    bad_strings = ('ab', 'cd', 'pq', 'xy')
    qtde_bad_string = 0
    for bad_string in bad_strings:
        qtde_bad_string += string.count(bad_string)

    if qtde_bad_string == 0:
        return True
    return False


def contem_mais_que_dois_caracteres_repetidos(string):
    lista_string = list(string)
    qtd_mais_que_dois_caracteres_repetidos = 0
    for caracter in lista_string:
        caracter_repetido_na_string = string.count(caracter)
        if caracter_repetido_na_string > 2:
            qtd_mais_que_dois_caracteres_repetidos += 1
    if qtd_mais_que_dois_caracteres_repetidos > 0:
        return True
    return False


def contar_strings_boas(lista_strings):
    qtde_strings_boas = 0

    for string_percorrida in lista_strings:
        if contem_pelo_menos_tres_vogais(string_percorrida) and contem_mais_que_dois_caracteres_repetidos(string_percorrida) and nao_contem_bad_string(string_percorrida):
            qtde_strings_boas += 1

    return qtde_strings_boas

diretorio = os.path.dirname(os.path.abspath(__file__))
strings = comum.ler_linhas(diretorio)
print contar_strings_boas(strings)
