# Programa para simular a Formiga de Langton.

class Ant():
    def __init__(self, position):
        self.DIRECTIONS = {
            'R': {
                'UP': 'RIGHT',
                'RIGHT':'DOWN',
                'DOWN': 'LEFT',
                'LEFT': 'UP'
            },
            'L': {
                'UP': 'LEFT',
                'RIGHT': 'UP',
                'DOWN': 'RIGHT',
                'LEFT': 'DOWN'
            }
        }
        self.MOVES = {
            'UP': {
                'line': -1,
                'col': 0
            },
            'RIGHT': {
                'line': 0,
                'col': 1
            },
            'DOWN': {
                'line': 1,
                'col': 0
            },
            'LEFT': {
                'line': 0,
                'col': -1
            }
        }
        self.position = position
        self.orientation = 'UP'
    
    def changePosition(self, position):
        self.position = position

    def walk(self):
        move = self.MOVES[self.orientation]
        self.position[0] += move['line']
        self.position[1] += move['col']
        return self.position

    def rotate(self, color, rules):
        direction = rules[color]
        self.orientation = self.DIRECTIONS[direction][self.orientation]

class AntLangton():
    def __init__(self, rules, size):
        self.num_colors = len(rules)
        self.rules = {i: rules[i] for i in range(len(rules))}
        self.size = size
        self.grid = [[0 for i in range(size)] for i in range(size)]
        self.ant = Ant(self.getMiddleGrid())

    def isValidPosition(self, position):
        if position[0] < 0 or position[0] >= self.size:
            return False
        if position[1] < 0 or position[1] >= self.size:
            return False
        return True

    def start(self):
        moves = 0
        position = self.ant.position
        while self.isValidPosition(position):
            print(self.ant.position)
            moves += 1
            self.changeColor(self.ant.position[0], self.ant.position[1])
            position = self.ant.walk()
            if not self.isValidPosition(position):
                break
            self.ant.rotate(self.getColor(), self.rules)
        return moves, self.grid
            
    def getColor(self):
        return self.grid[self.ant.position[0]][self.ant.position[1]]

    def getNextColor(self, color):
        return (color + 1) % self.num_colors

    def getMiddleGrid(self):
        return [int((self.size - 1) / 2), int((self.size - 1) / 2)]

    def changeColor(self, line, col):
        self.grid[line][col] = self.getNextColor(self.grid[line][col])

def run_langton(rules, size):
    antLangton = AntLangton(rules, size)
    return antLangton.start()

print(run_langton('RL', 4))