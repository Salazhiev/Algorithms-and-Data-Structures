# Реализация простой хеш-таблицы с помощью обычного списка.
# Важно понимать что это мини реализация dict()
class HashTable:
    # Инициализация количество элементов.
    lens = 0

    # Инициализация конструктора класса, на выходе получает аргумент
    # - количество бакетов, по умолчанию равно 100.
    def __init__(self, size=10):
        # Количество бакетов.
        self.size = size

        # Инициализация таблицы.
        self.table = [[] for _ in range(size)]



    # Функция для получения хеш-кода, принимает на вход ключ.
    def hash_function(self, key):
        return hash(key) % self.size



    # Добавление элемента в нашу таблицу.
    def insert(self, key, value):
        # Вычисляем индекс бакета.
        hash_code = self.hash_function(key)

        # Проверка, нужно ли обновить количесто бакетов
        if self.lens==self.size:
            # Если все же нужно обновить, то новый размер количеств бактов, увеличивается
            # в два раза.
            self.size *= 2

            # Инициализация новой таблицы с новой длиной.
            self.new_table = [[] for _ in range(self.size)]

            # Запонение новой таблицы элементами со старой.
            for backet in self.table:
                for kv_pair in backet:
                    hash_code_key = self.hash_function(kv_pair[0])
                    self.new_table[hash_code_key].append( [kv_pair[0], kv_pair[1]] )

            # Замена старой таблицы на новую.
            self.table = self.new_table


        # Проверяем, существует ли ключ в таблице
        for kv_pair in self.table[hash_code]:
            if kv_pair[0] == key:
                kv_pair[1] = value
                return

        # Если ключ не найден, добавляем новую пару.
        self.table[hash_code].append([key, value])
        self.lens += 1


    # Функиця для получения значения по ключу.
    def get(self, key):
        # Получение хеш-кода ключа.
        hash_code = self.hash_function(key)

        # Проходимся по бакету и когда натыкаемся на нужный ключ, возвращаем его.
        for kv_pair in self.table[hash_code]:
            if kv_pair[0] == key:
                return kv_pair[1]

        # При отсутствии такого ключа возвращаем пустоту.
        return None


    # Удаление элемента по ключу.
    def remove(self, key):
        hash_code = self.hash_function(key)

        for i, kv_pair in enumerate(self.table[hash_code]):
            if kv_pair[0] == key:
                del self.table[hash_code][i]
                return True

        return False

    # Красивый вывод :)
    def __str__(self):
        result = ''
        for i, bucket in enumerate(self.table):
            if bucket:
                result += f'Index {i}: {bucket}\n'
        return result