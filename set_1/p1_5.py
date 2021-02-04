# Programa que calcule o custo de uma pizza sob este modelo.

size = 'small'
toppings = ['presunto', 'abacaxi']

CUST = {
    'small': 14,
    'medium': 16,
    'large': 18
}

def getCust(size, toppings):
    cust = CUST[size]
    for i in range(len(toppings)):
        cust += cust * (12 + i + len(toppings[i])) / 100
    if 'bacon' in toppings or 'anchovas' in toppings:
        return 1.1 * cust
    return cust
    
out = round(getCust(size, toppings), 2)
print(out)