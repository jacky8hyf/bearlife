from TextModel import TextModel
from FootballModel import Football
class ComplexPuzzleWinModel(TextModel):
    def __init__(self, ctrl, graphics):
        TextModel.__init__(self, ctrl, graphics, [], 'blue')
    def next(self):
        return Football(self.ctrl, self.graphics)
