# -*- coding: UTF-8 -*-
import os
import comum


def papel_de_presente(dimensoes):
    area_total = 0
    for dimensao in dimensoes:
        l, w, h = [int(x) for x in dimensao.split('x')]

        l_w = l * w
        w_h = w * h
        h_l = h * l

        area1 = 2 * l_w
        area2 = 2 * w_h
        area3 = 2 * h_l

        area4 = min(l_w, w_h, h_l)
        area_total += area1 + area2 + area3 + area4
    print "vamos precisar de: " + str(area_total) + " m² de papel de presente."


def laco_de_fita(dimensoes):
    medida_total = 0
    for dimensao in dimensoes:
        l, w, h = [int(x) for x in dimensao.split('x')]
        medida1 = l * w * h

        lista = list()
        lista.append(l)
        lista.append(w)
        lista.append(h)
        medida2 = min(lista)
        lista.remove(medida2)
        medida3 = min(lista)

        medida_total += medida1 + 2*medida2 + 2*medida3

    print "vamos precisar de: " + str(medida_total) + " m de fita de presente."

diretorio = os.path.dirname(os.path.abspath(__file__))
dimensoes_presentes = comum.ler_linhas(diretorio)
papel_de_presente(dimensoes_presentes)
laco_de_fita(dimensoes_presentes)
