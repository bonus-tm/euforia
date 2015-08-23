# Модуль хранения основных данных и их вывода
import random

# вероятности начала событий
probability = {
    'Market': 100,
    'Distribute': 100,
    'Vizier': 100,
    'Church': 0,
    'Caravan': 10,
    'Inheritance': 10,
}

# основные данные
date = 1985
# год правления
year = 0
king_age = 15
king_hp = 10

# экономическая блокада
embargo = False


# довольствие армии = кол-во солдат × 10 руб.
allowance = 0
# зерна на еду, на посев
corn_for_food = 0
corn_for_seed = 0
# крысы сожрали зерна
rats_eat = 0

# урожайность в текущем году - 0.5-7
crop_rate = 1

# недовольство, гнев народа
anger = 0
# процент заговорщиков
rebels = 0

# население - прибыль, убыль
births = 0
famishes = 0
fugitives = 0
deserters = 0


# казна
money = random.randrange(50, 1000)

# в государстве - ресурсы, начальные значения
resources = {
    'gold': 0,
    'land': random.randrange(50, 150),
    'corn': random.randrange(400, 1000),
    'peasant': random.randrange(50, 150),
    'soldier': random.randrange(50, 150)
}
 # диапазон колебаний min-max, множитель биржи
limits = {
    'gold':    (800, 2000,  0.1),
    'land':    ( 80,  160,  1.0),
    'corn':    (  4,   20, 10.0),
    'peasant': ( 50,  200,  1.0),
    'soldier': (100,  300,  0.5)
}
# текущие цены, начальные значения
prices = {
    'gold':    random.randrange(limits['gold'][0],    limits['gold'][1]),
    'land':    random.randrange(limits['land'][0],    limits['land'][1]),
    'corn':    random.randrange(limits['corn'][0],    limits['corn'][1]),
    'peasant': random.randrange(limits['peasant'][0], limits['peasant'][1]),
    'soldier': random.randrange(limits['soldier'][0], limits['soldier'][1])
}
history = []




#
def treasury():
    """Показать сколько денег в казне"""
    
    # print("В казне {:n} тыс. {:n} руб.".format(data.money // 1000, data.money % 1000))
    print("В казне {:n} руб.".format(money))


# 
def print_big_table():
    """ Большая таблица ресурсов с ценами - для главного экрана """
    
    print(" {:>10} год   {:>33d} год правления\n".format(date, year) +
          " В  в а ш е м  г о с у д а р с т в е  н а  т е к у щ и й  м о м е н т:\n" +
          "-----------------------------------------------------------------------\n" +
          "! Н а и м е н о в а н и е !  Количество  !  Стоимость  !  Курс биржи  !\n" +
          "-----------------------------------------------------------------------\n" +
          "!  З о л о т о    (кг  )  !  {:>10n}  ! {:>10d}  !  {:>10d}  !\n"
          .format(resources['gold'], prices['gold'], round(prices['gold'] * limits['gold'][2])) +
          "!  З е м л я      (га  )  !  {:>10n}  ! {:>10d}  !  {:>10d}  !\n"
          .format(resources['land'], prices['land'], round(prices['land'] * limits['land'][2])) +
          "!  З е р н о      (тонн)  !  {:>10n}  ! {:>10d}  !  {:>10d}  !\n"
          .format(resources['corn'], prices['corn'], round(prices['corn'] * limits['corn'][2])) +
          "!  Р а б о ч и е  (чел.)  !  {:>10n}  ! {:>10d}  !  {:>10d}  !\n"
          .format(resources['peasant'], prices['peasant'], round(prices['peasant'] * limits['peasant'][2])) +
          "!  Г в а р д и я  (сол.)  !  {:>10n}  ! {:>10d}  !  {:>10d}  !\n"
          .format(resources['soldier'], prices['soldier'], round(prices['soldier'] * limits['soldier'][2])) +
          "-----------------------------------------------------------------------\n" +
          "\n  В настоящее время в казне {:>10n} руб.\n".format(money))
    

#
def print_small_table(money, resources):
    """ Малая таблица ресурсов - для наследства, войны """
    
    print("\tКапитал: {:n} руб.".format(money))
    print("\t-------------------------------")
    print("\tЗолото  (кг  ) {:>10n}".format(resources['gold']))
    print("\tЗемля   (га  ) {:>10n}".format(resources['land']))
    print("\tЗерно   (тонн) {:>10n}".format(resources['corn']))
    print("\tРабочие (чел.) {:>10n}".format(resources['peasant']))
    print("\tГвардия (сол.) {:>10n}".format(resources['soldier']))



