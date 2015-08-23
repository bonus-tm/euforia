# Модуль глобальных действий:
#  изменения цен
#  очистки экрана
#  удаления последних строк
#  ...
import random
import data

# debug global method
def debug(info):
    """ debug """
    print('\033[41m DEBUG: \033[00m\033[91m', info, '\033[00m')
    

#
def erase_line(lines=1):
    """ Удалить lines последних строк """
    CURSOR_UP_ONE = '\x1b[1A'
    ERASE_LINE = '\x1b[2K'
    for i in range(0, lines):
        print(CURSOR_UP_ONE + ERASE_LINE + CURSOR_UP_ONE)


# 
def clear_screen():
    """ Очистить экран """
    # os.system('clear')
    # print("width {}, height {}".format(os.get_terminal_size()[0], os.get_terminal_size()[1]))
    print(" - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
    

#
def meet_new_year():
    """ Новый год - записать историю, обновить цены """
    write_down_history()
    
    data.year += 1
    data.date += 1
    data.king_age += 1
    data.king_hp -= 1
    
    data.crop_rate = random.uniform(0.5, 7)
    
    make_new_prices()
    
    dice = random.randrange(100)
    if dice < 15:
        data.embargo = True
    else:
        data.embargo = False


def write_down_history():
    """docstring for write_down_history"""
    data.history.append({'prices': data.prices})

#    
def make_new_prices():
    """ Ежегодное изменение цен """
    data.prices['gold'] = random.randrange(800, 1800)
    data.prices['land'] = random.randrange(80, 150)
    data.prices['corn'] = random.randrange(5, 17)
    data.prices['peasant'] = random.randrange(50, 180)
    data.prices['soldier'] = random.randrange(100, 290)
    

# 
def shift_price():
    """docstring for shift_price"""
    pass