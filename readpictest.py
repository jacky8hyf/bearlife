from readpic import readpic
from Graphics import Graphics
g = Graphics()

def s(path):
    arr = readpic(path)
    g.setPureScreen(arr)
    g.refresh() 
