from TextModel import TextModel
from SimplePuzzleModel import SimplePuzzleModel
class StartModel(TextModel):
    def __init__(self, ctrl, graphics):
        TextModel.__init__(self, ctrl, graphics, ["Welcome to Berkeley!", "This is a unique adventure.",
                "You will experience every aspect of life at Cal, Bearlife.",
                "...",
                "......",
                "Oops! You found yourself locked in Soda Hall, ...",
                "... and you need to go to Hilfinger's Lecture.",
                "...",
                "... which is in DWINELLE...",
                "FOUND YOUR WAY OUT of Soda!"
                ], 'title')
    def next(self):
        return SimplePuzzleModel(self.ctrl, self.graphics)
