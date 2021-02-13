# Programa para criação de uma classe que representa os números racionais como frações.

class Rational:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
    
    def get_numerator(self):
        return self.numerator

    def get_denominator(self):
        return self.denominator
    
    def to_float(self):
        return self.numerator / self.denominator
    
    def reciprocal(self):
        return Rational(self.denominator,self.numerator)

    def reduce(self):
        def mdc(n1, n2):
            return n1 if not n2 else mdc(n2, n1 % n2)
        mdc = mdc(self.numerator, self.denominator)
        return Rational(self.numerator / mdc, self.denominator / mdc)
    
    def __add__(self, other):
        if isinstance(other, Rational):
            numerator = (self.numerator * other.denominator) + (other.numerator * self.denominator)
            denominator = self.denominator * other.denominator
            return Rational(numerator, denominator).reduce()
        
        if isinstance(other, int):
            numerator = self.numerator + (other.numerator * self.denominator)
            denominator = self.denominator
            return Rational(numerator, denominator).reduce()
        
        if isinstance(other, float):
            return (self.numerator / self.denominator) + other

    def __mul__(self, other):
        if isinstance(other, Rational):
            numerator = self.numerator * other.numerator
            denominator = self.denominator * other.denominator
            return Rational(numerator, denominator).reduce()
        
        if isinstance(other, int):
            numerator = self.numerator * other
            denominator = self.denominator
            return Rational(numerator, denominator).reduce()
        
        if isinstance(other, float):
            return (self.numerator * other) / self.denominator

    def __truediv__(self, other):
        if isinstance(other, Rational):
            numerator = self.numerator * other.denominator
            denominator = self.denominator * other.numerator
            return Rational(numerator, denominator).reduce()
        
        if isinstance(other, int):
            numerator = self.numerator
            denominator = self.denominator * other
            return Rational(numerator, denominator).reduce()
        
        if isinstance(other, float):
            return (self.numerator / self.denominator) / other

    def __sub__(self, other):
        if isinstance(other, Rational):
            numerator = (self.numerator * other.denominator) - (other.numerator * self.denominator)
            denominator = self.denominator * other.denominator
            return Rational(numerator, denominator).reduce()
        
        if isinstance(other, int):
            numerator = self.numerator - (other * self.denominator)
            denominator = self.denominator
            return Rational(numerator, denominator).reduce()
        
        if isinstance(other, float):
            return (self.numerator / self.denominator) - other