# Реализация простого хеш-множества с помощью обычного списка.
# Важно понимать что это мини реализация set()
class HashSet:
    # Инициализация количество элементов.
    lens = 0

    # Инициализация конструктора класса, на выходе получает аргумент
    # - количество бакетов, по умолчанию равно 100.
    def __init__(self, size=5) -> None:
        # Количество бакетов.
        self.size = size

        # Инициализация массива при инициализации
        # класса(i-ый элемент массива это бакет).
        # Количество бакетов равно длине массива.
        self.table = [[] for _ in range(size)]



    # Функция для получения хеш-кода, для значения добавляемого
    # в наше хеш-множество. Для каждого значение оно уникально.
    def hash_function(self, value) -> hash:
        # Преобразуем значение в строку и вычисляем хеш
        return hash(value) % self.size


    # Функция для добавления элемента в наше хеш-множество.
    def add(self, value) -> None:
        # Вычисляем индекс бакета.
        hash_code = self.hash_function(value)

        # Проверяем, есть ли значение в бакете, если нет добавляем его.
        if value not in self.table[hash_code]:
            # Проверка, нужно ли увеличивать количество бакетов.
            if self.lens==self.size:
                # Создаем массив на х2 бакетов
                self.size *= 2
                self.new_table = [[] for _ in range(self.size)]

                # Вставка всех текущих элементов со старого массива в новый.
                # Берем каждый бакет.
                for backet in self.table:
                    # Берем элементы с каждого бакета.
                    for val in backet:
                        # Вычисляем хеш-код для элемента с выбранного бакета.
                        hash_code_val = self.hash_function(val)
                        # Добавляем значение по его хеш-коду в новый массив.
                        self.new_table[hash_code_val].append(val)

                # Замена старого массива на новый
                self.table = self.new_table

            # Вставка нового элемента в множество.
            self.table[hash_code].append(value)
            # Увилечение количества элементов в множестве.
            self.lens += 1
        else:
            # Если у нас уже есть такой элемент в выбранном бакете, то очевидно такой элемент уже существует.
            print('Такой элемент уже существует!')


    # Проверка наличия значения в хеш-множестве.
    def contains(self, value) -> bool:
        # Вычисление хеш-ключа.
        hash_code = self.hash_function(value)

        # Проверяем наличие элемента в нашем массиве.
        return value in self.table[hash_code]


    # Удаление элемента.
    def remove(self, value) -> None:
        # Вычисление хеш кода.
        hash_code = self.hash_function(value)

        # Удаляем значению, если он присутсвует в нашем множестве.
        if value in self.table[hash_code]:
            self.table[hash_code].remove(value)
        else:
            print('В Хеш-Множестве нет такого значения!')


    # Вывод все на экран.
    def __str__(self) -> str:
        # Отображение содержимого множества для удобства.
        result = "HashSet contents:\n"
        for i, bucket in enumerate(self.table):
            if bucket:
                result += f"Index {i}: {bucket}\n"
        return result

h = HashSet()
h.add('Иса')
h.add('Муса')
h.add('Адам')
h.add('Хава')
h.add('Иман')
h.add('Амина')
print(h, end='\n\n')
print(h.table)