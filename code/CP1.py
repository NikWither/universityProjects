from datetime import datetime
from math import sqrt


def main(**kwargs):
    """
    Высчитывает квадратный корень суммы квадратов двух элементов кортежей
    
    Args:
        kwargs: кортежи

    :return:
        float: квадратный корень суммы квадратов двух элементов кортежей
    """
    for key in kwargs.items():
        result = sqrt(key[1][0] ** 2 + key[1][1] ** 2)
        print(result)


if __name__ == '__main__':  # точка входа
    start_time = datetime.now()  # начинаем отсчет времени

    # запуск функции main и передача параметров kwargs
    main(
        one=[10, 3],
        two=[5, 4],
        three=[15, 13],
        four=[93, 53],
        five=[133, 15]
    )

    # подсчёт времени выполнения программы. Старт - начало времени
    time_costs = datetime.now() - start_time

    # выводит временя выполнялнения функции
    print(f"Время выполнения программы - {time_costs}")