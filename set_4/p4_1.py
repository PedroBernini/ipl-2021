# Programa para modelar um simples sistema de contabilidade de armazém.

def warehouse_process(stock, transition):
    if transition[0] == 'receive':
        if transition[1] in stock:
            stock[transition[1]] += transition[2]
        else:
            stock[transition[1]] = transition[2]
    else:
        if transition[1] not in stock or stock[transition[1]] < transition[2]:
            stock[transition[1]] = 0
            print('not enough')
        else:
            stock[transition[1]] -= transition[2]

class Warehouse():
    def __init__(self):
        self.stock = {}
    
    def process(self, transition):
        if transition[0] == 'receive':
            if transition[1] in self.stock:
                self.stock[transition[1]] += transition[2]
            else:
                self.stock[transition[1]] = transition[2]
        else:
            if transition[1] not in self.stock or self.stock[transition[1]] < transition[2]:
                self.stock[transition[1]] = 0
                print('not enough')
            else:
                self.stock[transition[1]] -= transition[2]
    
    def lookup(self, supply):
        return self.stock[supply] if supply in self.stock else 0
