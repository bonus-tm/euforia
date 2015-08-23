# main module
import os
os.system('clear')


import random, sys
import data, ask, act

import locale
locale.setlocale(locale.LC_ALL, 'ru_RU.utf-8')

sys.path.append('./events')
# import modules
from market import Market
from distribute import Distribute
from vizier import Vizier
from caravan import Caravan
from church import Church
from inheritance import Inheritance


# init modules
events = [
    Market(),
    Distribute(),
    Vizier(),
    Caravan(),
    Inheritance(),
    Church()
]


act.meet_new_year()

# main loop
while data.king_hp > 0 and data.anger < 100:
    act.meet_new_year()
    
    act.clear_screen()
    data.print_big_table()
    
    for event in events:
        event.invoke()
    
    if not ask.will_meet_new_year():
        break
# end of main loop

print("health", data.king_hp)
print("Year", data.year, " king is dead")

