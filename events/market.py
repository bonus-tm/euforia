# Торговля
import random, re
import data, ask, act
from event import Event

class Market(Event):
    """docstring for Market"""
    
    def invoke(self):
        if data.embargo:
            data.probability['Market'] = 0
            say.line("   ЧП! Экономическая блокада!\n")
        else:
            data.probability['Market'] = 100
            say.line("   Торговля - двигатель прогресса\n")
        super().invoke()
    
    
    def start(self):
        """docstring for start"""
        complete = False
        say.line("\n")
        while not complete:
            act.erase_line(2)
            self.broker_wants = round(data.money * random.uniform(0.2, 0.99))
            say.line("   Маклер просит {:>10n} руб.".format(self.broker_wants))
            if ask.yesno("Желаете использовать маклера?"):
                complete = self.broker()
                continue
            
            act.erase_line(2)
            if ask.yesno("Желаете сами торговать?"):
                complete = self.manual()
            else:
                act.erase_line()
                break
        else:
            act.clear_screen()
            data.print_big_table()
    
    
    def manual(self):
        """ Сколько чего продать/купить """
        debet = data.money
        credit = 0
        act.erase_line()
        say.line("            (+) Покупайте / Продавайте (-):")
        say.word("Золото (кг), земля (га), зерно (т), рабочие, солдаты (чел)? ")
        answer = re.search(r"""(?P<gold>[-+]?\d+)     # 1 золото
                               ([^0-9+-]+)? # delimiter
                               (?P<land>[-+]?\d+)?    # 3 земля
                               ([^0-9+-]+)? # delimiter
                               (?P<corn>[-+]?\d+)?    # 5 зерно
                               ([^0-9+-]+)? # delimiter
                               (?P<peasant>[-+]?\d+)? # 7 рабочие
                               ([^0-9+-]+)? # delimiter
                               (?P<soldier>[-+]?\d+)? # 9 солдаты
                               """,
                      input().strip(),
                      re.VERBOSE)
        if answer:
            # проверить достаточность товаров и рассчитать предварительный итог
            for resource in data.resources.keys():
                value = int(answer.group(resource) or 0)
                if value > 0:
                    credit += value * data.prices[resource]
                elif value < 0:
                    if abs(value) > data.resources[resource]:
                        act.erase_line(2)
                        print("Вы продаёте товара больше, чем у вас есть!")
                        return not ask.yesno("Повторить?")
                    else:
                        debet += abs(value) * data.prices[resource]
            # проверка достаточности денег
            if debet - credit < 0:
                act.erase_line(2)
                print("Сделка расторгнута - нехватает {:>10n} руб.".format(debet - credit))
                return not ask.yesno("Повторить?")
            else:
                # всё верно - завершить сделку
                for resource in data.resources.keys():
                    data.money = debet - credit
                    value = int(answer.group(resource) or 0)
                    data.resources[resource] += value
                return True
        else:
            return False
                
    
    def broker(self):
        """ Маклер """
        pass