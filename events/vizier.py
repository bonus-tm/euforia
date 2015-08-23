# Визирь
import random
import data, ask, act
from event import Event

class Vizier(Event):
    """docstring for Vizier"""
    
    def start(self):
        """docstring for start"""
        # довольствие армии
        data.deserters = 0
        data.allowance = data.resources['soldier'] * 10
        if data.allowance > data.money:
            shortage = data.allowance - data.money
            data.allowance = data.money
            data.deserters = min(round(shortage / 10 * random.uniform(0, 1.5)),
                                 data.resources['soldier'])
        data.money -= data.allowance
        data.resources['soldier'] -= data.deserters
        
        sldr = data.resources['soldier']
        psnt = data.resources['peasant']
        
        # население
        data.births = 0
        data.famishes = 0
        data.fugitives = 0
        if psnt + sldr > data.corn_for_food:
            shortage = psnt + sldr - data.corn_for_food
            data.famishes = round(shortage * random.uniform(0.3, 1))
        data.resources['peasant'] -= data.famishes
            
        if psnt > min(data.corn_for_seed, data.resources['land']):
            shortage = psnt - min(data.corn_for_seed, data.resources['land'])
            data.fugitives = min(round(shortage * random.uniform(0, 1.2)),
                                 data.resources['peasant'],)
        data.resources['peasant'] -= data.fugitives
        
        data.births = round(data.resources['peasant'] * random.uniform(0.05, 0.4))
        data.resources['peasant'] += data.births
        
        # крысы пожрали зерно
        data.rats_eat = 0
        dice = random.randrange(100)
        if dice < 50:
            data.rats_eat = round(data.resources['corn'] * random.uniform(0.1, 0.9))
        
        # урожай
        data.resources['corn'] += round(data.corn_for_seed * data.crop_rate)
        
        
        # настроения народа
        # стихийные бедствия
        # визирь украл и скрылся
        # ограбление каравана
        # ограблен храм
        
        if ask.let_messenger_in("Ваше высочество! Прибыл визирь, впустить?"):
            act.clear_screen()
            print("Жалованье солдат: {:>10n} руб.\n".format(data.allowance) +
                  "-----------------------------------------------------------------------")
            
            act.debug("на еду {:n}, на посев {:n} × {:.3} = урожай {:n} тонн, итого {:n}"
                      .format(data.corn_for_food,
                              data.corn_for_seed,
                              data.crop_rate,
                              round(data.corn_for_seed * data.crop_rate),
                              data.resources['corn']))
            
            if data.rats_eat:
                print(" - Крысы сожрали {:>10n} тонн зерна.".format(data.rats_eat))
            
            if data.deserters:
                print(" - Гвардия не получила денежного довольствия.\n" +
                      " {:>10n} солдат покинули казармы и ушли за кордон.".format(data.deserters))
            if data.fugitives:
                print(" - Рабочим не хватает земли. Сбежало {:>10n} человек.".format(data.fugitives))
            if data.famishes:
                print(" - Вы заморили голодом {:>10n} ваших верноподданных!".format(data.famishes))
            if data.births:
                print(" - В государстве родилось {:>10n} детей.".format(data.births))
            # if data.:
                # print(" -  {:>10n} \n".format(data.))
            print()
            
        
        
        
        