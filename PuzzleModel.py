from Model import Model
from Graphics import Graphics
from ucb import trace
class PuzzleModel(Model):
    """An abstract maze. """
    def __init__(self, ctrl, graphics, arr, startX, startY, endX, endY):
        self.ctrl = ctrl
        self.ctrl.setTimeOut(0.1)
        self.graphics = graphics
        self.arr = arr
        self.WALL = '█'
        self.x = startX
        self.y = startY
        self.endX = endX
        self.endY = endY
        self.hero = 'λ'
        self.herocolor = Graphics.CYAN
        arr[self.x][self.y] = self.hero
        arr = [[(e, {self.WALL:Graphics.BLACK, self.hero:self.herocolor, Graphics.EMPTY:Graphics.WHITE}[e]) for e in row] for row in arr]
        arr[self.endX][self.endY] = (Graphics.EMPTY, Graphics.WHITE * 9)
        self.graphics.array = arr
        self.refresh()
    def process(self, key):
        def up():
            if self.graphics.array[self.x - 1][self.y][0] != self.WALL:
                self.graphics.array[self.x][self.y] = (Graphics.EMPTY, Graphics.WHITE)
                self.x -= 1
                self.graphics.array[self.x][self.y] = (self.hero, self.herocolor)
                self.refresh()
                return (self.x, self.y) == (self.endX, self.endY)
        def down():
            if self.graphics.array[self.x + 1][self.y][0] != self.WALL:
                self.graphics.array[self.x][self.y] = (Graphics.EMPTY, Graphics.WHITE)
                self.x += 1
                self.graphics.array[self.x][self.y] = (self.hero, self.herocolor)
                self.refresh()
                return (self.x, self.y) == (self.endX, self.endY)
        def left():
            if self.graphics.array[self.x][self.y - 1][0] != self.WALL:
                self.graphics.array[self.x][self.y] = (Graphics.EMPTY, Graphics.WHITE)
                self.y -= 1
                self.graphics.array[self.x][self.y] = (self.hero, self.herocolor)
                self.refresh()
                return (self.x, self.y) == (self.endX, self.endY)
        def right():
            if self.graphics.array[self.x][self.y + 1][0] != self.WALL:
                self.graphics.array[self.x][self.y] = (Graphics.EMPTY, Graphics.WHITE)
                self.y += 1
                self.graphics.array[self.x][self.y] = (self.hero, self.herocolor)
                self.refresh()
                return (self.x, self.y) == (self.endX, self.endY)
        d = {
            ord('w'): up,
            ord('s'): down,
            ord('a'): left,
            ord('d'): right      
        }
        if key in d: 
            return d[key]()
    def timeout(self):
        return False
