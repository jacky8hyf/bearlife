from TextModel import TextModel
from ComplexPuzzleModel import ComplexPuzzleModel   
class SimplePuzzleWinModel(TextModel):
    def __init__(self, ctrl, graphics):
        TextModel.__init__(self, ctrl, graphics, [], 'red')
    def next(self):
        return ComplexPuzzleModel(self.ctrl, self.graphics)
