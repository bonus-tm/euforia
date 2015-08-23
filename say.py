# Модуль вывода текста и т.д.
import os, re
import data

def line(*args):
    """Напечатать аргументы и поставить перенос строки в конце"""
    print(*args)

def word(*args):
    """Без переноса строки в конце"""
    print(end=" ", *args)
