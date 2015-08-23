# Распределение зерна на еду и на посев
import re
import data, ask, act
from event import Event

class Distribute(Event):
    """docstring for Distribute"""
    
    def start(self):
        """docstring for start"""
        self.min_for_food = data.resources['peasant'] + data.resources['soldier'] + 1
        self.min_for_seed = min(data.resources['peasant'], data.resources['land'])
    
        if ask.yesno("Желаете сами распорядиться запасами зерна?") \
           or self.min_for_food + self.min_for_seed > data.resources['corn']:
               self.manually()
               msg = "Остаток зерна в амбарах: {:>10n} тонн"
        else:
            self.automatically()
            msg = "Излишки зерна в амбарах: {:>10n} тонн"
        
        data.resources['corn'] -= data.corn_for_food
        data.resources['corn'] -= data.corn_for_seed
        print(msg.format(data.resources['corn']))
    
    
    def automatically(self):
        """ Дефолтная раздача """
        
        data.corn_for_food = self.min_for_food
        data.corn_for_seed = self.min_for_seed
        act.erase_line()
        print("--> Выделена норма: {:>10n} тонн зерна".format(self.min_for_food + self.min_for_seed))
        
    
    def manually(self):
        """ Сколько зерна на еду, сколько на посев """
        
        got_distribution = False
        while not got_distribution:
            act.erase_line()
            print("Сколько тонн зерна на еду, сколько на посев? ", end='')
            answer = re.split('[^0-9]+', input().strip())
            if answer[0].isnumeric() and answer[1].isnumeric():
                data.corn_for_food = int(answer[0])
                data.corn_for_seed = int(answer[1])
                if data.corn_for_food + data.corn_for_seed <= data.resources['corn']:
                    got_distribution = True
