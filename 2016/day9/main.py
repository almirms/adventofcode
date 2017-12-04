# -*- coding: UTF-8 -*-
import os
import input_file
import itertools


def calcular_menor_rota(viagens):
    rotas, viagens_possiveis = calcular_viagens_possiveis_e_rotas(viagens)

    tamanho_min = 9999999
    rota_minima = list()
    for rota in rotas:
        try:
            tamanho_da_rota = calcular_tamanho_rota(rota, viagens_possiveis)

            if tamanho_da_rota < tamanho_min:
                tamanho_min = tamanho_da_rota
                rota_minima = rota

        except KeyError:
            # rota não existente
            continue

    return "a menor rota é " + str(rota_minima) + " medindo " + str(tamanho_min)


def calcular_maior_rota(viagens):
    rotas, viagens_possiveis = calcular_viagens_possiveis_e_rotas(viagens)

    tamanho_maximo = 0
    rota_maxima = list()
    for rota in rotas:
        try:
            tamanho_da_rota = calcular_tamanho_rota(rota, viagens_possiveis)

            if tamanho_da_rota > tamanho_maximo:
                tamanho_maximo = tamanho_da_rota
                rota_maxima = rota

        except KeyError:
            # rota não existente
            continue

    return "a maior rota é " + str(rota_maxima) + " medindo " + str(tamanho_maximo)


def calcular_tamanho_rota(rota, viagens_possiveis):
    tamanho_da_rota = viagens_possiveis[rota[0], rota[1]] + viagens_possiveis[rota[1], rota[
        2]] + viagens_possiveis[rota[2], rota[3]] + viagens_possiveis[rota[3], rota[4]] + \
                      viagens_possiveis[rota[4], rota[5]] + \
                      viagens_possiveis[rota[5], rota[6]] + \
                      viagens_possiveis[rota[6], rota[7]]
    return tamanho_da_rota


def calcular_viagens_possiveis_e_rotas(viagens):
    viagens_possiveis = {}
    cidades_unicas = set()
    for viagem in viagens:
        cidades_distancia = viagem.split(' = ')
        cidades = cidades_distancia[0].split(' to ')
        cidades_unicas.update(cidades)
        distancia = cidades_distancia[1]
        viagens_possiveis[cidades[0], cidades[1]] = int(distancia.replace('\n', ''))
        viagens_possiveis[cidades[1], cidades[0]] = int(distancia.replace('\n', ''))
    rotas = list(itertools.permutations(list(cidades_unicas)))
    return rotas, viagens_possiveis


diretorio = os.path.dirname(os.path.abspath(__file__))
viagens_lista = input_file.ler_linhas(diretorio)
print(calcular_menor_rota(viagens_lista))
print(calcular_maior_rota(viagens_lista))
