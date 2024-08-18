class Node:
    def __init__(self, val: int, next=None, prev=None) -> None:
        self.val = val
        self.next = next
        self.prev = prev

class DoublyLinkedList:
    lens = 0

    def __init__(self, root: Node) -> None:
        self.root = root
        self.lens += 1

    # Добавление в конец ноду
    def adding_to_the_end(self, val: int) -> None:
        self.lens += 1

        current = self.root
        if current==None:
            self.root = Node(val=val)
        while current.next:
            current = current.next

        node = Node(val=val)
        current.next = node
        node.prev = current


    # Добавление узла в начало
    def adding_to_the_beginning(self, val: int) -> None:
        self.lens += 1

        node = Node(val=val)
        current = self.root
        node.next = current
        current.prev = node
        self.root = node

    # Добавление узла по номеру(после введенного номера), нумерация начинается с 1
    def adding_to_the_number(self, num: int, val: int) -> None or str:
        if num>self.lens: return "Такого номера нет"

        self.lens+=1
        if num==0:
            node = Node(val=val)
            self.root.prev = node
            node.next = self.root
            self.root = node
            return

        current = self.root
        while True:
            if num==1:
                node = Node(val=val)
                nexts = current.next
                current.next = node
                node.prev = current
                nexts.prev = node
                node.next = nexts

                return
            num-=1
            current = current.next


    # Вывод на экран значений нодов
    def outputs(self) -> None:
        current = self.root
        if current==None:
            print('Элементов в списке нет!')
            return
        while current:
            print(current.val, end=' ')
            current = current.next
        print()


    # Проверка наличия элемента по значению
    def search(self, val: int) -> bool:
        current = self.root
        while current:
            if current.val==val:
                return True
            current = current.next
        return False


    # Удаление элемента с конца
    def pop(self) -> None:
        current = self.root

        if current.next:
            while current.next.next:
                current = current.next
            current.next = None
        elif current:
            self.root = None
        else:
            return
        self.lens -= 1


    # Переворот
    def reverse(self) -> None:
        current = self.root
        while current:
            temp = current.next
            current.next = current.prev
            current.prev = temp

            if temp==None:
                self.root = current

            current = temp


    # Получить узел по индексу, индексация начинается с 1
    def get_node_index(self, index: int) -> str or Node:
        if index>self.lens or index<=0:
            return 'такого индекса нет в списке'

        current = self.root
        for _ in range(index-1):
            current = current.next
        return current


    # Получить узел по значению
    def get_node_val(self, val: int) -> str or Node:
        current = self.root
        while current:
            if current.val==val:
                return current
            current = current.next
        return 'Нет узла с таким значением'


    # Удаление узла по индексу, индексация начианается с 1
    def remove_node_index(self, index: int) -> None:
        if index>self.lens or index<=0:
            print('Такого индекса нет в списке')
            return

        self.lens -= 1
        if index==1:
            if self.lens==0:
                self.root = None
                return

            current = self.root
            current = current.next
            current.prev = None
            self.root = current
            return

        index_remove = 1
        prev = None
        current = self.root

        while current:
            if index_remove==index:
                if index_remove==self.lens+1:
                    prev.next=None
                else:
                    prev.next = current.next
                    current.next.prev = prev
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
            nxt = self.root.next
            if nxt==None:
                self.root = None
            else:
                self.root = nxt
                self.root.prev = None
            return

        while current:
            if current.val==val:
                prev.next = current.next
                if current.next!=None:
                    current.next.prev = prev
                return
            prev = current
            current = current.next

        self.lens+=1
        print('Нет узла с таким значением')