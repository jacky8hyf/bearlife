from TextModel import TextModel
from RaidenModel import RaidenModel
class FootballWinModel(TextModel):
    def __init__(self, ctrl, graphics):
        TextModel.__init__(self, ctrl, graphics, [], 'pink')
    def next(self):
        return RaidenModel(self.ctrl, self.graphics)
