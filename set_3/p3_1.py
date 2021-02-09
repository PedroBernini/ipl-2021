# Programa para compactar conjuntos de dados esparsos com corridas longas (sequências do mesmo valor) utilizando a técnica "codificação run-length".

def run_length_encode_2d(array):
    encodeArray = []
    number = None
    count = 1
    for current in [number for row in array for number in row]:
        if current == number:
            count += 1
        else:
            if number != None:
                encodeArray.append((count, number))
            number = current
            count = 1
    if number != None:
        encodeArray.append((count, number))
    return encodeArray
            
print(run_length_encode_2d([]))
