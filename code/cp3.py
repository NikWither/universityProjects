# Класс Tomato, представляющий помидор с возможностью созревания
class Tomato:
    # Статическое свойство states, описывающее стадии созревания помидора
    states = {0: 'отсутствует', 1: 'цветение', 2: 'зеленый', 3: 'красный'}

    def __init__(self, index):
        """Инициализация экземпляра класса Tomato
        _index (int): уникальный индекс помидора
        _state (str): текущая стадия созревания, инициализируется первым значением из states"""
        self._index = index
        self._state = Tomato.states[0]

    def grow(self):
        """Переводит помидор на следующую стадию созревания"""
        current_stage = list(Tomato.states.keys())[list(Tomato.states.values()).index(self._state)]
        if current_stage < 3:
            self._state = Tomato.states[current_stage + 1]

    def is_ripe(self):
        """Проверяет, созрел ли помидор (стадия 'красный')"""
        return self._state == Tomato.states[3]


# Класс TomatoBush, представляющий куст с помидорами
class TomatoBush:
    def __init__(self, num_tomatoes):
        """Инициализация экземпляра класса TomatoBush
        tomatoes (list): список томатов на кусте"""
        self.tomatoes = [Tomato(i) for i in range(num_tomatoes)]

    def grow_all(self):
        """Заставляет все томаты на кусте перейти на следующую стадию созревания"""
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self):
        """Проверяет, все ли томаты на кусте созрели"""
        return all(tomato.is_ripe() for tomato in self.tomatoes)

    def give_away_all(self):
        """Очищает список томатов после сбора урожая"""
        self.tomatoes = []


# Класс Gardener, представляющий садовника, ухаживающего за растением
class Gardener:
    def __init__(self, name, plant):
        """Инициализация экземпляра класса Gardener
        name (str): имя садовника (публичное свойство)
        _plant (TomatoBush): куст, за которым ухаживает садовник"""
        self.name = name
        self._plant = plant

    def work(self):
        """Заставляет садовника ухаживать за кустом, переводя томаты на следующую стадию"""
        self._plant.grow_all()
        print(f"{self.name} поработал, все томаты на кусте перешли на следующую стадию созревания.")

    def harvest(self):
        """Собирает урожай, если все томаты созрели, иначе выводит предупреждение"""
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print(f"{self.name} собрал урожай.")
        else:
            print("Не все томаты созрели, пока рано собирать урожай.")

    @staticmethod
    def knowledge_base():
        """Выводит справку по садоводству"""
        print("Справка по садоводству: ухаживайте за растениями, поливайте их, следите за стадиями созревания.")


# Тесты
# 1. Выводим справку по садоводству
Gardener.knowledge_base()

# 2. Создаем объекты классов TomatoBush и Gardener
bush = TomatoBush(num_tomatoes=5)
gardener = Gardener(name="Иван", plant=bush)

# 3. Ухаживаем за кустом с помидорами
gardener.work()  # Переход на первую стадию для всех помидоров
gardener.work()  # Переход на вторую стадию
gardener.work()  # Переход на третью стадию

# 4. Пробуем собрать урожай, когда томаты еще не дозрели
gardener.harvest()  # Предупреждение, если помидоры не созрели полностью

# 5. Повторяем уход и собираем урожай, когда томаты созрели
gardener.work()  # Все томаты становятся красными
gardener.harvest()  # Урожай собирается
