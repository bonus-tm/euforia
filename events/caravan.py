# Модуль каравана
from event import Event

class Caravan(Event):
    """ Караван """
    
    def __init__(self, data, say, ask):
        self.probability = {
            'offer': 10,
            'rob': 30,
            'pillage': 40,
            'return': 20
        }
        self.profit_ratio_range = (6, 10)
        self.wandering = False
        self.year = 0
        self.investment = 0
        self.profit = 0
        
        super(Caravan, self).__init__(data, say, ask)
        
    #
    def invoke(self):
        """docstring for invoke"""
        
        if self.wandering:
            self.data.probability['Caravan'] = 100
        else:
            self.data.probability['Caravan'] = self.probability['offer']
        super().invoke()
    
    #   
    def start(self):
        """ Запуск события — отправка каравана либо продолжение похода, грабёж """
        
        self.debug("start: Year {:n}".format(self.year))
        if self.wandering:
            self.year += 1
            if self.ask.dice(self.probability['return']):
                self.comeback()
            elif self.ask.dice(self.probability['pillage']):
                self.pillage()
            elif self.ask.dice(self.probability['rob']):
                if self.investment > 3:
                    self.rob()
                else:
                    self.pillage()
        else:
            self.dispatch()
    
    #
    def dispatch(self):
        """ Отправить караван """
        
        self.say.line("Заморский купец предлагает снарядить караван.")
        if self.ask.yesno("Вы согласны?"):
            error = True
            while error:
                invest, error, msg = self.ask.number("В казне {:n} руб., сколько в караван?".format(self.data.money), self.data.money)
                if error:
                    self.say.line(msg)
                    
            if invest > 0:
                self.say.line("Караван отправился за три-девять земель.")
                self._go(invest)
            else:
                self.say.line("Караван ушёл в дальние страны без ваших товаров.")
        else:
            self.say.line("Караван ушёл в дальние страны без ваших товаров.")
    
    #
    def rob(self):
        """ Ограбление на сумму """
        
        rob = self.ask.rand(1, self.investment - 1)
        self.investment -= rob
        self.debug("rob, robbed={:n} investment={:n}".format(rob, self.investment))
        
        if self.let_messenger_in():
            self.say.line("Караван ограблен на сумму {:n} руб.".format(rob))
    
    #
    def pillage(self):
        """ Разграблен пиратами """
        
        self._stop()
        if self.let_messenger_in():
            self.say.line("Караван разграблен пиратами!")
    
    #
    def comeback(self):
        """ Вернулся караван """
        
        profit = self.year * self.investment * self.ask.rand(*self.profit_ratio_range)
        self.data.money += profit
        self.debug("comeback, years={:n} profit={:n} data.money={:n}".format(self.year, profit, self.data.money))
        self._stop()
        if self.let_messenger_in():
            self.say.line("Вернулся карван! Прибыль {:n} руб.".format(profit))
    
    #
    def let_messenger_in(self, introduction="Прибыл гонец с известиями, впустить?"):
        """ Гонец с известиями """
        
        return self.ask.yesno(introduction)
        
    #
    def _go(self, invest):
        """docstring for _go"""
        
        self.wandering = True
        self.year = 1
        self.investment = invest
        self.data.money -= invest
        
        self.debug("_go, investment={:n}, data.money={:n}".format(self.investment, self.data.money))
        
    #
    def _stop(self):
        """docstring for _stop"""
        
        self.wandering = False
        self.year = 0
        self.investment = 0
        self.profit = 0
        

