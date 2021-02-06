# Programa para definir funções de quadrados.

def square(n):
    return n ** 2

def fourth_power(n):
    return square(square(n))

def perfect_square(n):
    return n ** 0.5 == int(n ** 0.5)