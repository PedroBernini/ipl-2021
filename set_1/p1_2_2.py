# Programa para calcular a média geométrica de uma lista de números (que pode ser ints ou floats). 

numbers = [2, 7, 3, 9, 13]

def getGeometricMean(numbers):
    if numbers:
        product = 1
        for number in numbers:
            product *= number
        return product ** (1 / len(numbers))
    else:
        None

out = getGeometricMean(numbers)
print(out)