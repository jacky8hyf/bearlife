from Graphics import Graphics
from Model import Model
from EndModel import EndModel
import random as r
from ucb import trace
import time
from time import time as now
duration = 10
class RaidenModel(Model):
    def __init__(self, ctrl, graphics, parent = None):
        self.ctrl = ctrl
        self.ctrl.setTimeOut(0.5);
        self.graphics = graphics
        self.parent = parent
        self.started = False
        self.missles = list()
        self.bullets = list()
        self.misslesEnd = True
        self.x = Graphics.DEFAULT_HEIGHT - 1
        self.y = Graphics.DEFAULT_WIDTH // 2
        self.empty = (' ', Graphics.WHITE)
        self.bullet = ('*', Graphics.YELLOW)
        self.me = ('^',Graphics.BLUE)
        self.missle = ('V', Graphics.RED)
        self.array = list()
        for i in range(Graphics.DEFAULT_HEIGHT):
            self.array.append(list())
            for j in range(Graphics.DEFAULT_WIDTH):
                self.array[i].append(tuple(self.empty))
        self.array[self.x][self.y] = self.me
        self.graphics.array = self.array
        self.keyfn = {ord('w'):self.up, ord('s'):self.down, ord('a'):self.left, ord('d'):self.right, ord(' '):self.shoot}
        self.graphics.showline()
        self.graphics.showline()
        self.graphics.showline()
        self.graphics.showline()
        self.graphics.showline()
        self.graphics.showline()
        self.graphics.showline("#################################################")
        self.graphics.showline("Raiden")
        self.graphics.showline("WASD to control, space to shooot. Enter to start.")
        self.graphics.showline("You need to stay at least {0} seconds".format(duration))
        self.graphics.showline("#################################################")
        self.graphics.showline()
        self.graphics.showline()


    def refresh(self):
        self.array[self.x][self.y] = self.me
        Model.refresh(self)
    
    def getGraphics(self):
        return self.graphics
    def process(self, key):
        if not self.started:
            if (key == 10):
                self.startGame()
            return False
        if key in self.keyfn:
            self.keyfn[key]()
            self.refresh()
        if (self.x, self.y) in self.missles:
            self.lose()
            return True
        return False
    def up(self):
        if self.x - 1 >= 0:
            self.array[self.x][self.y] = self.empty
            self.x -= 1
            self.array[self.x][self.y] = self.me
    def down(self):
        if self.x + 1 < Graphics.DEFAULT_HEIGHT:
            self.array[self.x][self.y] = self.empty
            self.x += 1
            self.array[self.x][self.y] = self.me
    def left(self):
        if self.y - 1 >= 0:
            self.array[self.x][self.y] = self.empty
            self.y -= 1
            self.array[self.x][self.y] = self.me
    def right(self):
        if self.y + 1 < Graphics.DEFAULT_WIDTH:
            self.array[self.x][self.y] = self.empty
            self.y += 1
            self.array[self.x][self.y] = self.me
    def shoot(self):
        x = self.x - 1
        if x >=0:
            self.bullets.append((x, self.y))
    def startGame(self):
        self.started = True
        self.misslesEnd = False
        self.missles.append((0, self.y))
        self.starttime = now()
        self.refresh()
    def timeout(self):
        if not self.started:
            return False
        if len(self.missles) == 0:
            self.win()
            return True
        if now() - self.starttime > duration: #Duration 5 seconds
            self.stopMissles()
        if not self.misslesEnd:
            self.missles.append((0, r.randrange(Graphics.DEFAULT_WIDTH)))
            self.missles.append((0, self.y))
        newbullets = list()
        for (x, y) in self.bullets:
            self.array[x][y] = self.empty
            x -= 1
            if x >= 0:
                newbullets.append((x, y))
        self.bullets = newbullets
        newmissles = list()
        for (x, y) in self.missles:
            self.array[x][y] = self.empty
            if (x, y) not in self.bullets:
                x += 1
                if x < Graphics.DEFAULT_HEIGHT and (x, y) not in self.bullets:
                    newmissles.append((x, y))
            else:
                self.bullets.remove((x, y))
        self.missles = newmissles
        for (x, y) in self.bullets: self.array[x][y] = self.bullet
        for (x, y) in self.missles: self.array[x][y] = self.missle
        self.refresh()
        if (self.x, self.y) in self.missles:
            self.lose()
            return True
        return False
    
    def stopMissles(self):
        self.misslesEnd = True
    def win(self):
        self.nextModel = EndModel(self.ctrl, self.graphics)
    def lose(self):
        self.graphics.showline("You failed the test. Restarting...")
        self.nextModel = RaidenModel(self.ctrl, self.graphics, self.parent)
    def next(self):
        return self.nextModel
