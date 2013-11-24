import random
from Model import Model
from Graphics import Graphics
from FootballWinModel import FootballWinModel
from ucb import trace
class Football(Model):
    field = [
            Graphics.writeRow("                                                                                "),
            Graphics.writeRow("                                                                                "),
            Graphics.writeRow("                                                                                "),
            Graphics.writeRow("                                                                                "),
            Graphics.writeRow("                                                                                "),
            Graphics.writeRow("                                                                                "),
            Graphics.writeRow("                                                                                "),
            Graphics.writeRow("                                                                                "),
            Graphics.writeRow("                 #####        ######         ###         #                      "),
            Graphics.writeRow("                #            #      #       #   #        #                      "),
            Graphics.writeRow("                #   ###      #      #      #######       #                      "),
            Graphics.writeRow("                #     #      #      #      #     #       #                      "),
            Graphics.writeRow("                 ######       ######       #     #       ######                 "),
            Graphics.writeRow("|──────────────────────────────────────────────────────────────────────────────|"),
            Graphics.writeRow("|                  ──                                      ──                  |"),
            Graphics.writeRow("|                  ──                                      ──                  |"),
            Graphics.writeRow("|                  ──                                      ──                  |"),
            Graphics.writeRow("|                  ──                                      ──                  |"),
            Graphics.writeRow("|──────────────────────────────────────────────────────────────────────────────|"),
            Graphics.writeRow("|                  ──                                      ──                  |"),
            Graphics.writeRow("|                  ──                                      ──                  |"),
            Graphics.writeRow("|                  ──                                      ──                  |"),
            Graphics.writeRow("|                  10                                      10                  |"),
            Graphics.writeRow("|──────────────────────────────────────────────────────────────────────────────|"),
            Graphics.writeRow("|                  ──                                      ──                  |"),
            Graphics.writeRow("|                  ──                                      ──                  |"),
            Graphics.writeRow("|                  ──                                      ──                  |"),
            Graphics.writeRow("|                  ──                                      ──                  |"),
            Graphics.writeRow("|──────────────────────────────────────────────────────────────────────────────|"),
            Graphics.writeRow("|                  ──                                      ──                  |"),
            Graphics.writeRow("|                  ──                                      ──                  |"),
            Graphics.writeRow("|                  ──                                      ──                  |"),
            Graphics.writeRow("|                  20                                      20                  |"),
            Graphics.writeRow("|──────────────────────────────────────────────────────────────────────────────|"),
            Graphics.writeRow("|                  ──                                      ──                  |"),
            Graphics.writeRow("|                  ──                                      ──                  |"),
            Graphics.writeRow("|                  ──                                      ──                  |"),
            Graphics.writeRow("|                  ──                                      ──                  |"),
            Graphics.writeRow("|──────────────────────────────────────────────────────────────────────────────|"),
            Graphics.writeRow("|                  ──                                      ──                  |"),
            Graphics.writeRow("|                  ──                                      ──                  |"),
            Graphics.writeRow("|                  ──                                      ──                  |"),
            Graphics.writeRow("|                  30                                      30                  |"),
            Graphics.writeRow("|──────────────────────────────────────────────────────────────────────────────|"),
            Graphics.writeRow("|                  ──                                      ──                  |"),
            Graphics.writeRow("|                  ──                                      ──                  |"),
            Graphics.writeRow("|                  ──                                      ──                  |"),
            Graphics.writeRow("|                  ──                                      ──                  |"),
            Graphics.writeRow("|──────────────────────────────────────────────────────────────────────────────|"),
            Graphics.writeRow("|                  ──                                      ──                  |"),
            Graphics.writeRow("|                  ──                                      ──                  |"),
            Graphics.writeRow("|                  ──                                      ──                  |"),
            Graphics.writeRow("|                  40                                      40                  |"),
            Graphics.writeRow("|──────────────────────────────────────────────────────────────────────────────|"),
            Graphics.writeRow("|                  ──                                      ──                  |"),
            Graphics.writeRow("|                  ──                                      ──                  |"),
            Graphics.writeRow("|                  ──                                      ──                  |"),
            Graphics.writeRow("|                  ──                                      ──                  |"),
            Graphics.writeRow("|──────────────────────────────────────────────────────────────────────────────|"),
            Graphics.writeRow("|                  ──                                      ──                  |"),
            Graphics.writeRow("|                  ──                                      ──                  |"),
            Graphics.writeRow("|                  ──                                      ──                  |"),
            Graphics.writeRow("|                  50                                      50                  |"),
            Graphics.writeRow("|──────────────────────────────────────────────────────────────────────────────|"),
            Graphics.writeRow("|                  ──                                      ──                  |"),
            Graphics.writeRow("|                  ──                                      ──                  |"),
            Graphics.writeRow("|                  ──                                      ──                  |"),
            Graphics.writeRow("|                  ──                                      ──                  |"),
            Graphics.writeRow("|──────────────────────────────────────────────────────────────────────────────|"),
            Graphics.writeRow("|                  ──                                      ──                  |"),
            Graphics.writeRow("|                  ──                                      ──                  |"),
            Graphics.writeRow("|                  ──                                      ──                  |"),
            Graphics.writeRow("|                  40                                      40                  |"),
            Graphics.writeRow("|──────────────────────────────────────────────────────────────────────────────|"),
            Graphics.writeRow("|                  ──                                      ──                  |"),
            Graphics.writeRow("|                  ──                                      ──                  |"),
            Graphics.writeRow("|                  ──                                      ──                  |"),
            Graphics.writeRow("|                  ──                                      ──                  |"),
            Graphics.writeRow("|──────────────────────────────────────────────────────────────────────────────|"),
            Graphics.writeRow("|                  ──                                      ──                  |"),
            Graphics.writeRow("|                  ──                                      ──                  |"),
            Graphics.writeRow("|                  ──                                      ──                  |"),
            Graphics.writeRow("|                  30                                      30                  |"),
            Graphics.writeRow("|──────────────────────────────────────────────────────────────────────────────|"),
            Graphics.writeRow("|                  ──                                      ──                  |"),
            Graphics.writeRow("|                  ──                                      ──                  |"),
            Graphics.writeRow("|                  ──                                      ──                  |"),
            Graphics.writeRow("|                  ──                                      ──                  |"),
            Graphics.writeRow("|──────────────────────────────────────────────────────────────────────────────|"),
            Graphics.writeRow("|                  ──                                      ──                  |"),
            Graphics.writeRow("|                  ──                                      ──                  |"),
            Graphics.writeRow("|                  ──                                      ──                  |"),
            Graphics.writeRow("|                  20                                      20                  |"),
            Graphics.writeRow("|──────────────────────────────────────────────────────────────────────────────|"),
            Graphics.writeRow("|                  ──                                      ──                  |"),
            Graphics.writeRow("|                  ──                                      ──                  |"),
            Graphics.writeRow("|                  ──                                      ──                  |"),
            Graphics.writeRow("|                  ──                                      ──                  |"),
            Graphics.writeRow("|──────────────────────────────────────────────────────────────────────────────|"),
            Graphics.writeRow("|                  ──                                      ──                  |"),
            Graphics.writeRow("|                  ──                                      ──                  |"),
            Graphics.writeRow("|                  ──                                      ──                  |"),
            Graphics.writeRow("|                  10                                      10                  |"),
            Graphics.writeRow("|──────────────────────────────────────────────────────────────────────────────|"),
            Graphics.writeRow("|                  ──                                      ──                  |"),
            Graphics.writeRow("|                  ──                                      ──                  |"),
            Graphics.writeRow("|                  ──                                      ──                  |"),
            Graphics.writeRow("|                  ──                                      ──                  |"),
            Graphics.writeRow("|──────────────────────────────────────────────────────────────────────────────|"),
            Graphics.writeRow("|                                                                              |"),
            Graphics.writeRow("|                                                                              |"),
            Graphics.writeRow("|                                                                              |"),
            Graphics.writeRow("|                                                                              |"),
            Graphics.writeRow("|                                                                              |"),
            Graphics.writeRow("|                                                                              |"),
            Graphics.writeRow("|                                                                              |"),
            Graphics.writeRow("|                                                                              |"),
            Graphics.writeRow("|                                                                              |"),
            Graphics.writeRow("|                                                                              |"),
            Graphics.writeRow("|                                                                              |"),
            Graphics.writeRow("|                                                                              |"),
            Graphics.writeRow("|                                                                              |"),
            ]

    def __init__(self, ctrl, graphics):
        self.started = False
        self.ballCaught = False
        self.blink = False
        self.won = False
        self.ctrl = ctrl
        self.graphics = graphics
        self.graphics.clear()
        self.ctrl.setTimeOut(0.4)
        self.dic = {10:self.start}
        self.x = 40
        self.y = 108
        self.opponent = []
        self.band = []
        while len(self.opponent) <= 11:
            t = (random.randint(0, 40), random.randint(24, 94))
            if t not in self.opponent and t not in self.band:
                self.opponent.append(t)
        while len(self.band) <= 30:
            t = (random.randint(20, 40), random.randint(24, 64))
            if t not in self.opponent and t not in self.band:
                self.band.append(t)

    def up(self):
        if self.y == 13:
            self.graphics.clear()
            self.graphics.showline("You Win!!!")
            self.won = True
            return True
        for one in self.opponent:
            if(Football.touches((self.x, self.y - 1), one)):
                self.graphics.clear()
                self.graphics.showline("You ran into an opponent's arm!!!")
                return True
        for one in self.band:
            if(Football.touches((self.x, self.y - 1), one)):
                self.graphics.clear()
                self.graphics.showline("You ran into an band member's arm!!!")
                return True
        self.y -= 1
        self.update(move = False)
    def down(self):
        if self.y >= 111:
            return False
        for one in self.opponent:
            if(Football.touches((self.x, self.y), one)):
                self.graphics.clear()
                self.graphics.showline("You ran into an opponent's arm!!!")
                return True
        for one in self.band:
            if(Football.touches((self.x, self.y), one)):
                self.graphics.clear()
                self.graphics.showline("You ran into an band member's arm!!!")
                return True
        self.y += 1
        self.update(move = False)
    def left(self):
        if self.x <= 1:
            return False
        for one in self.opponent:
            if(Football.touches((self.x, self.y), one)):
                self.graphics.clear()
                self.graphics.showline("You ran into an opponent's arm!!!")
                return True
        for one in self.band:
            if(Football.touches((self.x, self.y), one)):
                self.graphics.clear()
                self.graphics.showline("You ran into an band member's arm!!!")
                return True
        self.x -= 1
        self.update(move = False)
    def right(self):
        if self.x >= 79:
            return False
        for one in self.opponent:
            if(Football.touches((self.x, self.y), one)):
                self.graphics.clear()
                self.graphics.showline("You ran into an opponent's arm!!!")
                return True
        for one in self.band:
            if(Football.touches((self.x, self.y), one)):
                self.graphics.clear()
                self.graphics.showline("You ran into an band member's arm!!!")
                return True
        self.x += 1
        self.update(move = False)

    def timeout(self):
        self.graphics.refresh()
        self.graphics.showline("Welcome to the California Memorial Stadium !!!")
        self.graphics.showline("Today is November the 20th, 1982.")
        self.graphics.showline("You(^) need to get to the other end of the field")
        self.graphics.showline("while avoiding the opponent($)... And the Stanford Band(∮)... ...")
        if self.blink:
            self.graphics.showline("Use W,A,D to control, press         to begin.")
        else:
            self.graphics.showline("Use W,A,D to control, press [ENTER] to begin.")
        self.blink = not self.blink

    def update(self, move = True):
        self.graphics.array = Football.cloneField()
        opp_ref = list(self.opponent)
        for _ in opp_ref:
            one = tuple(_)
            if move:
                if (one[0] > self.x):
                    one = (one[0] - 1, one[1])
                if (one[0] < self.x):
                    one = (one[0] + 1, one[1])
                if (one[1] > self.y):
                    one = (one[0], one[1] - 1)
                if (one[1] < self.y):
                    one = (one[0], one[1] + 1)
                if (Football.touches((self.x, self.y), one)):
                    self.graphics.clear()
                    self.graphics.showline("An opponent team member caught you!!!")
                    return True
                if one not in self.opponent and one not in self.band:
                    self.opponent.remove(_)
                    self.opponent.append(one)
            self.graphics.array[one[1]][one[0]] = ('$', Graphics.RED)
        bd_ref = list(self.band)
        for _ in bd_ref:
            one = tuple(_)
            if move:
                one = (one[0] + random.randint(-1,1), one[1] + random.randint(-1,1))
                if 0 <= one[0] < 40 and 40 <= one[1] < 108 and one not in self.band and one not in self.opponent and one != (self.x, self.y):
                    self.band.remove(_)
                    self.band.append(one)
            self.graphics.array[one[1]][one[0]] = ('∮', Graphics.YELLOW)
        self.graphics.array = self.graphics.array[self.y - Graphics.DEFAULT_HEIGHT // 2 : self.y + Graphics.DEFAULT_HEIGHT // 2]
        self.graphics.array[Graphics.DEFAULT_HEIGHT // 2 - 1][self.x] = ('^', Graphics.CYAN)
        self.graphics.refresh()

    def cloneField():
        return [list(row) for row in Football.field]

    def touches(p1, p2):
        if p1[0] == p2[0]:
            if abs(p1[1] - p2[1]) <= 1:
                return True
        if p1[1] == p2[1]:
            if abs(p1[0] - p2[0]) <= 1:
                return True
        return False

    def start(self):
        if not self.started:
            self.dic = {10:self.start, 119:self.up, 97:self.left, 100:self.right, 115:self.down}
            self.timeout = self.update
            self.started = True
    def process(self, key):
        if key in self.dic:
            return self.dic[key]()
    def next(self):
        if self.won:
            return FootballWinModel(self.ctrl, self.graphics)
        return Football(self.ctrl, self.graphics)
