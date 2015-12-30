# -*- coding: UTF-8 -*-
import os

import arquivo_de_entrada


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


def contem_caracteres_seguidos(string):
    lista_string = list(string)
    qtd_mais_que_dois_caracteres_em_sequencia = 0
    for caractere in lista_string:
        caracter_repetido_na_string = string.count(caractere + caractere)
        if caracter_repetido_na_string >= 1:
            qtd_mais_que_dois_caracteres_em_sequencia += 1
    if qtd_mais_que_dois_caracteres_em_sequencia > 0:
        return True
    return False


def contar_strings_boas(lista_strings):
    qtde_strings_boas = 0

    for string_percorrida in lista_strings:
        if contem_pelo_menos_tres_vogais(string_percorrida) and contem_caracteres_seguidos(
                string_percorrida) and nao_contem_bad_string(string_percorrida):
            qtde_strings_boas += 1

    return "a quantidade de strings boas é: " + str(qtde_strings_boas)


def allindices(string, sub, listindex=[], offset=0):
    i = string.find(sub, offset)
    while i >= 0:
        listindex.append(i)
        i = string.find(sub, i + 1)
    return listindex


def encontrar_pares(string_percorrida):
    return ["xx"]


def encontrar_indices_pares(string_percorrida):
    pares = encontrar_pares(string_percorrida)
    indices = list()
    for par in pares:
        indices.append(allindices(string_percorrida, par))

    # parei aqui +/-
    return indices


def encontrar_indices_letra_repetida_com_uma_no_meio(string_percorrida):


    return 0, 0


def regra_louca(string_percorrida):
    indices_pares = encontrar_indices_pares(string_percorrida)
    print indices_pares
    indices_letra_repetida_com_uma_no_meio = encontrar_indices_letra_repetida_com_uma_no_meio(string_percorrida)

    if indices_letra_repetida_com_uma_no_meio[0] >= indices_pares[0] and indices_letra_repetida_com_uma_no_meio[1] <= \
            indices_pares[1]:
        return True
    return False


def contar_strings_boas_nova_regra(lista_strings):
    qtde_strings_boas = 0
    for string_percorrida in lista_strings:
        if regra_louca(string_percorrida):
            print "boa: " + string_percorrida
            qtde_strings_boas += 1
        else:
            print "ruim: " + string_percorrida
    return "a quantidade de strings boas na nova regra é: " + str(qtde_strings_boas)


diretorio = os.path.dirname(os.path.abspath(__file__))
strings = arquivo_de_entrada.ler_linhas(diretorio)
print contar_strings_boas(strings)
# print contar_strings_boas_nova_regra(strings)
