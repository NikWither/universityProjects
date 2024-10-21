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
