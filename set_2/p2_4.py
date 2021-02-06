# Programa para encontrar e retornar os maiores números em uma lista de números arbitrários.

def largest_number(input_list):
    if input_list:
        best_so_far = float('-inf')
        for i in range(len(input_list)):
            if input_list[i] > best_so_far:
                best_so_far = input_list[i]
        return best_so_far
    else:
        return None

def second_largest_number(input_list):
    if len(input_list) in [0, 1]:
        return None
    best_so_far = second_best_so_far = float('-inf')
    for number in input_list:
        if number > second_best_so_far:
            if number > best_so_far:
                second_best_so_far = best_so_far  
                best_so_far = number
            else:
                second_best_so_far = number
    return second_best_so_far