# Programa para "números de granizo" (hailstone sequence) ou "números maravilhosos".

def hailstone_sequence(a_0):
    if a_0 == 1:
        return [a_0]
    if a_0 % 2 == 0:
        return [a_0] + hailstone_sequence(a_0 / 2)
    return [a_0] + hailstone_sequence(3 * a_0 + 1)