def sum_integers_in_file(filename):
    total_sum = 0

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            for line in file:
                # Разбиваем строку на слова и ищем целые числа
                for word in line.split():
                    # Пытаемся преобразовать слово в целое число
                    try:
                        number = int(word)  # Преобразуем в целое число
                        total_sum += number
                    except ValueError:
                        continue  # Если не удалось преобразовать, просто пропускаем

        print(f"Сумма найденных целых чисел: {total_sum}")

    except FileNotFoundError:
        print("Файл не найден. Пожалуйста, проверьте имя файла.")

# Запуск программы
if __name__ == "__main__":
    sum_integers_in_file('grades.txt')
