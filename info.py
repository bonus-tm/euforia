from say import Say

class Info(Say):
    """ Вывод сложных данных — таблиц и т.д. """
    def __init__(self, data):
        self.data = data
        
    #
    def treasury(self):
        """Показать сколько денег в казне"""
    
        # print("В казне {:n} тыс. {:n} руб.".format(data.money // 1000, data.money % 1000))
        print("В казне {:n} руб.".format(self.data.money))


    # 
    def big_table(self):
        """ Большая таблица ресурсов с ценами - для главного экрана """
    
        print(" {:>10} год   {:>33d} год правления\n".format(self.data.date, self.data.year) +
              " В  в а ш е м  г о с у д а р с т в е  н а  т е к у щ и й  м о м е н т:\n" +
              "-----------------------------------------------------------------------\n" +
              "! Н а и м е н о в а н и е !  Количество  !  Стоимость  !  Курс биржи  !\n" +
              "-----------------------------------------------------------------------\n" +
              "!  З о л о т о    (кг  )  !  {:>10n}  ! {:>10d}  !  {:>10d}  !\n"
              .format(self.data.resources['gold'],
                      self.data.prices['gold'],
                      round(self.data.prices['gold'] * self.data.limits['gold'][2])) +
              "!  З е м л я      (га  )  !  {:>10n}  ! {:>10d}  !  {:>10d}  !\n"
              .format(self.data.resources['land'],
                      self.data.prices['land'],
                      round(self.data.prices['land'] * self.data.limits['land'][2])) +
              "!  З е р н о      (тонн)  !  {:>10n}  ! {:>10d}  !  {:>10d}  !\n"
              .format(self.data.resources['corn'],
                      self.data.prices['corn'],
                      round(self.data.prices['corn'] * self.data.limits['corn'][2])) +
              "!  Р а б о ч и е  (чел.)  !  {:>10n}  ! {:>10d}  !  {:>10d}  !\n"
              .format(self.data.resources['peasant'],
                      self.data.prices['peasant'],
                      round(self.data.prices['peasant'] * self.data.limits['peasant'][2])) +
              "!  Г в а р д и я  (сол.)  !  {:>10n}  ! {:>10d}  !  {:>10d}  !\n"
              .format(self.data.resources['soldier'],
                      self.data.prices['soldier'],
                      round(self.data.prices['soldier'] * self.data.limits['soldier'][2])) +
              "-----------------------------------------------------------------------\n" +
              "\n  В настоящее время в казне {:>10n} руб.\n".format(self.data.money))
    

    #
    def small_table(money, resources):
        """ Малая таблица ресурсов - для наследства, войны """
    
        print("\tКапитал: {:n} руб.".format(money))
        print("\t-------------------------------")
        print("\tЗолото  (кг  ) {:>10n}".format(resources['gold']))
        print("\tЗемля   (га  ) {:>10n}".format(resources['land']))
        print("\tЗерно   (тонн) {:>10n}".format(resources['corn']))
        print("\tРабочие (чел.) {:>10n}".format(resources['peasant']))
        print("\tГвардия (сол.) {:>10n}".format(resources['soldier']))

    