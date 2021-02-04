# Programa que calcule a integral simbólica de um polinômio dado nesta forma.

poly = [0]

const = 'c'

def getIntegral(coefficients):
    return [const] + [coefficients[i] / (i + 1) for i in range(0, len(coefficients))]
    
out = getIntegral(poly)
print(out)