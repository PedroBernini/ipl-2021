# Programa para calcular juros compostos.

interest_rate = 0.3

def getMonths(interest_rate):
    if interest_rate:
        totalRate = 1
        months = 0
        while totalRate < 2:
            totalRate *= interest_rate + 1
            months += 1
        return months
    return 'NEVER'

out = getMonths(interest_rate)
print(out)