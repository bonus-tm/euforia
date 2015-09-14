from debug import debug

class Event(object):
    """ События
    На каждой итерации (каждый год) вызывается метод invoke каждого события.
    Если срабатывает вероятность наступления этого события, то вызвать start.
    """
    
    def __init__(self, data, say, ask):
        self.data = data
        self.say = say
        self.ask = ask
    
    
    #
    def debug(self, msg):
        debug(msg, prefix=self.__class__.__name__)
    
    
    #
    def invoke(self):
        """ Вызывает запуск конкретного события """
        
        self.start()
    
    
    #
    def start(self):
        """ Запуск самого события """
        
        self.say.line("Event started")
