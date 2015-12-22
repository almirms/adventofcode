# -*- coding: UTF-8 -*-
import os
import comum


def aonde_parou(movimentos):
    andar = 0
    for movimento in movimentos:
        if movimento == '(':
            andar += 1
        else:
            andar -= 1
    print "parei no andar: " + str(andar)


def primeira_vez_no_porao(movimentos):
    andar = 0
    for index, movimento in enumerate(movimentos):
        if movimento == '(':
            andar += 1
        else:
            andar -= 1
        if andar == -1:
            print "parei no -1 na posição: " + str(index + 1)
            return

diretorio = os.path.dirname(os.path.abspath(__file__))
movimentos_papai_noel = comum.ler(diretorio)
aonde_parou(movimentos_papai_noel)
primeira_vez_no_porao(movimentos_papai_noel)

