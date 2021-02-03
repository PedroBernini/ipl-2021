# Programa baseado no algoritmo de Zeller, que calcula o dia da semana em que uma determinada data caiu (ou cairá).

year = 2017
month = 1
day = 9

def zellerAlgorithm(year, month, day):
    if month in [1, 2]:
        y1 = year - 1
        m1 = month + 12
    else:
        y1 = year
        m1 = month
    y2 = y1 % 100
    c = int(y1 / 100)

    return (day + int((13 * (m1 + 1)) / 5) + y2 + int(y2 / 4) + int(c / 4) - 2 * c) % 7

out = zellerAlgorithm(year, month, day)
print(out)