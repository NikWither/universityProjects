def text_statistics(filename):
    letters_count = 0
    words_count = 0
    lines_count = 0
    
    # Открываем файл для чтения
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            lines_count += 1  # Увеличиваем количество строк
            words_count += len(line.split())  # Считаем количество слов
            
            # Шаг 1: Отфильтровать только буквы из строки
            letters = [char for char in line if char.isalpha()]
            
            # Шаг 2: Посчитать количество букв
            letters_count += len(letters)

    # Выводим результаты
    print(f"{letters_count} letters")
    print(f"{words_count} words")
    print(f"{lines_count} lines")

# Запуск программы
text_statistics('example.txt')
