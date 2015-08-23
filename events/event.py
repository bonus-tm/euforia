import random
import data, ask

class Event(object):
    """docstring for Event"""
    
    def __init__(self):
        super(Event, self).__init__()
    
    
    def invoke(self):
        """docstring for invoke"""
        dice = random.randrange(100)
        ev = self.__class__.__name__
        # print("DEBUG: invoking Event '{}', probability {}, dice {}"
        #       .format(ev, data.probability[ev], dice))
        if dice < data.probability[ev]:
            self.start()
    
    
    def start(self):
        """docstring for start"""
        print("Event started")
    
    