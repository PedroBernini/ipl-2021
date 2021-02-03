# Programa para calcular o resultado da avaliação de uma expressão "ax2 + bx + c" em um valor particular de x.

a = 1
b = 2
c = 3
x = 0.5

def quadraticFunction(equation):
    return (equation['a'] * equation['x']) ** 2  + equation['b'] * equation['x'] + equation['c']

equation = {
    'a': a,
    'b': b,
    'c': c,
    'x': x
}

out = quadraticFunction(equation)
print(out)