# Модуль наследства
import random
import data
from event import Event

class Inheritance(Event):
    """docstring for Inheritance"""
    
    def start(self):
        """docstring for start"""
        money = round(data.money * random.uniform(0.1, 2))
        resources = {
            'gold': round(data.resources['gold'] * random.uniform(0.1, 2)),
            'land': round(data.resources['land'] * random.uniform(0.1, 2)),
            'corn': round(data.resources['corn'] * random.uniform(0.1, 2)),
            'peasant': round(data.resources['peasant'] * random.uniform(0.1, 2)),
            'soldier': round(data.resources['soldier'] * random.uniform(0.1, 2))
        }
        
        say.line("\nВам досталось наследство:")
        data.print_small_table(money, resources)
        
        data.money += money
        data.resources['gold'] += resources['gold']
        data.resources['land'] += resources['land']
        data.resources['corn'] += resources['corn']
        data.resources['peasant'] += resources['peasant']
        data.resources['soldier'] += resources['soldier']
        
        
        