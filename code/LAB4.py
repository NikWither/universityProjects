class Car:
    def __init__(self, make, model):
        self._make = make # защищенный атрибут, доступный для чтения только детям этого класса (ну и самому классу)
        self.__model = model # приватный атрибут, доступен только здесь
    
    def drive(self):
        print(f"Driving the {self._make} {self.__model}")


my_car = Car("Toyota", "Corolla")

print(my_car._make) # в VSC ничего не подсвечивает
# print(my_car.__model) # да, действительно ошибка
my_car.drive()