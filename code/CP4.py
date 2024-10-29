class Worker:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def sleep(self):
        print(f"{self.name} is sleeping now!")

    def work():
        print('To do something')

    def upgradeAge(self):
        self.age = self.age + 1

    def getAge(self):
        return self.age

class Programmer(Worker):
    def __init__(self, name, age, grade, position, isMarried, salary):
        super().__init__(name, age, grade)
        self.position = position
        self._isMarried = isMarried
        self.__salary = salary
    
    def programming(self):
        print(f"Now, Im working with {self.position}")
    
Programmer_1 = Programmer('Anton', 25, 'middle','Python', True, 75000)

print(Programmer_1._isMarried) # True
#print(Programmer_1.__salary) ошибка AttributeError
