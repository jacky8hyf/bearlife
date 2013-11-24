from TextModel import TextModel
from ucb import trace
from readpic import readpic
class EndModel(TextModel):
    def __init__(self, ctrl, graphics):
        self.ctrl = ctrl
        self.graphics = graphics
        self.ctrl.setTimeOut(0.7)
        self.pic = readpic('ending');
        self.pic2 = readpic('ending');
        self.index = 0
        self.graphics.setPureScreen(self.pic[self.index:self.index+26] if self.index % 2 == 0 else self.pic2[self.index:self.index+26])
        self.refresh()
    
    def next(self):
        return None
    def timeout(self):
        self.index+=1
        if self.index + 26 <= len(self.pic):
            self.graphics.setPureScreen(self.pic[self.index:self.index+26] if self.index % 2 == 0 else self.pic2[self.index:self.index+26])
            self.refresh()
            return False
        else:
            return True
    
