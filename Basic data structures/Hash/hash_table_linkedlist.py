class Node:
    def __init__(self, kv_pair, next=None):
        # Ключ-значение.
        self.key, self.value = kv_pair
        self.next = next

class SinglyLinkedList:
    lens = 0
    def __init__(self, root=None) -> None:
        self.root = root
        if self.root != None:
            self.lens += 1

    # Добавление по ключ-значение.
    def add(self, kv_pair):
        self.lens += 1

        current = self.root
        if current==None:
            self.root = Node(kv_pair)
            return
        while current.next:
            current = current.next
        current.next = Node(kv_pair)


    # Удаление по ключу
    def remove(self, key):
        prev = None
        current = self.root

        self.lens -= 1
        if current.key == key:
            self.root = self.root.next
            return True

        while current:
            if current.key==key:
                prev.next = current.next
                return True
            prev = current
            current = current.next
        self.lens += 1
        return False


    # Проверка есть ли такой ключ в списке
    def search(self, key):
        current = self.root
        while current:
            if current.key==key:
                return True
            current = current.next
        return False


    # Поочередное получение пар в узлах
    def get(self):
        result = []
        current = self.root
        while current:
            result.append( (current.key, current.value) )
            current = current.next
        return result


    # Замена значения по ключу.
    def change(self, kv_pair):
        key, val = kv_pair

        current = self.root
        while current:
            if current.key==key:
                current.val = val
                return
            current = current.next


    # Функция для получения значения по ключу.
    def get_value(self, key):
        current = self.root
        while current:
            if current.key==key:
                return current.val
            current = current.next



class HashTableLinkedList:
    lens = 0
    def __init__(self, size=3) -> None:
        self.size = size
        self.table = [SinglyLinkedList() for _ in range(size)]

    def hash_function(self, key):
        return hash(key) % self.size

    def add(self, kv_pair):
        key, value = kv_pair
        hash_code = self.hash_function(key)


        # Проверка нужно ли увеличить длину бакетов.
        if self.lens == self.size:

            self.size *= 2
            self.new_table = [SinglyLinkedList() for _ in range(self.size)]

            for backet in self.table:
                for k, v in backet.get():
                    hash_code_key = self.hash_function(k)
                    self.new_table[hash_code_key].add( (k,v) )

            self.table = self.new_table


        # Проверяем, существует ли ключ в таблице
        kv_ = self.table[hash_code].get()
        for k,_ in kv_:
            # Если он существует то просто заменяем его значением на новое
            if key==k:
                self.table[hash_code].change( (key, value) )
                return

        # Если клчу нет в нашей таблице, то просто добавляем новый
        self.table[hash_code].add( (key, value) )
        self.lens += 1

    # Функция для получения значения по ключу.
    def get(self, key):
        hash_code = self.hash_function(key)

        return self.table[hash_code].get_value(key)


    # Удаление по ключу
    def remove(self, key):
        hash_code = self.hash_function(key)

        if self.table[hash_code].remove(key):
            self.lens -= 1
            return True
        return False



l = HashTableLinkedList()
l.add(('Иса',20))
l.add(('Муса', 21))
l.add(('Зава', 23))
l.add(('ds', 41))
print()