# -*- coding: UTF-8 -*-
import os
import arquivo_de_entrada


def aonde_parou(movimentos):
    andar = 0
    for movimento in movimentos:
        if movimento == '(':
            andar += 1
        else:
            andar -= 1
    return "parei no andar: " + str(andar)


def primeira_vez_no_porao(movimentos):
    andar = 0
    for index, movimento in enumerate(movimentos):
        if movimento == '(':
            andar += 1
        else:
            andar -= 1
        if andar == -1:
            return "parei no -1 na posição: " + str(index + 1)

diretorio = os.path.dirname(os.path.abspath(__file__))
movimentos_papai_noel = arquivo_de_entrada.ler(diretorio)
print aonde_parou(movimentos_papai_noel)
print primeira_vez_no_porao(movimentos_papai_noel)

