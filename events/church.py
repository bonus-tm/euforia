# Митрополит
import data, ask, say, act
from event import Event

class Church(Event):
    """ Митрополит """
    
    money = 0
    buildings = 0
    price = 100000
    
    generous = [
        'Всевышний благословит ваше правление на долгие годы!',
        'Во всех храмах служат здравицу великому королю!',
        'Слава королю, щедрому и мудрому правителю!'
    ]
    nice = ['Вы чрезмерно скупы, ваше величество!']
    greedy = ['Вы что, насмехаетесь?! Скряга!']
    
    #
    def invoke(self):
        """docstring for invoke"""
        if data.money == 0:
            data.probability['Church'] = 0
        else:
            data.probability['Church'] = ask.rand(10, 50)
        super().invoke()
    
    #
    def start(self):
        """ Выделение средств на храм """
        say.line("Митрополит ожидает средства на постройку храма.")
        data.treasury()
        error = True
        while error:
            spend, error, msg = ask.number("Сколько выделяете?", data.money)
            if error:
                say.line(msg)
        
        percent = spend / data.money * 100
        act.clear_screen()
        if percent > 40:
            say.line(ask.choice(self.generous))
        elif percent > 20:
            say.line(ask.choice(self.nice))
        else:
            say.line(ask.choice(self.greedy))
        
        data.money -= spend
        self.money += spend
        
        self.build()
    
    #
    def build(self):
        while self.money > self.price:
            say.line(" -=- Воздвигнут храм! -=-")
            self.money -= self.price
