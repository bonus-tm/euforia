# Модуль каравана
import random
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
    dispatched = False
    year = 0
    money = 0
    profit = 0
    
    def invoke(self):
        """docstring for invoke"""
        if self.dispatched:
            data.probability['Caravan'] = 100
        else:
            self.probability['Caravan'] = self.probability['offer']
        super().invoke()
    
        
    def start(self):
        """docstring for start"""
        if self.dispatched:
            self.year += 1
            dice = random.randrange(100)
            if dice < self.probability['return']:
                self.comeback()
            else:
                dice = random.randrange(100)
                if dice < self.probability['pillage']:
                    self.pillage()
                else:
                    dice = random.randrange(100)
                    if dice < self.probability['rob']:
                        self.rob()
        else:
            self.dispatch()
        
    
    def dispatch(self):
        """Отправить караван"""
        print("Заморский купец предлагает снарядить караван.")
        if ask.yesno("Вы согласны?"):
            print("В казне {:n} руб., сколько в караван?".format(data.money), end='')
            spend = ask.number('', data.money)
            if spend > 0:
                print("Караван отправился за три-девять земель.")
                self.dispatched = True
                self.year = 1
                self.money = spend
                data.money -= spend
            else:
                print("Караван ушёл в дальние страны без ваших товаров.")
        else:
            print("Караван ушёл в дальние страны без ваших товаров.")
    
    
    def rob(self):
        """Ограбление на сумму"""
        rob = random.randrange(1, self.money - 1)
        self.money -= rob
        if self.let_messenger_in():
            print("Караван ограблен на сумму {:n} руб.".format(rob))
    
    
    def pillage(self):
        """Разграблен пиратами"""
        self._stop()
        if self.let_messenger_in():
            print("Караван разграблен пиратами!")
    
    
    def comeback(self):
        """Вернулся караван"""
        profit = self.year * self.money * random.randrange(6, 10)
        data.money += profit
        self._stop()
        if ask.let_messenger_in():
            print("Вернулся карван! Прибыль {:n} руб.".format(profit))
    
        
    def _stop(self):
        """docstring for _stop"""
        self.year = 0
        self.money = 0
        self.profit = 0
        self.dispatched = False
        
