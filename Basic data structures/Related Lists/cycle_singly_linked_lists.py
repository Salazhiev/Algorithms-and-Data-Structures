# Создаем класс узлов наших
class Node:
    def __init__(self, val: int, next=None) -> None:
        self.val = val
        self.next = next


class cycle_singly_LinkedList:
    lens = 0

    def __init__(self, root: Node) -> None:
        self.root = root
        self.lens += 1

    # Добавление узла в конец
    def adding_to_the_end(self, val: int) -> None:
        self.lens += 1

        current = self.root
        if current==None:
            self.root = Node(val=val)
            return

        while current.next:
            current = current.next
        node = Node(val=val)
        current.next = node
        # ?????????????????????????????????????????????
        #node.next = self.root
        return


l = cycle_singly_LinkedList(Node(10))
l.adding_to_the_end(11)
l.adding_to_the_end(12)
l.adding_to_the_end(13)
l.adding_to_the_end(14)
print(1)



