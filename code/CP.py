class Tomato:
    states = {0: 'отсутствует', 1: 'цветение', 2: "зеленый", 3: "красный"}

    def __init__(self, index):
        """Инициализация класса Tomato
        _index (integer) : уникальный индекс помидора
        _state (string) : текущая стадия созревания"""
        self._index = index
        self._state = self.states[0]
    
    def grow(self):
        """Переводит помидор на следующую стадию созревания"""
        # получаем список всех значений из словаря
        all_values_from_states = list(self.states.values())
        
        # а также возьмем все ключи
        all_keys_from_states = list(self.states.keys())
        
        # находим текущую стадию (значение)  
        current_state = all_values_from_states.index(self._state)
        
        # используем найденное значение для получение текущего ключа (шага стадии)
        current_key = all_keys_from_states[current_state]

        # проверка на то, не является ли текущая стадия последней
        if ((current_key + 1) > 3):
            return "помидор уже созрел, можно срывать"
        
        current_key += 1

        self._state = self.states[current_key]

        return f"Текущая стадия: {self._state}"
    
    def is_ripe(self):
        """Проверяет, созрел ли помидор"""
        # получаем список всех значений из словаря
        all_values_from_states = list(self.states.values())
        
        # находим текущую стадию (значение)  
        current_state = all_values_from_states.index(self._state)
        
        if (current_state == 3):
            return "помидор уже созрел, можно срывать"
        return "помидор ещё не созрел"
         

class TomatoBush():
    def __init__(self, tomatoesCount):
        """Инициализируем экземпляр класса TomatoBush
        tomatoes (list): список томатов """
        self._tomatoes = []
        for i in range(tomatoesCount):
            self._tomatoes.append(Tomato(i))
    
    def grow_all(self):
        """Заставляет все томаты на кусте перейти на следующую стадию созревания"""
        for tomato in self._tomatoes:
            tomato.grow()

    def all_are_ripe(self):
        """Проверяет, все ли томаты на кусте созрели"""
        countNotYeat = 0
        for tomato in self._tomatoes:
            if (tomato.is_ripe() == "помидор ещё не созрел"):
                countNotYeat += 1

        if countNotYeat > 0:
            return f"Не созрело ещё {countNotYeat} томатов"
        return f"Все томаты молодцы, красавцы созрели и готовы к сборке"
        
    def give_away_all(self):
        """Очищает список томатов после сбора урожая"""
        self._tomatoes = []
        return 'Теперь на кустах ничего нет, довольствуйтесь урожаем'
    
class Gardener:
    def __init__(self, name, plant):
        """Инициализация класса Gardener
        name (string) : имя садовника (публичное свойство)
        _plant (TomatoBush) : куст, за которым ухаживает садовник"""
        self.name = name
        self._plant = plant

    def work(self):
        """Заставляет садовника ухаживать за кустом, переводя томаты на следующую стадию"""
        self._plant.grow_all()
        print(f"Садовник {self.name} поработал, все томаты на кусте(ах) перешли на новый lvl")
    
    def harvest(self):
        """Собирает урожай, если все томаты созрели, иначе выводит предупреждение"""

        if (self._plant.all_are_ripe() == "Все томаты молодцы, красавцы созрели и готовы к сборке"):
            self._plant.give_away_all()
            print(f"Весь урожай собран")
        else:
            print(f"{self.name} считает, что не все томаты созрели, и он в этом прав")
    
    @staticmethod
    def knowledge_base():
        """Выводит справку по садоводству"""
        print("Добро пожаловать в эмулятор сбора урожая (помидоров, томатов, я по всякому там уже назвал)\n")
        print("____________________________________Наслаждайтесь игрой____________________________________")
        print("Документация для новичков:")
        print("Создание куста: newTomatoes = TomatoBush(tomatoesCount=n), где tomatoesCount - любое натуральное число")
        print("Создаем своего персонажа:  newGardener = Gardener(name, plant), где name - ваше имя, а plant - куст, который вы создали до этого")
        print("newGardener.work() - прокачиваем наши кусты (все помидоры и томаты растут)")
        print("newGardener.harvest() - собираем урожай с  кустов")
        print("___________________________________________________________________________________________\n")

# тесты
# 1. Выводим справку по садоводству
Gardener.knowledge_base()

# 2. Создайте объекты классов TomatoBush и Gardener
bush = TomatoBush(tomatoesCount=5)
gardener = Gardener(name="Иван", plant=bush)

# 3. Ухаживаем за кустом с помидорами
gardener.work()  # Переход на первую стадию для всех помидоров
gardener.work()  # Переход на вторую стадию

# 4. Пробуем собрать урожай, когда томаты еще не дозрели
gardener.harvest()  # Предупреждение, если помидоры не созрели полностью

# 5. Повторяем уход и собираем урожай, когда томаты созрели
gardener.work()  # Все томаты становятся красными
gardener.harvest()  # Урожай собирается



