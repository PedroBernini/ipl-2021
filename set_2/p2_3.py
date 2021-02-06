# Programa para o problema das n portas.

def execPassage(doors, n):
    for door in doors:
        if door[0] % n == 0:
            door[1] = 1 if door[1] == 0 else 0
    return doors

def ndoors(n):
    doors = [[i, 0] for i in range(1, n + 1)]
    for i in range(1, n + 1):
        execPassage(doors, i)
    return [door[0] for door in doors if door[1] == 1]