# Модуль вывода текста и т.д.
import os

class Say():
    """ Вывод простых строк """
    def __init__(self, print_func=print):
        self.print = print_func
        
    #
    def line(self, *args):
        """ Напечатать аргументы и поставить перенос строки в конце """
    
        self.print(*args)

    #
    def word(self, *args):
        """ Без переноса строки в конце """
    
        self.print(end=" ", *args)

    #
    def erase_line(self, lines=1):
        """ Удалить lines последних строк """
    
        CURSOR_UP_ONE = '\x1b[1A'
        ERASE_LINE = '\x1b[2K'
        for i in range(0, lines):
            self.line(CURSOR_UP_ONE + ERASE_LINE + CURSOR_UP_ONE)
    
    # 
    def clear_screen(self):
        """ Очистить экран """
        
        # os.system('clear')
        # print("width {}, height {}".format(os.get_terminal_size()[0], os.get_terminal_size()[1]))
        self.line(" - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - ")
    
    

