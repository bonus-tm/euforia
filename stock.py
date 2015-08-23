import random

class Stock:
    """ Класс изменения цен """
    
    _default_chance_to_alter_trend = 0.2
    
    
    def __init__(self, min=0, max=100):
        self.min = min
        self.max = max
        self.range = max - min
        self.trend = 1 if random.random() < .5 else -1
        self.chance_to_alter_trend = self._default_chance_to_alter_trend
        self.delta = 0
        self.median = 0
        self.price = random.randint(min, max)
    
    
    def change(self):
        if random.random() < self.chance_to_alter_trend:
            self.trend = self.trend * -1

        self.delta = abs(random.gauss(self.median, 0.333))
        self.delta = round(self.delta * self.trend * self.range)

        self.price = self.price + self.delta

        if self.price > self.max:
            self.trend = -1
            self.price = self.max - random.randint(0, round(self.range/10))
        elif self.price < self.min:
            self.trend = 1
            self.price = self.min + random.randint(0, round(self.range/10))
        
        self.keep()
    
    
    def rise(self, percent):
        """ Резкий взлёт цены, вызывать перед change """
        
        self.trend = 1
        self.chance_to_alter_trend = 0
        self.median = self.range * percent
    
    
    def fall(self, percent):
        """ Резкое падение цены, вызывать перед change """
        
        self.trend = -1
        self.chance_to_alter_trend = 0
        self.median = self.range * percent
    
    
    def keep(self):
        self.chance_to_alter_trend = self._default_chance_to_alter_trend
        self.median = 0




year = 0
life = 40


# init prices
gold = Stock(800, 2000)
land = Stock(80, 160)
corn = Stock(4, 20)
peasant = Stock(50, 200)
soldier = Stock(100, 300)


# main cycle
print("{}\t{}\t{}\t{}\t{}\t{}".format('Год', 'Золото', 'Земля', 'Зерно', 'Рабочие', 'Солдаты'))
while year < life:
    year = year + 1
    
    if year == 10:
        gold.fall(80)
        land.rise(20)
    gold.change()
    land.change()
    corn.change()
    peasant.change()
    soldier.change()
    gold.change()
    
    print("{:d}\t{:d}\t{:d}\t{:d}\t{:d}\t{:d}".format(
        year,
        gold.price,
        land.price,
        corn.price,
        peasant.price,
        soldier.price
    ))




