class Node:
    def __init__(self, val, next=None) -> None:
        self.val = val
        self.next = next

class SinglyLinkedList:
    lens = 0
    def __init__(self, root=None) -> None:
        self.root = root
        if self.root != None:
            self.lens += 1


    # Добавление ноды.
    def add(self, val) -> None:
        self.lens += 1

        current = self.root
        if current==None:
            self.root = Node(val=val)
            return
        while current.next:
            current = current.next
        current.next = Node(val=val)

    # Удаление ноды по значению.
    def remove(self, val) -> None:
        prev = None
        current = self.root

        self.lens -= 1
        if current.val == val:
            self.root = self.root.next
            return

        while current:
            if current.val == val:
                prev.next = current.next
                return

            prev = current
            current = current.next
        self.lens += 1
        print('Нет узла с таким значением!')

    # Проверка есть ли такой элемент в списке.
    # Проверка проходит по значениям.
    def search(self, val) -> bool:
        current = self.root
        while current:
            if current.val==val:
                return True
            current = current.next
        return False

    # Поочередное получение значений в узлах.
    def get(self):
        result = []
        current = self.root
        while current:
            result.append(current.val)
            current = current.next
        return result


    # Вывод на экран значений нодов
    def outputs(self) -> None or str:
        result = ''

        current = self.root
        if current==None:
            return
        while current!=None:
            result += current.val + ' '
            current = current.next
        return result


class HashSetLinkedList:
    lens = 0
    def __init__(self, size=3) -> None:
        self.size = size
        self.table = [SinglyLinkedList() for _ in range(size)]


    def hash_function(self, value):
        return hash(value) % self.size


    def add(self, value):
        hash_code = self.hash_function(value)

        # Проверяем наличия элемента, которого мы хотим добавить.
        if self.table[hash_code].search(value)==False:
            if self.lens==self.size:
                self.size *= 2
                self.new_table = [SinglyLinkedList() for _ in range(self.size)]


                for backet in self.table:
                    for val in backet.get():
                        hash_code_val = self.hash_function(val)
                        self.new_table[hash_code_val].add(val)

                self.table = self.new_table

            self.table[hash_code].add(value)
            self.lens += 1
        else:
            print('Такой элемент уже существует!')



    def contains(self, value) -> bool:
        hash_code = self.hash_function(value)

        return self.table[hash_code].search(value)



    def remove(self, value):
        hash_code = self.hash_function(value)

        if self.table[hash_code].search(value)==True:
            self.table[hash_code].remove(value)
            self.lens -= 1
        else:
            print('В хеш-множестве нет такого элемента к сожалению!')


    def __str__(self):
        result = 'Linkedlist contents:\n'
        for i, bucket in enumerate(self.table):
            if bucket.lens > 0:
                result += f'Index {i}: {bucket.outputs()}'
        return result



h = HashSetLinkedList()
h.add('Иса')
h.add('Муса')
h.add('Лала')
h.add('Адам')
print(h.contains('Л'))
print(h.contains('Иса'))
h.remove('l')
h.remove('Иса')
print()