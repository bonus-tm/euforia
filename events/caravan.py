# Модуль каравана
from event import Event


class Caravan(Event):
    """ Караван """
    
    def __init__(self, data, say, ask):
        self.probability = {
            'offer': 99,
            'rob': 30,
            'pillage': 40,
            'return': 20
        }
        self.profit_ratio_range = (6, 10)
        self.dispatched = False
        self.year = 0
        self.money = 0
        self.profit = 0
        
        super(Caravan, self).__init__(data, say, ask)
    
    #
    def invoke(self):
        """docstring for invoke"""
        
        if self.dispatched:
            self.data.probability['Caravan'] = 100
        else:
            self.data.probability['Caravan'] = self.probability['offer']
        super().invoke()
    
    #   
    def start(self):
        """ Запуск события — отправка каравана либо продолжение похода, грабёж """
        
        if self.dispatched:
            self.year += 1
            if self.ask.dice(self.probability['return']):
                self.comeback()
            else:
                if self.ask.dice(self.probability['pillage']):
                    self.pillage()
                elif self.ask.dice(self.probability['rob']):
                    self.rob()
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
        
        rob = self.ask.rand(1, self.money - 1)
        self.money -= rob
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
        
        profit = self.year * self.money * self.ask.rand(*self.profit_ratio_range)
        self.data.money += profit
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
        
        self.dispatched = True
        self.year = 1
        self.money = invest
        self.data.money -= invest
        
    #
    def _stop(self):
        """docstring for _stop"""
        
        self.dispatched = False
        self.year = 0
        self.money = 0
        self.profit = 0
        

