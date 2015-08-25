
class Event(object):
    """ События
    На каждой итерации (каждый год) вызывается метод invoke каждого события.
    Если срабатывает вероятность наступления этого события, то вызвать start.
    """
    
    def __init__(self, data, say, ask):
        self.data = data
        self.say = say
        self.ask = ask
    
    
    def invoke(self):
        """ Запускается каждый раз и проверяет вероятность события """
        
        ev = self.__class__.__name__
        # print("DEBUG: invoking Event '{}', probability {}, dice {}"
        #       .format(ev, data.probability[ev], dice))
        if self.ask.dice(self.data.probability[ev]):
            self.start()
    
    
    def start(self):
        """ Запуск самого события """
        
        self.say.line("Event started")
    
    