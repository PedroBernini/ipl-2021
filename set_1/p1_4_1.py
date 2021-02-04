# Programa que calcule a derivada simbólica de um polinômio dado nesta forma.

poly = [0, 0, 1/2]

def getDerivative(coefficients):
    return [coefficients[i] * i for i in range(1, len(coefficients))]
    
out = getDerivative(poly)
print(out)