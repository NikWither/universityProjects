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
        text = file.read()

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
   // count_words('DigitalRuble.txt')

```

### Результат

Создаем функцию count_words(filename), которая принимает в качестве аргумента название файла. Считываем текст из файла и кладем его в 
переменную текст text, а затем в новой переменной word делаем split()
Также имеется словарь word_count, в котором будут хранится все слова в виде ключа, а значение - количество повторений этого слова.
по циклу считаем количество слов, записываем их в словарь. Далее выводим с помощью функции len() кол-во слов, затем выводим часто встречающие слово и кол-во его повторв.

## Консоль

![Меню](https://github.com/NikWither/universityProjects/blob/Тема_7/img/cp1.jpg)

## Текст и самое часто встречающее слово (пруф)

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
                total += int(amount)  # суммирую расходы
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

## Добавление расхода (пункт 1), а также пример ввода данных.
![Меню](https://github.com/NikWither/universityProjects/blob/Тема_7/img/cp2.jpg)

## Вывод всех расходов (лист (пункт 2)).
![Меню](https://github.com/NikWither/universityProjects/blob/Тема_7/img/cp2_1.jpg)

## Подсчет всех расходов (пункт 3). Дополнительный пункт
![Меню](https://github.com/NikWither/universityProjects/blob/Тема_7/img/cp2_2.jpg)

## Выход из прогарммы (пункт 4).
![Меню](https://github.com/NikWither/universityProjects/blob/Тема_7/img/cp2_3.jpg)

### Выводы

С помощью функции def add_expense(filename), которая принимает название файла в качестве аргумента мы получаем ввод данных и записываем его в тхт документ. Тут всё просто - 3 инпута, 1 запись. (дата, категория, сумма)

Далее функция def view_expenses(), в которйо я вставил конструкцию try/catch (except) (привет запросы к базам данных), в try пытаемся прочитать файл (тут всё просто, проходимся по циклу и собираем все данные), а также except, который отлавливает ошибку на то, что не сможет открыть файл (нет в директории), в питоне есть встроенная функция, которая это отлавливает FileNotFoundError
P.S. может не так уж и уместно тут это вставлять, но захотелось поиграть, на питоне такого не делал

Также добавил дополнительную функцию (не удержался, этого УЖ СИЛЬНО не хватает) calculate_total_expenses(), здесь необходимо
подсчитать полную стоимость всех расходов. Аналично через try/except пытаемся открыть файл и отлавливаем ошибку. Т.к. у нас в каждой
строке 3 переменных, то применем прием деструк... короче не помню как он называется! Но работает следующим образом, например
в строке есть 3 числа (3, 6, 10), можно сделать так a, b, c = эта строка, тогда a = 3, b = 6, c = 10. Ну, как-то так.

Ну есть функция main, хотя можно было бы сразу в if закинуть. Там все просто, while True, ну и программа будет работать, пока не выберем пункт 4, а пункт 4 ведет к break, после этого программа завершится.
  
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
def text_statistics(filename):
    letters_count = 0
    words_count = 0
    lines_count = 0
    
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            lines_count += 1 
            words_count += len(line.split()) 
            
            letters = [char for char in line]
            letters_count += len(letters)

    print(f"{letters_count} letters")
    print(f"{words_count} words")
    print(f"{lines_count} lines")

text_statistics('example.txt')

```

### Результат

![Меню](https://github.com/NikWither/universityProjects/blob/Тема_7/img/cp3.jpg)

## txt файл
![Меню](https://github.com/NikWither/universityProjects/blob/Тема_7/code/example.txt)

### Выводы

Здесь все проще после прошлого теста.. Есть 3 переменные, каждая из которых отвечает за строки, буквы и слова. Открываем файл, строки посчитать просто, по циклу делаем всегда += 1, далее слова подсчитываем с помощью функции len, и делаем внутри split, получаем массив слов его и закидываем в переменную. НУ и потом также просто считаем каждый символ.

Далее просто все выводим прямо из функции, а затем просто вызываем функцию в глобальной области видимости............

## Самостоятельная работа №4
  
```python

```

### Результат

### Выводы

## Самостоятельная работа №5

### Самостоятельно придумайте и решите задачу, которая будет взаимодействовать с текстовым файлом.
### Необходимо открыть файл, найти все числа в файле, а затем вернуть их сумму 

```python
def sum_integers_in_file(filename):
    total_sum = 0

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                for word in line.split():
                    try:
                        total_sum += int(word)
                    except ValueError:
                        continue 

        print(f"Сумма найденных чисел: {total_sum}")

    except FileNotFoundError:
        print("Файл не найден")

if __name__ == "__main__":
    sum_integers_in_file('grades.txt')

```

### Результат

![Меню](https://github.com/NikWither/universityProjects/blob/Тема_7/img/cp5.jpg)

# Файл с цифрами
![Меню](https://github.com/NikWither/universityProjects/blob/Тема_7/img/cp5_1.jpg)

# txt файл

![Меню](https://github.com/NikWither/universityProjects/blob/Тема_7/code/grades.txt)

### Выводы

Открываем файл через try и except, также используя встроенную except ошибку FileNotFoundError, далее прикольно было бы еще попробовать использовать try&except, если можем преобразовать символ (а мы там уже по циклам for все разбили до символов, смотрим КАЖДЫЙ символ в тексте), так вот, если смогли преобразовать символ в число (а у нас всё по умолчанию - строки), то круто, мы сделали из '5' число 5. ПРосто добавляем total_sum(), затем просто выводим все прямо из функции. 
Тут очень высокая вычислительная сложность и код неоптимизирован, но захотел еще попробовать try except в питоне. Туда можно вообще всякую дичь писать, как например пытаться преобразовать символ в число и не словить ошибку типизации) короче динамические ЯП это забавно.

## Общие выводы по теме

Работа с файлами в Python включает несколько основных этапов: открытие файла с помощью функции open(), чтение или запись данных в файл. Для чтения файла могут использоваться методы read(), readline(), readlines(), а для записи — write() и writelines() (не всё упоминалось, загуглил). Важным аспектом является выбор режима открытия файла, например, для чтения ("r"), записи ("w") или добавления данных ("a"), а также присутствует возможность добавления кодировки, но у нас везде ютф8. Для упрощения работы и автоматического закрытия файла можно использовать контекстный менеджер with.
Помимо этого, изучил try catch (except). Пользовался ими на языке PHP при  запросах к БД. Работает аналогично. Также присутствует возможность ловли отдельных ошибок, как например FileNotFoundError. 


