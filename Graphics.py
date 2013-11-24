
import sys
import os
from ucb import trace
class Graphics:
    DEFAULT_WIDTH = 80
    DEFAULT_HEIGHT = 26
    BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE = range(8)
    BG_BLACK = 8
    BG_NO_COLOR = 0
    EMPTY = ' '
    FULL = '█'
    BOTTOM = "▄"
    
    def writeRow(s = EMPTY, color = WHITE):
        return [(c, color) for c in s]

    def __init__(self, array = [[]]): #, colormap):
        """
        hundreds: highlight
        tens: background
        ones: foreground
        """
        self.array = array
        #self.colormap = colormap
    
    def setPureScreen(self, array = [[]], double = False):
        """
        Array is a one color per cell array, shown as background color.
        """
        if double:
            result = []
            for r in range(0, len(array), 2):
                result.append(list())
                for c in range(len(array[r])):
                    bg = array[r][c] % 10 # does not support highlight
                    bg = Graphics.BG_BLACK if bg == Graphics.BLACK else bg
                    result[r // 2].append((Graphics.BOTTOM, bg * 9 + array[r+1][c]))
            self.array = result
        else:    
#            self.array = [[(Graphics.EMPTY, (c // 10) * 81 + (c % 10 if c % 10 != Graphics.BLACK else Graphics.BG_NO_COLOR) * 9) for c in row] for row in array]
            self.array = [[(Graphics.FULL, (c // 10) * 81 + (c % 10)) for c in row] for row in array]

    def clear(self):
        self.array = []
        for i in range(Graphics.DEFAULT_HEIGHT):
            self.array.append([])
            for j in range(Graphics.DEFAULT_WIDTH):
                self.array[i].append((" " , Graphics.WHITE))
        self.refresh()

    def refresh(self):
        """
        Display the array on screen.
        """
        def draw(ch, color):
            """ Color the character c.
            ch: a (string with only one) character.
            Color: an integer.
            """
            highlight = color // 81
            bg = color % 81 // 9
            return "\x1b["+(
                ("1;"+str(color + 30)) if color < 9 \
                else ("1;" if highlight == 0 else "")+
                    (str((Graphics.BLACK if bg == Graphics.BG_BLACK else bg) + 40) + ";" if bg != Graphics.BG_NO_COLOR else "")
                    +str(color % 9 + 30)
                )+"m"+ch+"\x1b[0m"
        height = len(self.array)
        width = len(self.array[0])
        luX = (Graphics.DEFAULT_WIDTH - width) // 2
        luY = (Graphics.DEFAULT_HEIGHT - height) // 2
        # CLEAN SCREEN HERE
        os.system('clear')
        for _ in range(luY - 1): sys.stdout.write("\n")
        x = 0
        for row in self.array:
            sys.stdout.write("\n")
            s = " " * luX
            y = 0
            for (ch, color) in row:
                s += draw(ch, color)
                y += 1
            sys.stdout.write(s)
            x += 1
        for _ in range(Graphics.DEFAULT_HEIGHT - luY - height): sys.stdout.write("\n")
        sys.stdout.flush()
    
    def showline(self, line = ""):
        print(line)
