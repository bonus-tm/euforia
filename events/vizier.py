# Визирь
from event import Event

class Vizier(Event):
    """ Визирь
    Армия: довольствие, дезертиры
    Население: рождаемость, смертность, недовольство, голод
    Урожай: засухи-наводнения, урожайность, крысы
    Визирь: украл золото и скрылся
    """
    
    def __init__(self, data, say, ask):
        self.data = data
        self.say = say
        self.ask = ask
    
    
    #
    def start(self):
        """ Запуск события — пересчёт параметров и вывод результатов """
        
        self.check_army()
        self.check_population()
        self.check_crop()
        self.check_rob_caravan()
        self.check_rob_church()
        self.check_vizier()
        
        if self.let_him_in():
            self.report()
        
        
    # довольствие армии
    def check_army(self):
        # дезертиры
        self.data.deserters = 0
        # денежное довольствие армии
        self.data.allowance = self.data.resources['soldier'] * 10
        
        # считаем дезертировавших из-за невыплаты довольствия
        if self.data.allowance > self.data.money:
            shortage = self.data.allowance - self.data.money
            self.data.allowance = self.data.money
            self.data.deserters = min(round(shortage / 10 * self.ask.frand(0, 1.5)),
                                      self.data.resources['soldier'])
        self.data.money -= self.data.allowance
        self.data.resources['soldier'] -= self.data.deserters
        
        
    # население
    # настроения народа
    def check_population(self):
        # родилось
        self.data.births = 0
        # померло от голода
        self.data.famishes = 0
        # сбежало
        self.data.fugitives = 0
        
        sldr = self.data.resources['soldier']
        psnt = self.data.resources['peasant']
        
        # считаем скольким хватило зерна на прокорм, а сколько рабочих померло с голодухи
        if psnt + sldr > self.data.corn_for_food:
            shortage = psnt + sldr - self.data.corn_for_food
            self.data.famishes = round(shortage * self.ask.frand(0.3, 1))
        self.data.resources['peasant'] -= self.data.famishes
        
        # считаем рабочих, сбежавших от нехватки земли
        if psnt > min(self.data.corn_for_seed, self.data.resources['land']):
            shortage = psnt - min(self.data.corn_for_seed, self.data.resources['land'])
            self.data.fugitives = min(round(shortage * self.ask.frand(0, 1.2)),
                                      self.data.resources['peasant'],)
        self.data.resources['peasant'] -= self.data.fugitives
        
        # эпидемия чумы
        
        # остальные размножаются
        self.data.births = round(self.data.resources['peasant'] * self.ask.frand(0.05, 0.4))
        self.data.resources['peasant'] += self.data.births
        
        # надо посчитать заговорщиков
        
        
    # урожай
    def check_crop(self):
        self.data.rats_eat = 0
        
        # крысы пожрали зерно
        if self.ask.dice(50):
            self.data.rats_eat = round(self.data.resources['corn'] * self.ask.frand(0.1, 0.9))
        
        # расчёт урожайности
        self.data.resources['corn'] += round(self.data.corn_for_seed * self.data.crop_rate)
        
        # стихийные бедствия - засухи, пожары, наводнения
        
        
    # визирь украл и скрылся
    def check_vizier(self):
        pass

    # ограблен храм
    
    
    # 
    def report(self):
        self.say.clear_screen()
        self.say.line("Жалованье солдат: {:>10n} руб.\n".format(self.data.allowance))
        self.say.line("-----------------------------------------------------------------------")
        
        self.debug("на еду {:n}, на посев {:n} × {:.3} = урожай {:n} тонн, итого {:n}"
                  .format(self.data.corn_for_food,
                          self.data.corn_for_seed,
                          self.data.crop_rate,
                          round(self.data.corn_for_seed * self.data.crop_rate),
                          self.data.resources['corn']))
        
        if self.data.rats_eat:
            self.say.line(" - Крысы сожрали {:>10n} тонн зерна.".format(self.data.rats_eat))
        
        if self.data.deserters:
            self.say.line(" - Гвардия не получила денежного довольствия.\n" +
                  " {:>10n} солдат покинули казармы и ушли за кордон.".format(self.data.deserters))
        if self.data.fugitives:
            self.say.line(" - Рабочим не хватает земли. Сбежало {:>10n} человек.".format(self.data.fugitives))
        if self.data.famishes:
            self.say.line(" - Вы заморили голодом {:>10n} ваших верноподданных!".format(self.data.famishes))
        if self.data.births:
            self.say.line(" - В государстве родилось {:>10n} детей.".format(self.data.births))
        # if self.data.:
            # self.say.line(" -  {:>10n} \n".format(self.data.))
        # self.say.line()
            
            
    #
    def let_him_in(self):
        return self.ask.yesno("Ваше высочество! Прибыл визирь, впустить?")
        
        
        