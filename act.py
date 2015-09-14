# Модуль глобальных действий:
#  изменения цен
#  очистки экрана
#  удаления последних строк
#  ...
import random
import data

class Act():
    """ Разные действия
    Встретить Новый год:
        записать историю с прошлого года (цены, казну, ресурсы и т.д.)
        увеличить счётчики
        рассчитать урожайность нового года
        определить наличие эмбарго — экономической блокады
        обновить цены
        
    """
    
    def __init__(self, data, ask):
        self.data = data
        self.ask = ask
            

    #
    def meet_new_year(self):
        """ Новый год - записать историю, обновить цены """
        
        self.write_down_history()
    
        self.data.year += 1
        self.data.date += 1
        self.data.king_age += 1
        self.data.king_hp -= 1
    
        self.data.crop_rate = self.ask.frand(*self.data.crop_rate_range)
    
        self.make_new_prices()
    
        self.data.embargo = True if self.ask.dice(15) else False


    def write_down_history(self):
        """docstring for write_down_history"""
        self.data.history.append({'prices': self.data.prices})

    #    
    def make_new_prices(self):
        """ Ежегодное изменение цен """
        
        self.data.prices['gold'] = self.ask.rand(800, 1800)
        self.data.prices['land'] = self.ask.rand(80, 150)
        self.data.prices['corn'] = self.ask.rand(5, 17)
        self.data.prices['peasant'] = self.ask.rand(50, 180)
        self.data.prices['soldier'] = self.ask.rand(100, 290)
    

    # 
    def shuffle_price(self):
        """ docstring for shuffle_price """
        pass


