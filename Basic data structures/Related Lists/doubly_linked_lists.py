class Node:
    def __init__(self, val: int, next=None, prev=None) -> None:
        self.val = val
        self.next = next
        self.prev = prev


class LinkedList:
    lens = 0

    def __init__(self, root: Node) -> None:
        self.root = root
        self.lens += 1

    # Добавление в конец ноду
    def adding_to_the_end(self, val: int) -> None:
        self.lens += 1

        current = self.root
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

    # Добавление узла по индексу
    # ------



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
    # def pop(self) -> None:
    #     if self.root==None: return




ll = LinkedList(Node(10))
ll.adding_to_the_end(11)
print()