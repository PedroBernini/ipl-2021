# Programa para mapear os empréstimos de amigos.

def lend_money(debts, person, amount):
    if person in debts:
        debts[person].append(amount)
    else:
        debts[person] = [amount]

def amount_owed_by(debts, person):
    return sum(debts[person]) if person in debts else 0

def total_amount_owed(debts):
    return sum([sum(debts[debt]) for debt in debts])