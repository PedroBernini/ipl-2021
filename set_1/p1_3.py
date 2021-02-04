# Programa para calcular o quociente e o restante ao dividir dois números usando a divisão inteira.

dividend = 7
divisor = 2

def getDivmod(dividend, divisor):
    quotient = 0
    rest = dividend
    while rest >= divisor:
        rest -= divisor
        quotient += 1
    return quotient, rest

out = getDivmod(dividend, divisor)
print(out)