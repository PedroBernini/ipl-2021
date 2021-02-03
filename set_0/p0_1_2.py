# Programa para calcular a distância euclidiana entre um ponto (px,py) no plano e uma linha especificada pela equação geral da reta.

px = 1
py = 2
a = 3
b = 4
c = 5

def getDistance(point, equation):
    numerator = abs((equation['a'] * point['x']) + (equation['b'] * point['y']) + equation['c'])
    denominator = (equation['a'] ** 2 + equation['b'] ** 2) ** 0.5
    return numerator / denominator

point = {
    'x': px,
    'y': py
}

equation = {
    'a': a,
    'b': b,
    'c': c
}

out = getDistance(point, equation)
print(out)