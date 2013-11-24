from SimplePuzzleModel import SimplePuzzleModel 
from StartModel import StartModel
from EndModel import EndModel
from FootballModel import Football
from ComplexPuzzleModel import ComplexPuzzleModel
from RaidenModel import RaidenModel
from Graphics import Graphics
from datetime import datetime
from ucb import trace
from datetime import datetime
from time import time as now
import time
from threading import Thread
import threading
import sys

REFRESH = 0.05 # FIXME Change to 0.01
class Controller:
    def __init__(self):
        Controller.static_ctrl = self
        Controller.static_end = False
        self.graphics = Graphics()
        self.model = StartModel(self, self.graphics) # FIXME change to Start a different Model
        assert hasattr(self, 'timeout'), "Model does not call setTimeOut()"
        self.timestamp = now() # in seconds
        Input().start() # Thread 2
        while True: # Thread 1
            if (Controller.static_end): break
            time.sleep(REFRESH)
            if(now() - self.timestamp > self.timeout):
                if(self.model.timeout()):
                    self.model = self.model.next()
                if (self.model == None):
                    Controller.static_end = True
                    exit()
                self.timestamp = now();

    def pressed(self, key):
        """
        Invoked when Input thread gets an keystroke. key is an integer representing the key pressed. 
        """
        if(self.model.process(key)):
            self.model = self.model.next()
        if (self.model == None):
            Controller.static_end = True
            exit()
        #self.timestamp = now();
    
    def setTimeOut(self,timeout):
        self.timeout = timeout

class Input(Thread):

    def run(self):
        while True: 
            if (Controller.static_end): break
            Controller.static_ctrl.pressed(getchar())

        
def getchar():
    import termios, sys, os
    """ Return a integer corresponding to the character just read. """
    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)
    new = termios.tcgetattr(fd)
    new[3] = new[3] & ~termios.ICANON & ~termios.ECHO
    new[6][termios.VMIN] = 1
    new[6][termios.VTIME] = 0
    termios.tcsetattr(fd, termios.TCSANOW, new)
    c = None
    try:
        c = os.read(fd, 1)
    finally:
        termios.tcsetattr(fd, termios.TCSAFLUSH, old)
    return c[0]
