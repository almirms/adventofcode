# -*- coding: UTF-8 -*-
import os
import comum
from itertools import izip


def quantas_casas_receberam_ao_menos_um_presente(coordenadas):
    pos_x = 0
    pos_y = 0
    coordenadas_passadas = [(0, 0)]
    for coordenada in coordenadas:
        if coordenada == '^':
            pos_y += 1
            item = pos_x, pos_y
            coordenadas_passadas.append(item)
        elif coordenada == '>':
            pos_x += 1
            item = pos_x, pos_y
            coordenadas_passadas.append(item)
        elif coordenada == '<':
            pos_x -= 1
            item = pos_x, pos_y
            coordenadas_passadas.append(item)
        elif coordenada == 'v':
            pos_y -= 1
            item = pos_x, pos_y
            coordenadas_passadas.append(item)
    return "papai noel passou por " + str(len(set(coordenadas_passadas))) + " únicas casas"


def pairwise(iterable):
    a = iter(iterable)
    return izip(a, a)


def quantas_casas_receberam_ao_menos_um_presente_com_ajuda_do_robo(coordenadas):
    pos_x_papai_noel = 0
    pos_y_papai_noel = 0
    pos_x_robo = 0
    pos_y_robo = 0
    coordenadas_passadas = [(0, 0)]
    for coordenada in pairwise(coordenadas):
        coordenada_papai_noel = coordenada[0]
        coordenada_robo = coordenada[1]

        if coordenada_papai_noel == '^':
            pos_y_papai_noel += 1
            item = pos_x_papai_noel, pos_y_papai_noel
            coordenadas_passadas.append(item)
        elif coordenada_papai_noel == '>':
            pos_x_papai_noel += 1
            item = pos_x_papai_noel, pos_y_papai_noel
            coordenadas_passadas.append(item)
        elif coordenada_papai_noel == '<':
            pos_x_papai_noel -= 1
            item = pos_x_papai_noel, pos_y_papai_noel
            coordenadas_passadas.append(item)
        elif coordenada_papai_noel == 'v':
            pos_y_papai_noel -= 1
            item = pos_x_papai_noel, pos_y_papai_noel
            coordenadas_passadas.append(item)

        if coordenada_robo == '^':
            pos_y_robo += 1
            item = pos_x_robo, pos_y_robo
            coordenadas_passadas.append(item)
        elif coordenada_robo == '>':
            pos_x_robo += 1
            item = pos_x_robo, pos_y_robo
            coordenadas_passadas.append(item)
        elif coordenada_robo == '<':
            pos_x_robo -= 1
            item = pos_x_robo, pos_y_robo
            coordenadas_passadas.append(item)
        elif coordenada_robo == 'v':
            pos_y_robo -= 1
            item = pos_x_robo, pos_y_robo
            coordenadas_passadas.append(item)

    return "papai noel e o robô passaram por " + str(len(set(coordenadas_passadas))) + " únicas casas"

diretorio = os.path.dirname(os.path.abspath(__file__))
coords = comum.ler(diretorio)
print quantas_casas_receberam_ao_menos_um_presente(coords)
print quantas_casas_receberam_ao_menos_um_presente_com_ajuda_do_robo(coords)
