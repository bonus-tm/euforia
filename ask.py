# Модуль запроса данных
import os, re, random
import say, data

#
def default_input_func():
    return input().strip().lower()

#
def default_random_func(*args):
    return random.randrange(*args)

#
def default_random_choice_func(seq):
    return random.choice(seq)

#
def dice(probability, random_func=default_random_func):
    """ Случилось событие или нет — возвращает True или False """
    
    return random_func(100) < probability

#
def rand(min, max, random_func=default_random_func):
    """ Возвращает случайное число между min и max """
    
    return random_func(min, max)

#
def choice(seq, random_func=default_random_choice_func):
    """ Возвращает случайный элемент последовательности """
    
    return random_func(seq)
    

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
           error_msg="В казне нет столько денег!",
           input_func=default_input_func):
    """ Запрос числа """
    
    say.word(prompt)
    text = input_func()
    error = False
    msg = ""
    try:
        number = int(text)
        if number > max:
            number = max
            error = True
            msg = error_msg
        return (number, error, msg)
    except ValueError:
        return (-1, True, "Это не число!")
        

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

