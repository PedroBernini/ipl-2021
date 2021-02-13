# Programa para definir classe chamada Matrix para representar matrizes bidimensionais.

class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def size(self):
        return len(self.matrix), len(self.matrix[0]) if self.matrix else 0
    
    def get(self, r, c):
        return self.matrix[r][c]

    def set(self, r, c, val):
        self.matrix[r][c] = val

    def row(self, n):
        return self.matrix[n]

    def col(self, n):
        return [element for row in self.matrix for index, element in enumerate(row) if index == n]

    def transpose(self):
        return Matrix([list(line) for line in [*zip(*self.matrix)]])
    
    def __add__(self, other):
        nRows, nCols = self.size()
        if isinstance(other, Matrix) and nRows == other.size()[0] and nCols == other.size()[1]:
            return Matrix([[self.matrix[i][j] + other.matrix[i][j] for j in range(nCols)] for i in range(nRows)])
        
        if isinstance(other, int) or isinstance(other, float):
            return Matrix([[self.matrix[i][j] + other for j in range(nCols)] for i in range(nRows)])

    def __sub__(self, other):
        nRows, nCols = self.size()
        if isinstance(other, Matrix) and nRows == other.size()[0] and nCols == other.size()[1]:
            return Matrix([[self.matrix[i][j] - other.matrix[i][j] for j in range(nCols)] for i in range(nRows)])
        
        if isinstance(other, int) or isinstance(other, float):
            return Matrix([[self.matrix[i][j] - other for j in range(nCols)] for i in range(nRows)])

    def __mul__(self, other):
        nRows, nCols = self.size()
        if isinstance(other, Matrix) and nCols == other.size()[0]:
            newMatrix = []
            for i in range(nRows):
                newMatrix.append([])
                for j in range(other.size()[1]):
                    newMatrix[i].append(sum([e1 * e2 for e1, e2 in zip(self.row(i), other.col(j))]))
            return Matrix(newMatrix)

        if isinstance(other, int) or isinstance(other, float):
            return Matrix([[self.matrix[i][j] * other for j in range(nCols)] for i in range(nRows)])
