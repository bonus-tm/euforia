# Модуль запроса данных
import os, re
import data


#
def number(prompt,
           max,
           min=0,
           default=0,
           error_max="В казне нет столько денег!",
           error_min=False):
    """ Запрос числа """
    got_number = False
    while not got_number:
        print(prompt, end=' ')
        text = input()
        try:
            number = int(text)
            got_number = True
            if number > max:
                got_number = False
                print(error_max)
            elif number < min:
                got_number = False
                if error_min:
                    print(error_min)
                else:
                    print(error_max)
        except ValueError:
            number = default
            got_number = True
    return number


#
def yesno(prompt="Вы согласны?", default=True):
    """ Запрос да/нет, либо 1/0"""
    print(prompt, "(1/0) ", end='')
    answer = input()
    if answer == "":
        return default
    elif answer in ['1', 'да', 'y', 'yes']:
        return True
    else:
        return False


#
def let_messenger_in(introduction="Прибыл гонец с известиями, впустить?"):
    """ Гонец с известиями """
    return yesno(introduction)


#
def will_meet_new_year():
    """ Встречать ли Новый год """
    if yesno("Встречаете новый год?"):
        if data.money > 1000 and yesno("Устраиваете новогодний бал?"):
            print("В казне {:n} руб., сколько на рождество?".format(data.money), end='')
            spend = number('', data.money)
            if spend > 0:
                data.money -= spend
        return True
    else:
        return False

