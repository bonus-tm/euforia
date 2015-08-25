# Модуль запроса данных
import random

class Ask():
    """ Запрос данных у юзера или генератора рандома """
    
    def __init__(self, say):
        self.say = say
        

    #
    def default_input_func():
        return input().strip().lower()

    #
    def default_random_func(*args):
        return random.randrange(*args)

    #
    def default_float_random_func(*args):
        return random.uniform(*args)

    #
    def default_random_choice_func(seq):
        return random.choice(seq)

    #
    def dice(self, probability, random_func=default_random_func):
        """ Случилось событие или нет — возвращает True или False """
    
        return random_func(100) < probability

    #
    def rand(self, min, max, random_func=default_random_func):
        """ Возвращает случайное целое число (int) между min и max """
    
        return random_func(min, max)

    #
    def frand(self, min, max, random_func=default_float_random_func):
        """ Возвращает случайное дробное число (float) между min и max """
    
        return random_func(min, max)

    #
    def choice(self, seq, random_func=default_random_choice_func):
        """ Возвращает случайный элемент последовательности """
    
        return random_func(seq)
    

    #
    def yesno(self, prompt="Вы согласны?", default=True, input_func=default_input_func):
        """ Запрос да/нет, либо 1/0 """
    
        self.say.word(prompt, "(1/0)")
        answer = input_func()
        if answer == "":
            return default
        elif answer in ['1', '11', '111', 'да', 'y', 'yes']:
            return True
        else:
            return False

    #
    def number(self,
               prompt,
               max,
               error_msg="В казне нет столько денег!",
               input_func=default_input_func):
        """ Запрос числа """
    
        self.say.word(prompt)
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


