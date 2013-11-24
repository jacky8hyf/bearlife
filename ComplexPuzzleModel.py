from PuzzleModel import PuzzleModel
from ComplexPuzzleWinModel import ComplexPuzzleWinModel
from Graphics import Graphics
class ComplexPuzzleModel(PuzzleModel):
    def __init__(self, ctrl, graphics):
        arr = list(open('maps'))
        arr = [list(s.replace('\n','')) for s in arr]
        PuzzleModel.__init__(self, ctrl, graphics, arr,12, 36,25, 72)
    def next(self):
        return ComplexPuzzleWinModel(self.ctrl, self.graphics)
    def process(self, key):
        if (key == ord('p')):
            self.graphics.array[self.x][self.y] = (Graphics.EMPTY, Graphics.WHITE)
            self.x = self.endX - 1
            self.y = self.endY
            self.graphics.array[self.x][self.y] = (self.hero, self.herocolor)
            self.refresh()
            return False
        else: return PuzzleModel.process(self, key)
