# Programa para calcular a distância euclidiana entre dois pontos (x1,y1) e (x2,y2).

x1 = 1
y1 = 2
x2 = 3
y2 = 4

def getDistance(pointA, pointB):
    return ((pointB['x'] - pointA['x']) ** 2 + (pointB['y'] - pointA['y']) ** 2) ** 0.5

pointA = {
    'x': x1,
    'y': y1
}

pointB = {
    'x': x2,
    'y': y2
}

out = getDistance(pointA, pointB)
print(out)