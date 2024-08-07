# Наша Нода, тоесть i-ый объект из всего связанного списка.
class Node:
    def __init__(self, val: int, next=None) -> None:
        self.val = val
        self.next = next



# Класс для управления всем связанные списком.
class LinkedList:
    lens = 0 # Длина нашего связного списка
    # Инициализация конструктора класса
    def __init__(self, root: Node) -> None:
        # При инициализации класса, мы добавляем первую ноду
        self.root = root
        self.lens += 1



    # Добавление в конец ноду
    def append(self, val: int) -> None:
        self.lens+=1

        # Сохранение главного элемента
        tmp = self.root
        while tmp.next:
            tmp = tmp.next
        tmp.next = Node(val=val)



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




    # Поиск элемента
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



    # Переворот за O(n)
    def reverse(self) -> None:
        prev = None # Предыдущий
        current = self.root # Этот

        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt

        self.root = prev


    # Получить узел по индексу, индексация начинается с 1
    def get_node(self, index: int) -> str or int:
        if index>self.lens or index<=0:
            return "Такого индекса нет в списке"

        tmp = self.root
        for _ in range(index-1):
            tmp = tmp.next
        return tmp.val



    # Удаление узла по индексу, индексация начинается с 1
    def remove_node(self, index: int):
        if index>self.lens or index<=0:
            return "Такого индекса нет в списке"



ll = LinkedList( root=Node(10) )
ll.append(11)
ll.append(12)
ll.outputs()
ll.remove_node(1)
ll.outputs()