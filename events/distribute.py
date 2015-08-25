# Распределение зерна на еду и на посев
import re
import data, ask, act
from event import Event

class Distribute(Event):
    """Распределение зерна"""
    
    #
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
        say.line(msg.format(data.resources['corn']))
    
    #
    def automatically(self):
        """ Дефолтная раздача """
        
        data.corn_for_food = self.min_for_food
        data.corn_for_seed = self.min_for_seed
        say.erase_line()
        say.line("--> Выделена норма: {:>10n} тонн зерна".format(self.min_for_food + self.min_for_seed))
        
    #
    def manually(self):
        """ Сколько зерна на еду, сколько на посев """
        
        [data.corn_for_food, data.corn_for_seed] = ask.corn(data.resources['corn'])
    
    
    #
    def corn(max, input_func=default_input_func, try_once=False):
        """ Сколько зерна на еду, сколько на посев """
    
        done = False
        while not done:
            erase_line()
            say.word("Сколько тонн зерна на еду, сколько на посев?")
            answer = re.findall('[0-9]+', input_func())
        
            try:
                food = int(answer[0])
                seed = int(answer[1])
            
                if food > max:
                    done = try_once
                    food = -1
                    seed = -1
                elif food + seed > max:
                    done = True
                    seed = max - food
                else:
                    done = True
            except ValueError:
                done = try_once
            
        return [food, seed]
        
