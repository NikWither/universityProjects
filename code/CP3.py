def try_add_two():
    try:
        user_input = input("введите число: ")
        number = float(user_input)
        result = 2 + number
        print(f"Результат: {result}")
    except ValueError:
        print("неподходящий тип данных, ожидалось число")


if __name__ == '__main__':
    try_add_two()
    try_add_two()
    try_add_two()
    try_add_two()