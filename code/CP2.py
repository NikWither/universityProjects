import random

def play():
    move = random.randrange(1, 6) # randrange - метод для рандомного числа среди двух параметров
    print(f'Выпало: {move}')
    if move >= 5:
        print('Вы победили')
    elif 3 <= move <= 4:
        play()
    elif 1 <= move <= 2:
        print('Вы проиграли')


if __name__ == '__main__':
    play()