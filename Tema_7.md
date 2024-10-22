# Тема 7. Работа с файлами (ввод, вывод).
Отчет по Теме №7 выполнил:
- Цаплин Всеволод Ильич
- АИС-22-1

| Задание | Лаб_раб | Сам_раб |
| ------ | ------ | ------ |
| Задание 1 | + | + |
| Задание 2 | + | + |
| Задание 3 | + | + |
| Задание 4 | + | - |
| Задание 5 | + | + |
| Задание 6 | + | - |
| Задание 7 | + | - |
| Задание 8 | + | - |
| Задание 9 | + | - |
| Задание 10 | + | - |

знак "+" - задание выполнено; знак "-" - задание не выполнено;

Работу проверили:
- к.э.н., доцент Панов М.А.

## Лабораторная работа №1

### Составьте текстовый файл и положите его в одну директорию с программой на Python. Текстовый файл должен состоять минимум из двух строк.

### Результат.

![Меню](https://github.com/NikWither/universityProjects/blob/Тема_7/img/lab1.jpg)

## Лабораторная работа №2

### Напишите программу, которая выведет только первую строку из вашего файла, при этом используйте конструкцию open()/close().

```python
f = open('input.txt', 'r')
print(f.readline())
f.close()
```

### Результат

![Меню](https://github.com/NikWither/universityProjects/blob/Тема_7/img/lab2.jpg)

## Лабораторная работа №3

### Напишите программу, которая выведет все строки из вашего файла в массиве, при этом используйте конструкцию open(/close().

```python
f = open('input.txt', 'r')
print(f.readlines())
f.close()
```

### Результат

![Меню](https://github.com/NikWither/universityProjects/blob/Тема_7/img/lab3.jpg)

  
## Лабораторная работа №4

### Напишите программу, которая выведет все строки из вашего файла в массиве, при этом используйте конструкцию with open().

```python

with open('input.txt') as f:
    print(f.readlines())
    
```

### Результат

![Меню](https://github.com/NikWither/universityProjects/blob/Тема_7/img/lab4.jpg)


## Лабораторная работа №5

### Напишите программу, которая выведет каждую строку из вашего файла отдельно, при этом используйте конструкцию with open().

```python
with open('input.txt') as f:
    for line in f:
        print(line)
```

### Результат

![Меню](https://github.com/NikWither/universityProjects/blob/Тема_7/img/lab5.jpg)

## Лабораторная работа №6

### Напишите программу, которая будет добавлять новую строку в ваш файл, а потом выведет полученный файл в консоль. Вывод можно
### осуществлять любым способом. Обязательно проверьте сам файл, чтобы изменения в нем тоже отображались.

```python
with open('input.txt', 'a+') as f:
    f.write('\nIm additional line')

with open('input.txt', 'r') as f:
    result = f.readlines()
    print(result)

```

### Результат

![Меню](https://github.com/NikWither/universityProjects/blob/Тема_7/img/lab6.jpg)

## Лабораторная работа №7

### Напишите программу, которая перепишет всю информацию, которая была у вас в файле до этого, например напишет любые данные из
### произвольно вами составленного списка. Также не забудьте проверить что измененная вами информация сохранилась в файле.

```python
lines = ['one', 'two', 'three']
with open('input.txt', 'w') as f:
    for line in lines:
        f.write('\nCycle run ' + line)
    print('Done!')
```

### Результат

![Меню](https://github.com/NikWither/universityProjects/blob/Тема_7/img/lab7.jpg)

## Лабораторная работа №8

### Выберите любую папку на своем компьютере, имеющую вложенные директории. Выведите на печать в терминал ее содержимое, как и всех
### подкаталогов при помощи функции print docs(directory).

```python
import os

def print_docs(directory):
    all_files = os.walk(directory)
    for catalog in all_files:
        print(f"Папка {catalog[0]} содержит:")
    print(f"Директории: {", ".join([folder for folder in catalog[1]])}")
    print(f"Файлы: {", ".join([file for file in catalog[2]])}")
    print('-' * 40)

print_docs('C:\PHP8')
```

### Результат

![Меню](https://github.com/NikWither/universityProjects/blob/Тема_7/img/lab8.jpg)

## Лабораторная работа №9

### Требуется реализовать функцию, которая выводит слово, имеющее
### максимальную длину (или список слов, если таковых несколько).
### Проверьте работоспособность программы на своем наборе данных

```python
def longest_words(file):
    with open(file, encoding='utf-8') as f:
        words = f.read().split()
        max_length = len(max(words, key=len))
        for word in words:
            if len(word) == max_length:
                sought_words = word

        if len(sought_words) == 1:
            return sought_words[0]
        return sought_words

print(longest_words('input.txt'))
```

### Результат

![Меню](https://github.com/NikWither/universityProjects/blob/Тема_7/img/lab9.jpg)

## Лабораторная работа №10

### Требуется создать csv-файл «rows_300.csv» со следующими столбцами:
### · № - номер по порядку (от 1 до 300);
### · Секунда - текущая секунда на вашем ПК;
### · Микросекунда - текущая миллисекунда на часах.
### Для наглядности на каждой итерации цикла искусственно риостанавливайте скрипт на 0,01 секунды.

```python
import csv
import datetime
import time

with open('rows_300.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['№', 'Секунда', 'Микросекунда'])
    for line in range(1, 301):
        writer.writerow([line, datetime.datetime.now().second, datetime.datetime.now().microsecond])
        time.sleep(0.01)
```

### Результат

![Меню](https://github.com/NikWither/universityProjects/blob/Тема_7/img/lab10.jpg)


## Самостоятельная работа №1
### Найдите в интернете любую статью (объем статьи не менее 200 слов), скопируйте ее содержимое в файл и напишите программу,
### которая считает количество слов в текстовом файле и определит самое часто встречающееся слово. Результатом выполнения задачи
### будет: скриншот файла со статьей, листинг кода, и вывод в консоль, в котором будет указана вся необходимая информация.

```python
def count_words(filename):

    most_common_word = 0
    max_count = 0

    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read().lower()

    words = text.split()

    word_count = {}
    
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    for word, count in word_count.items():
        if count > max_count:
            max_count = count
            most_common_word = word
    
    print(f'Количество слов: {len(words)}')
    print(f'Самое часто встречающееся слово: "{most_common_word}", встречается {max_count} раз')

if __name__ == '__main__':
    count_words('DigitalRuble')

```

### Результат

## Консоль

![Меню](https://github.com/NikWither/universityProjects/blob/Тема_7/img/cp1.jpg)

## Текст

![Меню](https://github.com/NikWither/universityProjects/blob/Тема_7/img/cp1_text.jpg)

### Выводы

Здесь всё просто, запрашиваем у пользователя строку, затем для списка с помощью метода split() разбиваем строчки по проблемам в список.
Для конвертации в кортеж воспользуемся функцией tuple(), куда положим уже готовый массив.
 
## Самостоятельная работа №2
### У вас появилась потребность в ведении книги расходов, посмотрев все существующие варианты вы пришли к выводу что вас ничего не
### устраивает и нужно все делать самому. Напишите программу для учета расходов. Программа должна позволять вводить информацию
### о расходах, сохранять ее в файл и выводить существующие данные в консоль. Ввод информации происходит через консоль. Результатом
### выполнения задачи будет: скриншот файла с учетом расходов, листинг кода, и вывод в консоль, с демонстрацией работоспособности программы.
       
```python
def add_expense(filename):
    date = input("Введите дату расхода (в формате ДД.ММ.ГГГГ): ")
    category = input("Введите категорию расхода: ")
    amount = input("Введите сумму расхода: ")

    with open(filename, 'a', encoding='utf-8') as file:
        file.write(f"{date},{category},{amount}\n")
    
    print("Расход добавлен!")


def view_expenses(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            print("\nТекущие расходы:")
            for line in file:
                date, category, amount = line.strip().split(',')
                print(f"Дата: {date}, Категория: {category}, Сумма: {amount} руб.")
        print()
    except FileNotFoundError:
        print("Записей о расходах пока нет.")

def calculate_total_expenses(filename):
    total = 0
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                _, _, amount = line.strip().split(',')
                total += float(amount)  # Суммируем расходы
        print(f"\nОбщая сумма расходов: {total:.2f} руб.\n")
    except FileNotFoundError:
        print("Записей о расходах пока нет.")

def main():
    filename = "expenses.txt"
    
    while True:
        print("\nМеню:")
        print("1. Добавить расход")
        print("2. Просмотреть все расходы")
        print("3. Посчитать все расходы")
        print("4. Выход")
        
        choice = input("Выберите действие (1-4): ")
        
        if choice == '1':
            add_expense(filename)
        elif choice == '2':
            view_expenses(filename)
        elif choice == '3':
            calculate_total_expenses(filename)
        elif choice == '4':
            print("Программа завершена.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()

```

### Результат

![Меню](https://github.com/NikWither/universityProjects/blob/Тема_6/pic/cp2.jpg)

### Выводы

Все тестовые данные представил в виде строки (а как иначе?? одна незакрытая скобка не дает покоя). Где-то код выглядит перегруженным, но в целом, вроде как,
не так уж и сложно. функция transformToList() принимает кортеж, далее по очередности: делает сплит строки до первой закрывающейся скобки с одной кавычкой (ну чтобы отделить и забрать 
только числа, типа: "1, 2, 3", с такой строкой проще работать, первое решение, которое пришло в голову. Затем делаем срез строки с первого символа (убираем открывающуюся скобку),
после чего делаем сплит по запятой. Получаем классный массив из '(1, 2, 3), 1)' в ['1', '2', '3']. С таким форматом удобнее работать. Кстати, эта функция будет использоваться
не только в этой задачи.
Вторая функция getFinderElement() также отделяет лишний шлак от строки, оставляя только нужное число по поиску. Опять же, из строки '(1, 2, 3), 1)' получаем просто '1'.
Далее возвращаемся в главную функцию remove_element, где получаем нормальный массив и число, заданное по поиску. Ищем в списке это число, удаляем, а затем конвертируем
в кортеж, не забывая перенести каждый элемент в int(), ну вроде так было в примере.
На этом всё.
  
## Самостоятельная работа №3
### Ребята поспорили кто из них одним нажатием на numpad наберет больше повторяющихся цифр, но не понимают, как узнать
### Имеется файл input.txt с текстом на латинице. Напишите программу, которая выводит следующую статистику по тексту: количество букв ### латинского алфавита; число слов; число строк
### · Текст в файле:
### Beautiful is better than ugly.
### Explicit is better than implicit.
### Simple is better than complex.
### Complex is better than complicated.
### · Ожидаемый результат:
### Input file contains:
### 108 letters
### 20 words
### 4 lines

```python
def findTop3FrequentNumbers(number_string):
    number_counts = {}
    
    for char in number_string:
        number = int(char) 
        if number in number_counts:
            number_counts[number] += 1 
        else:
            number_counts[number] = 1
    
    sorted_counts = sorted(number_counts.items(), key=lambda item: item[1], reverse=True)

    top_3_counts = sorted_counts[:3]
    
    top_3_sorted = sorted(top_3_counts, key=lambda item: item[0])
    
    top_3_dict = {num: count for num, count in top_3_sorted}
    
    return top_3_dict

number_string_1 = '123456789123455555'
number_string_2 = '1234567890'
number_string_3 = '111111111222222223333333344444444444444444444444444'
print(f"Тест со строкой: {number_string_1}\nРезультат: {findTop3FrequentNumbers(number_string_1)}")
print(f"Тест со строкой: {number_string_2}\nРезультат: {findTop3FrequentNumbers(number_string_2)}")
print(f"Тест со строкой: {number_string_3}\nРезультат: {findTop3FrequentNumbers(number_string_3)}")
```

### Результат

![Меню](https://github.com/NikWither/universityProjects/blob/Тема_6/pic/cp3.jpg)

### Выводы

В функции findTop3FrequentNumbers() создадим пустой словарь для подсчета количества каждой цифры, а затем будем пробегаться по
строке из цифр. Увеличиваем счетчик каждого значения по ключу в словаре. Затем преобразуем словарь в список кортежей (ключ, значение) и сортируем по количеству (значению) с помощью lambda функции. После применяем встроенную сортировку и срез, сставляя только три самых частых числа. Затем снова сортируем по ключам (числам) в порядке возрастания, потом преобразовываем в словарь.
  
## Самостоятельная работа №4
### Никто не любит получать плохие оценки, поэтому Борис решил это исправить. Допустим, что все оценки студента за семестр хранятся в одном списке. Ваша задача удалить из этого списка все двойки, а все
### Ваш хороший друг владеет офисом со входом по электронным картам, ему нужно чтобы вы написали программу, которая показывала в каком порядке сотрудники входили и выходили из
### офиса. Определение сотрудника происходит по id. Напишите функцию, которая на вход принимает кортеж и случайный элемент (id), его можно придумать самостоятельно. Требуется вернуть
### новый кортеж, начинающийся с первого появления элемента в нем и заканчивающийся вторым его появлением включительно. Если элемента нет вовсе – вернуть пустой кортеж. 
### Если элемент встречается только один раз, то вернуть кортеж, который начинается с него и идет до конца исходного.
### Входные данные:
### (1, 2, 3), 8)
### (1, 8, 3, 4, 8, 8, 9, 2), 8)
### (1, 2, 8, 5, 1, 2, 9), 8)
### Ожидаемый результат:
### ()
### (8, 3, 4, 8)
### (8, 5, 1, 2, 9)
  
```python
def transformToList(tpl):
    return (tpl.split('),')[0])[1:].split(', ')

def getFinderElement(tpl):
    return str(tpl[-2])

def findEmployer(tplForUpdate):
    lst = transformToList(tplForUpdate)
    finderElement = getFinderElement(tplForUpdate)
    if lst.count(finderElement) == 0:
        return ()
    if lst.count(finderElement) == 1:
        newArray = lst[lst.index(finderElement):]
        return tuple(list(map(int, newArray)))
    else:
        count = 0
        startAndEndEmployer = ''
        for i in range(len(lst)):
            if lst[i] == finderElement and count != 2:
                count += 1
                startAndEndEmployer += str(i)
        startJob = int(startAndEndEmployer[0])
        endJob = int(startAndEndEmployer[1])
        newArray = lst[startJob:endJob + 1]
        return tuple(list(map(int, newArray)))
    
tpl_1 = '(1, 2, 3), 8)'
tpl_2 = '(1, 8, 3, 4, 8, 8, 9, 2), 8)'
tpl_3 = '(1, 2, 8, 5, 1, 2, 9), 8)'
        
print(f"\nРезультат: {findEmployer(tpl_1)}")
print(f"\nРезультат: {findEmployer(tpl_2)}")
print(f"\nРезультат: {findEmployer(tpl_3)}")
```

### Результат

![Меню](https://github.com/NikWither/universityProjects/blob/Тема_6/pic/cp4.jpg)

### Выводы

Имеем уже знакомые функции transformToList() и getFinderElement() из СР2. Повторюсь: получаем массив, с которым удобно работать, а также
число, с которым надо работать. Если необходимого id сотрудника нет в массиве (используем метод count() ), нет смысла что-то делать ещё, поэтому сразу возвращаем пустой кортеж. Если встречается 1 раз, то находим индекс числа, создаем новый массив (срез со старого от 
индекса элемента id сотрудника), конвертируем привычным методом из СР2 массив в кортеж и возвращаем.
Если же два прошлых варианта не подошло, значит имеем как минимум 2 вхождения заданных интервалов. Проходимся по массиву, как только
нашли 2 нужных элемента, то запоминаем их индексы и прекращаем поиск. Создаем нвоый массив при помощи срезов (по индексам, которые нашли
до этого) и возвращаем его в виде кортежа (используя сочетание методов из СР2, спасибо ей за это).
  
## Самостоятельная работа №5

### Самостоятельно придумайте и решите задачу, которая будет взаимодействовать с текстовым файлом.

```python
def analyze_grades(students_grades):
    
    total_grades = 0 # сумма всех баллов

    # проходимся по каждому студенту
    for student in students_grades:
        # из каждого элемента (кортежа) забираем балл студента
        name, grade = student
        
        total_grades += grade

    average_grade = total_grades / len(students_grades) # поиск ср. арф. балла
    
    above_average_students = [] # студенты, чьи баллы выше ср. арф.
    for student in students_grades:
        name, grade = student
        
        if grade > average_grade:
            # если балл выше ср. арф., добавляем имя студента в новый список
            above_average_students.append(name)

    count_above_average = len(above_average_students)

    return (above_average_students, average_grade, count_above_average)

# Тест 1
students_grades_1 = [("Nikita", 85), ("Oleg", 70), ("Tamara", 95), ("Svetlana", 80)]
print(analyze_grades(students_grades_1))

# Тест 2
students_grades_2 = [("Valentina", 60), ("Durak", 65), ("Bob", 70), ("Kopatich", 75)]
print(analyze_grades(students_grades_2))

# Тест 3
students_grades_3 = [("Крош", 100), ("Ёжик", 90), ("Змей Горыныч", 80), ("какой-то мужик", 70), ("чувак", 60)]
print(analyze_grades(students_grades_3)) 
```

### Результат

![Меню](https://github.com/NikWither/universityProjects/blob/Тема_6/pic/cp5.jpg)

### Выводы

Работаем в функции analyze_grades, в которой инициализируем переменную total_grades, которая будет хранить сумму всех баллов.
Затем, используя цикл for, перебираем каждого студента в списке. Каждый студент представлен кортежем, где первый элемент — имя, а второй — его оценка.
Мы берем только оценку и добавляем её к общей сумме total_grades.
После этого делим сумму всех баллов на количество студентов для получения средней оценки.
Потом создаем список студентов с оценками выше среднего, далее, снова используя цикл, перебираем каждого студента.
Для каждого студента проверяем, если его баллы выше среднего, то в этом случае добавляем его имя в новый список.

## Общие выводы по теме

Словари и кортежи — это структуры данных в Python, с помощью которых можно эффективно хранить и обрабатывать информацию.
Словарь — это коллекции, которые хранят данные в виде пар "ключ-значение". Ключи должны быть уникальными и неизменяемыми, а значения могут быть любыми типами данных.
Когда актуально: словари полезны, когда требуется быстро находить значения по ключам (например, как в задачи из ЛР1 про аудитории, хранение параметров). Также словари имеют низкую алгоритмическую сложность.
Кортеж — это неизменяемая последовательность элементов, упорядоченная по индексам. В отличие от списков, кортежи нельзя изменять после создания, что делает их более защищенными и удобными для случаев, когда данные должны оставаться неизменными, этакие константы
Когда использовать: Кортежи полезны, когда нужно хранить неизменяемые наборы данных (например, координаты точек)
Словари отлично подходят для хранения ассоциативных данных, где нужно быстро находить значения по ключам, а кортежи удобны для передачи неизменяемых наборов данных и для создания ключей в словарях (так как они неизменяемы).
