# Модуль запроса данных
import os, re
import say, data

#
def default_input_func():
    return input().strip().lower()

#
def erase_line(lines=1):
    """ Удалить lines последних строк """
    CURSOR_UP_ONE = '\x1b[1A'
    ERASE_LINE = '\x1b[2K'
    for i in range(0, lines):
        say.line(CURSOR_UP_ONE + ERASE_LINE + CURSOR_UP_ONE)

#
def yesno(prompt="Вы согласны?", default=True, input_func=default_input_func):
    """ Запрос да/нет, либо 1/0 """
    say.word(prompt, "(1/0)")
    answer = input_func()
    if answer == "":
        return default
    elif answer in ['1', '11', '111', 'да', 'y', 'yes']:
        return True
    else:
        return False

#
def number(prompt,
           max,
           min=0,
           default=0,
           error_max="В казне нет столько денег!",
           error_min=False,
           input_func=default_input_func,
           try_once=False):
    """ Запрос числа """
    done = False
    while not done:
        say.word(prompt)
        text = input_func()
        try:
            number = int(text)
            done = True
            if number > max:
                number = max
                done = try_once
                say.line(error_max)
            elif number < min:
                number = min
                done = try_once
                if error_min:
                    say.line(error_min)
                else:
                    say.line(error_max)
        except ValueError:
            number = default
            done = True
    return number

#
def corn(max, input_func=default_input_func, try_once=False):
    """ Сколько зерна на еду, сколько на посев """
    
    done = False
    while not done:
        erase_line()
        say.word("Сколько тонн зерна на еду, сколько на посев?")
        answer = re.findall('[0-9]+', input_func())
        
        try:
            food = int(answer[0])
            seed = int(answer[1])
            
            if food > max:
                done = try_once
                food = -1
                seed = -1
            elif food + seed > max:
                done = True
                seed = max - food
            else:
                done = True
        except ValueError:
            done = try_once
            
    return [food, seed]

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

