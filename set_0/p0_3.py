# Programa que calcula o valor total devido, em $, ao final de um mês, com base no número de quilowatts-hora usados:

# Cada um dos primeiros 500 quilowatts-hora usados custa $0.45 / kWh
# Os próximos 1000 quilowatts-hora usados custam $0.74 / kWh
# Os próximos 1000 quilowatts-hora usados custam $1.25 / kWh
# Cada quilowatt-hora além de 2500 custa $2.00 / kWh

kwh_used = 1000

def getCust(kwhUsed):
    if kwhUsed <= 500:
        total = kwhUsed * 0.45
    elif kwhUsed > 500 and kwhUsed <= 1500:
        total = 500 * 0.45 + (kwhUsed - 500) * 0.74
    elif kwhUsed > 1500 and kwhUsed <= 2500:
        total = 500 * 0.45 + 1000 * 0.74 + (kwhUsed - 1500) * 1.25
    else:
        total = 500 * 0.45 + 1000 * 0.74 + 1000 * 1.25 + (kwhUsed - 2500) * 2
    return 1.2 * total

out = getCust(kwh_used)
print(out)