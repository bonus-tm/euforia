# Модуль вывода текста и т.д.
import os, re
import data

#
def line(*args):
    """Напечатать аргументы и поставить перенос строки в конце"""
    
    print(*args)

#
def word(*args):
    """Без переноса строки в конце"""
    
    print(end=" ", *args)

#
def erase_line(lines=1):
    """ Удалить lines последних строк """
    
    CURSOR_UP_ONE = '\x1b[1A'
    ERASE_LINE = '\x1b[2K'
    for i in range(0, lines):
        say.line(CURSOR_UP_ONE + ERASE_LINE + CURSOR_UP_ONE)

