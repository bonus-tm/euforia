import data, ask

class Event(object):
    """docstring for Event"""
    
    def __init__(self):
        super(Event, self).__init__()
    
    
    def invoke(self):
        """ Вызвать событие, если сработала вероятность """
        
        ev = self.__class__.__name__
        # print("DEBUG: invoking Event '{}', probability {}, dice {}"
        #       .format(ev, data.probability[ev], dice))
        if ask.dice(data.probability[ev]):
            self.start()
    
    
    def start(self):
        """docstring for start"""
        
        say.line("Event started")
    
    