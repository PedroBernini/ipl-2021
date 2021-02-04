# Programa para calcular a média aritmética de uma lista de números (que podem ser ints ou floats). 

numbers = [2, 7, 3, 9, 13]

def getMean(numbers):
    return sum(numbers) / len(numbers) if numbers else None

out = getMean(numbers)
print(out)