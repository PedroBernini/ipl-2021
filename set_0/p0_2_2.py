# Programa para calcular as raízes da expressão "ax2 + bx + c".

a = 1
b = 2
c = 3

def getRoots(equation):
    delta = equation['b'] ** 2 - (4 * equation['a'] * equation['c'])
    x1 = (-equation['b'] + (delta) ** 0.5) / (2 * equation['a'])
    x2 = (-equation['b'] - (delta) ** 0.5) / (2 * equation['a'])
    if x1 == x2:
        return x1
    return x1, x2

equation = {
    'a': a,
    'b': b,
    'c': c,
}

out = getRoots(equation)
print(out)