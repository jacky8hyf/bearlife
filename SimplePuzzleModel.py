from PuzzleModel import PuzzleModel
from SimplePuzzleWinModel import SimplePuzzleWinModel
class SimplePuzzleModel(PuzzleModel):
    def __init__(self, ctrl, graphics):
        arr = [list('██████████████████████████████████████████'),
               list('█      █           █      █              █'),
               list('█      █   █████████   █  █   █████      █'),
               list('█                      █      █           '),
               list('██████████████████████████████████████████') 
        ]
        PuzzleModel.__init__(self, ctrl, graphics, arr,1,1,3, 41)
    def next(self):
        return SimplePuzzleWinModel(self.ctrl, self.graphics)
    
