class Worker:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def sleep(self):
        print(f"{self.name} is sleeping now!")

    def work(self):
        print('To do something')

    def upgradeAge(self):
        self.age = self.age + 1

    def getAge(self):
        return self.age
    


worker_1 = Worker('Anton', 32, 'middle')

worker_1.sleep()

print(worker_1.getAge())
worker_1.upgradeAge()
print(worker_1.getAge())