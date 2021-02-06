# Programa para definir função de número primo.

def prime(n):
    if n in [0, 1]:
        return False
    for number in range(2, n):
        if n % number == 0 and n != number:
            return False
    return True