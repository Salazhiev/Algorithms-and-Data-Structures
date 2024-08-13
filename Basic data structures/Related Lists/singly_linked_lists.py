# Наша Нода, тоесть i-ый объект из всего связанного списка.
class Node:
    def __init__(self, val: int, next=None) -> None:
        self.val = val
        self.next = next

# Класс для управления всем связанные списком.
class singly_LinkedList:
    lens = 0 # Длина нашего связного списка
    # Инициализация конструктора класса
    def __init__(self, root: Node) -> None:
        # При инициализации класса, мы добавляем первую ноду
        self.root = root
        self.lens += 1


    # Добавление в конец ноду
    def adding_to_the_end(self, val: int) -> None:
        self.lens+=1


        tmp = self.root
        if tmp==None:
            self.root = Node(val=val)
            return
        while tmp.next:
            tmp = tmp.next
        tmp.next = Node(val=val)


    # Добавление узла в начало
    def adding_to_the_beginning(self, val: int) -> None:
        self.lens += 1

        node = Node(val=val)
        current = self.root
        node.next = current
        self.root = node


    # Добавление узла по номеру(после введенного номера), нумерация начинается с 1
    def adding_to_the_number(self, num: int, val: int) -> None or str:
        if num>self.lens or num<0:
            return 'Такого номера в списке нет'
        self.lens += 1
        if num==0:
            node = Node(val=val)
            node.next = self.root
            self.root = node
            return


        current = self.root
        while True:
            if num==1:
                node = Node(val=val)
                nexts = current.next
                current.next = node
                node.next = nexts
                return
            current = current.next
            num -= 1


    # Вывод на экран значений нодов
    def outputs(self) -> None:
        tmp = self.root
        if tmp==None:
            print("Элементов в списке нет!")
            return
        while tmp!=None:
            print(tmp.val, end=' ')
            tmp = tmp.next
        print()


    # Проверка наличия элемента по значению
    def search(self, val: int) -> bool:
        tmp = self.root
        while tmp:
            if tmp.val == val:
                return True
            tmp = tmp.next
        return False


    # Удаление элемента с конца
    def pop(self) -> None:
        if self.root==None: return

        tmp = self.root
        if tmp.next:
            while tmp.next.next:
                tmp = tmp.next
            tmp.next = None
        elif tmp:
            self.root = None
        self.lens-=1


    # Переворот за O(n)
    def reverse(self) -> None:
        prev = None # Предыдущий
        current = self.root # Этот

        while current!=None:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt

        self.root = prev


    # Получить узел по индексу, индексация начинается с 1
    def get_node_index(self, index: int) -> str or Node:
        if index>self.lens or index<=0:
            return "Такого индекса нет в списке"

        tmp = self.root
        for _ in range(index-1):
            tmp = tmp.next
        return tmp


    # Получить узел по значению
    def get_node_val(self, val: int) -> str or Node:
        current = self.root
        while current:
            if current.val==val:
                return current
            current = current.next
        return 'Нет узла с таким значением'


    # Удаление узла по индексу, индексация начинается с 1
    def remove_node_index(self, index: int) -> None:
        if index>self.lens or index<=0:
            print("Такого индекса нет в списке")
            return

        self.lens-=1
        if index==1:
            if self.lens==1:
                self.root = None
                return

            self.root = self.root.next
            return

        index_remove = 1
        prev = None
        current = self.root

        while current:
            if index_remove==index:
                prev.next = current.next
                return

            prev = current
            current = current.next
            index_remove+=1


    # Удаление узла по значению
    def remove_node_value(self, val: int):
        prev = None
        current = self.root

        self.lens-=1
        if current.val==val:
            self.root = self.root.next
            return

        while current:
            if current.val==val:
                prev.next = current.next
                return

            prev = current
            current = current.next

        self.lens+=1
        print('Нет узла с таким значением')

