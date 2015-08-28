# Модуль запроса данных
import random

class Ask():
    """ Запрос данных у юзера или генератора рандома """
    
    def __init__(self,
                 say,
                 input_func=lambda: input().strip().lower(),
                 random_int_func=lambda *args: random.randrange(*args),
                 random_float_func=lambda *args: random.uniform(*args),
                 random_choice_func=lambda seq: random.choice(seq)):
        self.say = say
        self.input_func = input_func
        self.random_int_func = random_int_func
        self.random_float_func = random_float_func
        self.random_choice_func = random_choice_func


    #
    def dice(self, probability):
        """ Случилось событие или нет — возвращает True или False """
    
        return self.random_int_func(100) < probability

    #
    def rand(self, min, max):
        """ Возвращает случайное целое число (int) между min и max """
    
        return self.random_int_func(min, max)

    #
    def frand(self, min, max):
        """ Возвращает случайное дробное число (float) между min и max """
    
        return self.random_float_func(min, max)

    #
    def choice(self, seq):
        """ Возвращает случайный элемент последовательности """
    
        return self.random_choice_func(seq)
    

    #
    def yesno(self, prompt="Вы согласны?", default=True):
        """ Запрос да/нет, либо 1/0 """
    
        self.say.word(prompt, "(1/0)")
        answer = self.input_func()
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
               error_msg="В казне нет столько денег!"):
        """ Запрос числа """
    
        self.say.word(prompt)
        text = self.input_func()
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


