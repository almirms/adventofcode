def read(diretorio):
    txt = open(diretorio + '/input.txt')
    return list(txt.read().replace("\n", ""))


def read_lines(diretorio):
    txt = open(diretorio + '/input.txt')
    return list(txt.readlines())
