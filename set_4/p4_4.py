# Programa para criação de uma classe que representa os vetores n-dimensionais.

class Vector():
    def __init__(self, vector):
        self.vector = vector 

    def as_list(self):
        return self.vector
    
    def size(self):
        return len(self.vector)

    def magnitude(self):
        mag = 0
        for value in self.vector:
            mag += value ** 2
        return mag ** 0.5
    
    def euclidean_distance(self, other):
        distance = 0
        for element in range(len(self.vector)):
            distance += (self.vector[element] - other.vector[element]) ** 2
        return distance ** 0.5
    
    def normalized(self):
        return Vector([value / self.magnitude() for value in self.vector])

    def cosine_similarity(self, other):
        num = 0
        for element in range(len(self.vector)):
            num += self.vector[element] * other.vector[element]
        return num / (self.magnitude() * other.magnitude())
    
    def __add__(self, other):
        if isinstance(other, Vector) and len(self.vector) == len(other.vector):
            return Vector([self.vector[element] + other.vector[element] for element in range(len(self.vector))])
        
        if isinstance(other, int):
            return self.vector + other.vector
    
    def __sub__(self, other):
        if isinstance(other, Vector) and len(self.vector) == len(other.vector):
            return Vector([self.vector[element] - other.vector[element] for element in range(len(self.vector))])

        if isinstance(other, int):
            return self.vector - other.vector
    
    def __mul__(self, other):
        if isinstance(other, Vector) and len(self.vector) == len(other.vector):
            escalarProduct = 0
            for element in range(len(self.vector)):
                escalarProduct += self.vector[element] * other.vector[element]
            return escalarProduct
        
        if isinstance(other, int) or isinstance(other, float):
            return Vector([self.vector[element] * other for element in range(len(self.vector))])
    
    def __truediv__(self, other):
        if isinstance(other, float) or isinstance(other, int):
            return Vector([self.vector[element] / other for element in range(len(self.vector))])