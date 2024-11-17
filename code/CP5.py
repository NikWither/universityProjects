class InvalidAgeError(Exception):
    """
    Исключение для случаев, когда возраст пользователя некорректен.
    """
    def __init__(self, age, message="Возраст должен быть от 18 лет."):
        self.age = age
        self.message = message
        super().__init__(f"Ошибка: {message} (Ваш возраст: {age})")

def get_alchohol_or_cigarettes(age):
    if age <= 18:
        raise InvalidAgeError(age)
    print(f"Держите и алкоголь, и сигареты, все продадим, ведь вам уже {age} лет")

if __name__ == '__main__':
    try:
        print("Тест 1, некорректный возраст")
        get_alchohol_or_cigarettes(15) 
    except InvalidAgeError as err:
        print(err)

    try:
        print("\nТест 2, корректный возраст")
        get_alchohol_or_cigarettes(25)
    except InvalidAgeError as err:
        print(err)