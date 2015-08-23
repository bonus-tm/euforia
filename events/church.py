# митрополит
import random
import data, ask, act
from event import Event

class Church(Event):
    """ митрополит """
    
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
    
    
    def invoke(self):
        """docstring for invoke"""
        if data.money == 0:
            data.probability['Church'] = 0
        else:
            data.probability['Church'] = random.randrange(10, 50)
        super().invoke()
    
    
    def start(self):
        """  """
        print("Митрополит ожидает средства на постройку храма.")
        data.treasury()
        spend = ask.number("Сколько выделяете?", data.money)
        
        percent = spend / data.money * 100
        act.clear_screen()
        if percent > 40:
            print(random.choice(self.generous))
        elif percent > 20:
            print(random.choice(self.nice))
        else:
            print(random.choice(self.greedy))
        
        data.money -= spend
        self.money += spend
        
        self.build()
    
    
    def build(self):
        """docstring for build"""
        while self.money > self.price:
            print(" -=- Воздвигнут храм! -=-")
            self.money -= self.price
