# Programa para aproximar o valor de π.

p_d = 151

def isValidCell(cell, pd):
    return (cell[0] ** 2 + cell[1] ** 2) ** 0.5 <= pd / 2

def getNumberValidCells(pd):
    validCells = 0
    limit = int(pd / 2)
    for j in range(limit, -(limit + 1), -1):
        for i in range(-limit, limit + 1):
            if isValidCell((i, j), pd):
                validCells += 1
    return validCells

def getPiApproximation(numberValidCells, totalCells):
    return numberValidCells / totalCells * 4

out = getPiApproximation(getNumberValidCells(p_d), p_d ** 2)
print(out)