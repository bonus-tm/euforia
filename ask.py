# Модуль запроса данных
import os, re
import say, data


def default_input_func():
    """docstring for default_input_func"""
    return input()

#
def number(prompt,
           max,
           min=0,
           default=0,
           error_max="В казне нет столько денег!",
           error_min=False,
           input_func=default_input_func):
    """ Запрос числа """
    got_number = False
    while not got_number:
        say.word(prompt)
        text = input_func()
        try:
            number = int(text)
            got_number = True
            if number > max:
                got_number = False
                say.line(error_max)
            elif number < min:
                got_number = False
                if error_min:
                    say.line(error_min)
                else:
                    say.line(error_max)
        except ValueError:
            number = default
            got_number = True
    return number


#
def yesno(prompt="Вы согласны?", default=True, input_func=default_input_func):
    """ Запрос да/нет, либо 1/0"""
    say.word(prompt, "(1/0)")
    answer = input_func()
    if answer == "":
        return default
    elif answer.lower() in ['1', '11', '111', 'да', 'y', 'yes']:
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
            say.word("В казне {:n} руб., сколько на рождество?".format(data.money))
            spend = number('', data.money)
            if spend > 0:
                data.money -= spend
        return True
    else:
        return False

