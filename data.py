# Модуль хранения основных данных и их вывода
import datetime

class Data():
    """ Хранилище данных — синглтон по сути"""
    def __init__(self, ask):
        self.ask = ask

        # вероятности начала событий
        self.probability = {
            'Market': 100,
            'Distribute': 100,
            'Vizier': 100,
            'Church': 0,
            'Caravan': 10,
            'Inheritance': 10,
        }

        # основные данные
        self.date = datetime.date.today().year
        # год правления
        self.year = 0
        self.king_age = 15
        self.king_hp = 10

        # экономическая блокада
        self.embargo = False


        # довольствие армии = кол-во солдат × 10 руб.
        self.allowance = 0
        # зерна на еду, на посев
        self.corn_for_food = 0
        self.corn_for_seed = 0
        # крысы сожрали зерна
        self.rats_eat = 0

        # урожайность в текущем году - 0.5-7
        self.crop_rate = 1
        self.crop_rate_range = (0.5, 7)

        # недовольство, гнев народа
        self.anger = 0
        # процент заговорщиков
        self.rebels = 0

        # население - прибыль, убыль
        self.births = 0
        self.famishes = 0
        self.fugitives = 0
        self.deserters = 0


        # казна
        self.money = ask.rand(50, 1000)

        # в государстве - ресурсы, начальные значения
        self.resources = {
            'gold': 0,
            'land': ask.rand(50, 150),
            'corn': ask.rand(400, 1000),
            'peasant': ask.rand(50, 150),
            'soldier': ask.rand(50, 150)
        }
         # диапазон колебаний min-max, множитель биржи
        self.limits = {
            'gold':    (800, 2000,  0.1),
            'land':    ( 80,  160,  1.0),
            'corn':    (  4,   20, 10.0),
            'peasant': ( 50,  200,  1.0),
            'soldier': (100,  300,  0.5)
        }
        # текущие цены, начальные значения
        self.prices = {
            'gold':    ask.rand(self.limits['gold'][0],    self.limits['gold'][1]),
            'land':    ask.rand(self.limits['land'][0],    self.limits['land'][1]),
            'corn':    ask.rand(self.limits['corn'][0],    self.limits['corn'][1]),
            'peasant': ask.rand(self.limits['peasant'][0], self.limits['peasant'][1]),
            'soldier': ask.rand(self.limits['soldier'][0], self.limits['soldier'][1])
        }
        self.history = []
    
    def get(self, name):
        return getattr(self, name)
    
    
