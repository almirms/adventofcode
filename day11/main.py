# -*- coding: UTF-8 -*-


def incrementar_senha(senha):
    tamanho_senha = len(senha)

    ultima_senha = 'a' * tamanho_senha

    senha_incrementada = senha

    while senha_incrementada != ultima_senha:
        senha_incrementada = adicionar_um(senha_incrementada)
        print senha_incrementada
    return senha_incrementada


def achar_ultimo_char_diferente_de_a(senha):
    a_split = senha.rsplit('a')
    if len(a_split) == 1 or a_split[1] == '':

        return len(senha) - 1, a_split[0][-1:]
    else:
        return 1


def adicionar_um(senha):

    ultima_posicao_diferente_de_a, char_ultima_posicao_diferente_de_a = achar_ultimo_char_diferente_de_a(senha)
    if char_ultima_posicao_diferente_de_a == 'z':
        senha = senha[:ultima_posicao_diferente_de_a] + 'a' + senha[ultima_posicao_diferente_de_a + 1:]

    else:
        senha = senha[:ultima_posicao_diferente_de_a] + chr(ord(char_ultima_posicao_diferente_de_a) + 1) \
                + senha[ultima_posicao_diferente_de_a + 1:]

    return senha


entrada = "cqjxjnds"
incrementar_senha(entrada)
