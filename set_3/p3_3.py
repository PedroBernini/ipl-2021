# Programa para substituir valores de um dicionário através de uma função f.

def dictmap(d, f):
    for key in d:
        d[key] = f(d[key])