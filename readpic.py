from ucb import trace
def readpic(name):
    """ Return an array representing each pixel in the image file NAME:
    tens: 0: highlight, 1: does not highlight
    ones: the color.
    """
    filerows = list(open(name))
    arr = []
    i = 0
    for row in filerows:
        arr.append(list())
        for pixel in row.split(";"):
            arr[i].append(findnearest(tuple(map(int, pixel.split(",")))))
        i+=1
    return arr

#colors = [(0,0,0), (255,0,0), (0,255,0), (255,255,0), (0,0,255), (255,0,255), (0,255,255), (255,255,255)]
colors = [(10,10,10), (229,5,0), (31,232,23), (153,204,0), (0,23,182), (146,39,143), (0,209,192),(255,255,255)]
colors = [(i + 10, c) for (i, c) in enumerate(colors)] # not highlighted
color2 = [(153,153,155), (244,152,192), (42,239,133), (255,242,0), (128,113,204), (198,121,212), (129,219,238), (179,179,182)]
color2 = [(i, c) for (i, c) in enumerate(color2)] # highlighted
colors += color2


def findnearest(color):
    nearest = 255 * 3
    nearI = 0
    for (index, other) in colors:
        d = diff(color, other)
        if d < nearest:
            nearest = d
            nearI = index
    return nearI

def diff(c1, c2):
    sum = 0
    for i in range(len(c1)):
        sum += abs(c1[i] - c2[i])
    return sum
            
