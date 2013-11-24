from Model import Model
from Graphics import Graphics
from readpic import readpic
class TextModel(Model):
    """ Should be an abstraction class. """
    def __init__(self, ctrl, graphics, sentences, img):
        self.ctrl = ctrl
        self.graphics = graphics
        self.ctrl.setTimeOut(100)
        self.sentences = sentences
        self.sentenceNum = 0
        self.graphics.setPureScreen(readpic(img))
        self.refresh()
    def process(self, key):
        if self.sentenceNum >= len(self.sentences):
            return True
        if key == 10:
            self.showWords()
        return False
    def timeout(self):
        return False
    
    def showWords(self):
        arr = self.graphics.array
        l = len(arr)
        W = len(arr[0])
        sentence = self.sentences[self.sentenceNum]
        arr[l - 5] = [(c, Graphics.WHITE) for c in ("#" * W)]
        arr[l - 4] = [(c, Graphics.WHITE) for c in ("#" + " "* (W - 3) +" #")]
        arr[l - 3] = [(c, Graphics.WHITE) for c in ("# "+ sentence + " "*(W - 4 - len(sentence))+" #")]
        arr[l - 2] = [(c, Graphics.WHITE) for c in ("#" + " "* (W - 3) +" #")]
        arr[l - 1] = [(c, Graphics.WHITE) for c in ("#" * W)]
        self.sentenceNum+=1
        self.refresh()

