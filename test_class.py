"""Примеры по созданию и использованию классов в питоне
Всё есть объект!
"""

class FirstClass:                   #когда интерпретатор достигнет инструкции class, он начнёт создавать объект класса с именем (ссылкой на объект)FirstClass
    def set_data(self, value):      #интерпретатор определяет метод класса (поведение по умолчанию для экземпляров)
        self.data = value           #экземпляр или контекст(self ссылка на объект) с переменной data должен будет получить значение через аргумент

    def display(self):              #def это операция присваивания переменной display к объекту функции в области видимости class
        print(self.data)            #и тем самым становясь атрибутом у объекта класса (FirstClass.display)



if __name__ == '__main__':
    x = FirstClass()        #x,y отдельные пространства имён
    y = FirstClass()        #создаются объекты экземпляров (из объекта класса FirstClass), а x и y это ссылки на них
                            #на данный момент имеются три связаных пространства имён
                            #атрибут data обнаруживается в объекте экземпляра, а set_data и display в классе

    x.set_data(5)
    x.display()
    print(x.data)

"""Ни x, ни y не имеют собственного атрибута setdata и display, поэтому, чтобы отыскать его, интерпретатор следует по ссылке от экземпляра к классу.
В этом заключается суть наследования в языке Python: механизм наследования привлекается в момент разрешения имени атрибута,
 и вся его работа заключается лишь в поиске имен в связанных объектах"""

