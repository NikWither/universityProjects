class UserDecorator:
    """
    Класс-декоратор для добавления функциональности авторизованным пользователям
    """
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("=== Авторизация пользователя ===")
        # это типа эмуляция проверки авторизации
        is_authorized = kwargs.get('is_authorized', False)
        if is_authorized:
            print("вы успешно авторизованы")
            self.extra_features()  # добавление дополнительных возможностей
        else:
            print("Ограниченный доступ, авторизация не пройдена")
        return self.func(*args, **kwargs)

    def extra_features(self):
        """
        Дополнительные возможности для авторизованных пользователей.
        """
        print("Теперь доступны следующие действия:")
        print("- Ставить лайки")
        print("- Комментировать публикации")
        print("- Создавать свои записи")


# функция для работы неавторизованных пользователей
@UserDecorator
def browse_website(is_authorized=False):
    """
    Основная функция для работы с сайтом.
    """
    print("Вы просматриваете общедоступный контент.")

# функция для демонстрации работы декоратора, для авторизованных пользователей
@UserDecorator
def view_post(post_id, is_authorized=False):
    """
    Функция для просмотра публикации.
    """
    print(f"Вы смотрите публикацию с ID: {post_id}")


if __name__ == '__main__':
    print("\nТест 1, неавторизованный пользователь")
    browse_website(is_authorized=False)

    print("\nТест 2, авторизованный пользователь")
    browse_website(is_authorized=True)

    print("\nТест 3, просмотр публикации неавторизованным пользователем")
    view_post(post_id=101, is_authorized=False)

    print("\nТест 4, просмотр публикации авторизованным пользователем")
    view_post(post_id=102, is_authorized=True)
