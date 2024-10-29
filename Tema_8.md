# Тема 8. Основы объектно-ориентированного программирования
Отчет по Теме №8 выполнил:
- Цаплин Всеволод Ильич
- АИС-22-1

| Задание | Лаб_раб | Сам_раб |
| ------ | ------ | ------ |
| Задание 1 | + | + |
| Задание 2 | + | + |
| Задание 3 | + | + |
| Задание 4 | + | + |
| Задание 5 | + | + |

знак "+" - задание выполнено; знак "-" - задание не выполнено;

Работу проверили:
- к.э.н., доцент Панов М.А.

## Лабораторная работа №1

### Создайте класс "Car” с атрибутами производитель и модель. Создайте объект этого класса. Напишите комментарии для кода, объясняющие
### его работу. Результатом выполнения задания будет листинг кода с комментариями.

```python
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

my_car = Car("Трактор", "Деда")
```

### Результат.

![Меню](https://github.com/NikWither/universityProjects/blob/Тема_8/img/lab2.jpg)

## Лабораторная работа №2

### Дополните код из первого задания, добавив в него атрибуты и методы класса, заставьте машину "поехать". Напишите комментарии для кода,
### объясняющие его работу. Результатом выполнения задания будет листинг кода с комментариями и получившийся вывод в консоль.

```python
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def drive(self):
        print(f"Driving the {self.make} {self.model}")


my_car = Car("Трактор", "Деда")

my_car.drive()

```

### Результат

![Меню](https://github.com/NikWither/universityProjects/blob/Тема_8/img/lab2.jpg)

## Лабораторная работа №3

### Создайте новый класс "ElectricCar" с методом "charge" и атрибутом емкость батареи. Реализуйте его наследование от класса, созданного ### в первом задании. Заставьте машину поехать, а потом заряжаться.
### Напишите комментарии для кода, объясняющие его работу.
### Результатом выполнения задания будет листинг кода с комментариями и получившийся вывод в консоль.

```python
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def drive(self):
        print(f"Driving the {self.make} {self.model}")


class ElectricCar(Car):
    def __init__(self, make, model, battery_capacity):
        super().__init__(make, model)
        self.battery_capacity = battery_capacity

    def charge(self):
        print(f"Charging the {self.make} {self.model} with {self.battery_capacity}")


my_electric_car = ElectricCar("Дедовский трактор", "на самогоном апарате", "3 литра")
my_electric_car.drive()
my_electric_car.charge()
```

### Результат

![Меню](https://github.com/NikWither/universityProjects/blob/Тема_8/img/lab3.jpg)

  
## Лабораторная работа №4

### Реализуйте инкапсуляцию для класса, созданного в первом задании. Создайте защищенный атрибут производителя и приватный атрибут
### модели. Вызовите защищенный атрибут и заставьте машину поехать.Напишите комментарии для кода, объясняющие его работу.
### Результатом выполнения задания будет листинг кода с комментариями и получившийся вывод в консоль.

```python
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
    
```

### Результат

![Меню](https://github.com/NikWither/universityProjects/blob/Тема_8/img/lab4.jpg)


## Лабораторная работа №5

### Реализуйте полиморфизм создав основной (общий) класс "Shape", а также еще два класса "Rectangle" и "Circle". Внутри последних двух
### классов реализуйте методы для подсчета площади фигуры. После этого создайте массив с фигурами, поместите туда круг и прямоугольник,
### затем при помощи цикла выведите их площади. Напишите комментарии для кода, объясняющие его работу. Результатом
### выполнения задания будет листинг кода с комментариями и получившийся вывод в консоль.

```python
class Shape:
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


# создаем экземпляры классов с фигурами
newCircle_1 = Circle(5)
newCircle_2 = Circle(25)

newRectangle_1 = Rectangle(5, 4)
newRectangle_2 = Rectangle(10, 12)
# кладем в массив
figures = [newCircle_1, newCircle_2, newRectangle_1, newRectangle_2]
# обращаемся к каждому элементу массива и вызываем метод area()
for figures in figures:
    print(figures.area())

```

### Результат

![Меню](https://github.com/NikWither/universityProjects/blob/Тема_8/img/lab5.jpg)


## Самостоятельная работа №1
### Самостоятельно создайте класс и его объект. Они должны отличаться, от тех, что указаны в теоретическом материале
### (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.
       
```python
class Worker:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

worker_1 = Worker('Anton', 32, 'middle')
        
```

### Результат


### Выводы

Просто создаем класс Worker (работник), и даем ему то, что есть у каждого работника (закос под айти компанию). Родительские классы
желательно проектировать с особым вниманием, так как очень важно понимать, какие методы могут быть у дочерних классов

 
## Самостоятельная работа №2
### Самостоятельно создайте атрибуты и методы для ранее созданного класса. Они должны отличаться, от тех, что указаны в
### теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и
### получившийся вывод консоли.
       
```python
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
```

### Результат

![Меню](https://github.com/NikWither/universityProjects/blob/Тема_8/img/cp2.jpg)

### Выводы

Создал метода sleep() - ничего интересно, просто печатает, что работник спит и обращается к собственному атрибуту name
Метод upgradeAge() увеличивает возраст сотрдудника на единицу, все мы стареем
Метод getAge() (о да, я знаю что такое геттеры и сеттеры), возвращает текущий возраст

В качестве примера вызвал метод getAge(), затем увеличил возраст и вызвал геттер (getAge()) ещё раз.

## Самостоятельная работа №3
### Самостоятельно реализуйте наследование, продолжая работать с ранее созданным классом. Оно должно отличаться, от того, что
### указано в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и
### получившийся вывод консоли.


```python
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


```

### Результат

![Меню](https://github.com/NikWither/universityProjects/blob/Тема_8/img/cp3.jpg)


### Выводы

Создадим новый класс программист. У него также есть имя, возраст и грейд (как и у дизайнеров, маркетологов и т.д.), а также добавил
position (типо на каком стеке работает, но изначально хотел сделать там бек/фронт, но описался). Ну, предположим, что 
позиция фронт/бек у класса (будущего класса) дизайнер не было бы, поэтому это атрибут, который может быть тольк у этого класса 

## Самостоятельная работа №4

### Самостоятельно реализуйте инкапсуляцию, продолжая работать с ранее созданным классом. Она должна отличаться, от того, что
### указана в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и
### получившийся вывод консоли.

  
```python
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

```

### Результат

![Меню](https://github.com/NikWither/universityProjects/blob/Тема_8/img/cp4.jpg)

### Выводы

Добавил защищенный атрибут isMarried , это является персональной данной, а любая персональная информация должна быть защищена, вот такие
вот отсылки получились
Ну и атрибут salary (зарплата), во многих компаниях такие вещи как зарплата - засекречены, даже между сотрудниками, поэтому кто угодно
вызвать метод salary не сможет

## Самостоятельная работа №5

### Самостоятельно реализуйте полиморфизм. Он должен отличаться, от того, что указан в теоретическом материале (методичке) и
### лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.

```python
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

class Programmer(Worker):
    def __init__(self, name, age, grade, position, isMarried, salary):
        super().__init__(name, age, grade)
        self.position = position
        self._isMarried = isMarried
        self.__salary = salary
    
    def programming(self):
        print(f"Now, Im working with {self.position}")

    def work(self):
        self.programming()

Worker_1 = Worker('Jenya', 20, 'Junior')
Programmer_1 = Programmer('Anton', 25, 'middle','Python', True, 75000)

Worker_1.work()
Programmer_1.work()

```

### Результат

![Меню](https://github.com/NikWither/universityProjects/blob/Тема_8/img/cp5.jpg)


### Выводы

Переопределение методов. Значит создал класс от родителя Worker, у которого есть свой метод work. Так как воркер - это вообще непонятно кто, то у него метод работать "Что то делать", а вот такой же метод есть и у класса Программиста, но он уже не фигней страдает, а вызывает метод programming() при вызове метода work. Поэтому программист - работает с питоном, а воркер - ну что-то делает, хотя иногда бывает и одинаково.. В общем, как то так можно переопределять методы у каждого класса! Кроме приватных, т.к. они недоступны даже наследным классам.

## Общие выводы по теме

Концепция ООП - это очень круто. Всякие вещи по типу инкапсуляции, наследовании, полиморфизма и других (напр. абстракция) - это важные составляющие, да и вообще, база программирования. Сам я лично PHP разработчик, но освоить прицнипы ООП в питоне (которые в целом одинаковые везде) было несложно. С помощью ООП очень просто управлять и разбираться в проекте (особенно чужом и при работе в команде), а также такие проекты очень просто масштабируются. Большинство фреймворков (напр. ларавел/джанго) как раз реализованы на ООП, поэтому это база программирования (да и возможно в целом, завершающий этап в программировании), которую необходимо знать для освоения какого-либо фреймворка.
