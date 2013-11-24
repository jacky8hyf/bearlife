from Model import Model
from Graphics import Graphics
class TestModel(Model):
    def __init__(self, ctrl):
        self.ctrl = ctrl
        def up():
            if self.graphics.array[self.x - 1][self.y] != WALL:
                self.graphics.array[self.x][self.y] = (Graphics.EMPTY, Graphics.WHITE)
                self.x -= 1
                self.graphics.array[self.x][self.y] = (self.hero, self.herocolor)
                self.refresh()
        def down():
            if self.graphics.array[self.x + 1][self.y] != WALL:
                self.graphics.array[self.x][self.y] = (Graphics.EMPTY, Graphics.WHITE)
                self.x += 1
                self.graphics.array[self.x][self.y] = (self.hero, self.herocolor)
                self.refresh()
        def left():
            if self.graphics.array[self.x][self.y - 1] != WALL:
                self.graphics.array[self.x][self.y] = (Graphics.EMPTY, Graphics.WHITE)
                self.y -= 1
                self.graphics.array[self.x][self.y] = (self.hero, self.herocolor)
                self.refresh()
        def right():
            if self.graphics.array[self.x][self.y + 1] != WALL:
                self.graphics.array[self.x][self.y] = (Graphics.EMPTY, Graphics.WHITE)
                self.y += 1
                self.graphics.array[self.x][self.y] = (self.hero, self.herocolor)
                self.refresh()
        
        arr = [list('##########################################'),
               list('#      #           #      #              #'),
               list('#      #   #########   #  #   #          #'),
               list('#                      #      #          #'),
               list('##########################################') 
        ]
        WALL = '#'
        self.x = 1
        self.y = 1
        self.hero = 'H'
        self.herocolor = Graphics.RED
        arr[self.x][self.y] = self.hero
        arr = [[(e, {'#':Graphics.GREEN, self.hero:self.herocolor, Graphics.EMPTY:Graphics.WHITE}[e]) for e in row] for row in arr]
        self.graphics = Graphics(arr)#, {'#':Graphics.GREEN, self.hero:self.herocolor} , startX, startY)
        self.key_funcs = {
            ord('w'): up,
            ord('s'): down,
            ord('a'): left,
            ord('d'): right      
          }
        self.refresh()
        # FIXME Start of game init.
