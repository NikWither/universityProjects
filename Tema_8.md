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

### Напишите программу, которая выведет только первую строку из вашего файла, при этом используйте конструкцию open()/close().

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

### Напишите программу, которая выведет все строки из вашего файла в массиве, при этом используйте конструкцию open(/close().

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

### Напишите программу, которая выведет все строки из вашего файла в массиве, при этом используйте конструкцию with open().

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

### Напишите программу, которая выведет каждую строку из вашего файла отдельно, при этом используйте конструкцию with open().

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
### У вас появилась потребность в ведении книги расходов, посмотрев все существующие варианты вы пришли к выводу что вас ничего не
       
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


 
## Самостоятельная работа №2
### У вас появилась потребность в ведении книги расходов, посмотрев все существующие варианты вы пришли к выводу что вас ничего не
### устраивает и нужно все делать самому. Напишите программу для учета расходов. Программа должна позволять вводить информацию
### о расходах, сохранять ее в файл и выводить существующие данные в консоль. Ввод информации происходит через консоль. Результатом
### выполнения задачи будет: скриншот файла с учетом расходов, листинг кода, и вывод в консоль, с демонстрацией работоспособности программы.
       
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

  
## Самостоятельная работа №3
### Ребята поспорили кто из них одним нажатием на numpad наберет больше повторяющихся цифр, но не понимают, как узнать


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



## Самостоятельная работа №4
  
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

![Меню](https://github.com/NikWither/universityProjects/blob/Тема_8/img/CP4.jpg)

### Выводы

## Самостоятельная работа №5

### Самостоятельно придумайте и решите задачу, которая будет взаимодействовать с текстовым файлом.
### Необходимо открыть файл, найти все числа в файле, а затем вернуть их сумму 

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

![Меню](https://github.com/NikWither/universityProjects/blob/Тема_8/img/CP5.jpg)


### Выводы

Открываем файл через try и except, также используя встроенную except ошибку FileNotFoundError, далее прикольно было бы еще попробовать использовать try&except, если можем преобразовать символ (а мы там уже по циклам for все разбили до символов, смотрим КАЖДЫЙ символ в тексте), так вот, если смогли преобразовать символ в число (а у нас всё по умолчанию - строки), то круто, мы сделали из '5' число 5. ПРосто добавляем total_sum(), затем просто выводим все прямо из функции. 
Тут очень высокая вычислительная сложность и код неоптимизирован, но захотел еще попробовать try except в питоне. Туда можно вообще всякую дичь писать, как например пытаться преобразовать символ в число и не словить ошибку типизации) короче динамические ЯП это забавно.

## Общие выводы по теме

Работа с файлами в Python включает несколько основных этапов: открытие файла с помощью функции open(), чтение или запись данных в файл. Для чтения файла могут использоваться методы read(), readline(), readlines(), а для записи — write() и writelines() (не всё упоминалось, загуглил). Важным аспектом является выбор режима открытия файла, например, для чтения ("r"), записи ("w") или добавления данных ("a"), а также присутствует возможность добавления кодировки, но у нас везде ютф8. Для упрощения работы и автоматического закрытия файла можно использовать контекстный менеджер with.
Помимо этого, изучил try catch (except). Пользовался ими на языке PHP при  запросах к БД. Работает аналогично. Также присутствует возможность ловли отдельных ошибок, как например FileNotFoundError. 

