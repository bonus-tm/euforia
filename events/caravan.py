# Модуль каравана
import data, ask
from event import Event


class Caravan(Event):
    """ Караван """
    
    probability = {
        'offer': 30,
        'rob': 30,
        'pillage': 40,
        'return': 20
    }
    profit_ratio_range = (6, 10)
    dispatched = False
    year = 0
    money = 0
    profit = 0
    
    #
    def invoke(self):
        """docstring for invoke"""
        
        if self.dispatched:
            data.probability['Caravan'] = 100
        else:
            self.probability['Caravan'] = self.probability['offer']
        super().invoke()
    
    #   
    def start(self):
        """docstring for start"""
        
        if self.dispatched:
            self.year += 1
            if ask.dice(self.probability['return']):
                self.comeback()
            else:
                if ask.dice(self.probability['pillage']):
                    self.pillage()
                elif ask.dice(self.probability['rob']):
                    self.rob()
        else:
            self.dispatch()
        
    #
    def dispatch(self):
        """ Отправить караван """
        
        say.line("Заморский купец предлагает снарядить караван.")
        if ask.yesno("Вы согласны?"):
            error = True
            while error:
                spend, error, msg = ask.number("В казне {:n} руб., сколько в караван?".format(data.money), data.money)
                if error:
                    say.line(msg)
                    
            if spend > 0:
                say.line("Караван отправился за три-девять земель.")
                self.dispatched = True
                self.year = 1
                self.money = spend
                data.money -= spend
            else:
                say.line("Караван ушёл в дальние страны без ваших товаров.")
        else:
            say.line("Караван ушёл в дальние страны без ваших товаров.")
    
    #
    def rob(self):
        """ Ограбление на сумму """
        
        rob = ask.rand(1, self.money - 1)
        self.money -= rob
        if ask.let_messenger_in():
            say.line("Караван ограблен на сумму {:n} руб.".format(rob))
    
    #
    def pillage(self):
        """ Разграблен пиратами """
        
        self._stop()
        if ask.let_messenger_in():
            say.line("Караван разграблен пиратами!")
    
    #
    def comeback(self):
        """ Вернулся караван """
        
        profit = self.year * self.money * ask.rand(*profit_ratio_range)
        data.money += profit
        self._stop()
        if ask.let_messenger_in():
            say.line("Вернулся карван! Прибыль {:n} руб.".format(profit))
    
    #
    def _stop(self):
        """docstring for _stop"""
        
        self.year = 0
        self.money = 0
        self.profit = 0
        self.dispatched = False
        

