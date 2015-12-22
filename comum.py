def ler(diretorio):
    txt = open(diretorio + '/input.txt')
    return list(txt.read())


def ler_linhas(diretorio):
    txt = open(diretorio + '/input.txt')
    return list(txt.readlines())
