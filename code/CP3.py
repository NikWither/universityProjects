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
    def __init__(self, name, age, grade, position):
        super().__init__(name, age, grade)
        self.position = position
    
    def programming(self):
        print(f"Now, Im working with {self.position}")
    
Programmer_1 = Programmer('Anton', 25, 'middle','Python')

Programmer_1.programming()
