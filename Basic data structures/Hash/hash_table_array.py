# Реализация простой хеш-таблицы с помощью обычного списка.
# Важно понимать что это мини реализация dict()
class HashTable:
    # Инициализация количество элементов.
    lens = 0

    # Инициализация конструктора класса, на выходе получает аргумент
    # - количество бакетов, по умолчанию равно 100.
    def __init__(self, size=5):
        # Количество бакетов.
        self.size = size

        # Инициализация таблицы.
        self.table = [[] for _ in range(size)]



    # Функция для получения хеш-кода, принимает на вход ключ.
    def hash_function(self, key):
        # Вычисляем хеш-код с помощью встроенной функции.
        return hash(key) % self.size



    # Добавление элемента в нашу таблицу.
    def insert(self, key, value):
        # Вычисляем индекс бакета.
        hash_code = self.hash_function(key)

        # Проверка, нужно ли обновить количесто бакетов.
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
            # Если такой ключ существует, то мы просто меняем его значение на новое.
            if kv_pair[0] == key:
                # Сама непосредственно замена.
                kv_pair[1] = value
                # Завершение работы функции, так как все готово.
                return

        # Если ключ не найден, добавляем новую пару.
        self.table[hash_code].append( [key, value] )
        # Также увеличиваем количество пар на одну единицу.
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
                self.lens -= 1
                return True
        return False


    # Красивый вывод :)
    def __str__(self):
        result = 'HashTable contents:\n'
        for i, bucket in enumerate(self.table):
            if bucket:
                result += f'Index {i}: {bucket}\n'
        return result


h = HashTable()
h.insert('Иса', 20)
h.insert('Муса', 21)
h.insert('Адам', 50)
h.insert('Хава', 45)
h.insert('Иман', 16)
h.insert('Амина', 4)
h.remove('Амина')
h.remove('Иса')
h.remove('Адам')
print(h)
print(h.table)
print(h.get('Хава'))