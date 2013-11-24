from Graphics import Graphics
from ucb import trace
class Model:
    """ Game logic. Change self.key_funcs when need to map new keys. Change self.graphics.array when need to
    change graphical display. 
    
    This is an abstract class. Please do not initialize a Model object; instead, extend it.
    """
    def __init__(self, ctrl, graphics):
        """ Init. Should call ctrl.setTimeOut()."""
        raise Exception("Model cannot be initialized.")

    def refresh(self):
        """
        Refreshes the screen.
        """
        self.graphics.refresh()
    
    def get_Graphics(self):
        """ Return a Graphics object describing the current Graphics. """
        return self.graphics
   
    def process(self, key):
        """ invoked when KEY is pressed. Return true if the model finishes, false otherwise."""
        raise Exception("{0} did not override process.".format(self))
        
    def timeout(self):
        """ invoked when time out. Return true if the model finishes, false otherwise."""
        raise Exception("{0} did not override timeout.".format(self))
    
    def next(self):
        """Return the next model. """
        raise Exception("{0} did not override next.".format(self))
