# entry point

# debug global method
def debug(msg):
    print('\033[41m DEBUG: \033[00m\033[91m', msg, '\033[00m')


import os
os.system('clear')

import random, sys, locale
locale.setlocale(locale.LC_ALL, 'ru_RU.utf-8')
sys.path.append('./events')

# import main modules
from data import Data
from say import Say
from info import Info
from ask import Ask
from act import Act


# init main modules
say = Say()
ask = Ask(say)
data = Data(ask)
info = Info(data)
act = Act(data, ask)

# import events modules
# from market import Market
# from distribute import Distribute
# from vizier import Vizier
from caravan import Caravan
# from church import Church
# from inheritance import Inheritance
#
# # init event modules
events = [
#     Market(),
#     Distribute(),
#     Vizier(),
    Caravan(data, say, ask),
#     Inheritance(),
#     Church()
]


act.meet_new_year()

# main loop
while data.king_hp > 0 and data.anger < 100:
    act.meet_new_year()
    
    say.clear_screen()
    info.big_table()
    
    for event in events:
        event.invoke()
    
    if not ask.yesno("Встречаете новый год?"):
        break
    
    if data.money > 1000 and ask.yesno("Устраиваете новогодний бал?"):
        error = True
        while error:
            spend, error, msg = ask.number("В казне {:n} руб., сколько на рождество?".format(data.money), data.money)
            if error:
                say.line(msg)
            
        data.money -= spend
# end of main loop

debug("Год правления {:n}, здоровье короля {:n}".format(data.year, data.king_hp))


