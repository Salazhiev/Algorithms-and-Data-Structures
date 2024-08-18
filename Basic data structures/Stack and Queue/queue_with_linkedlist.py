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

    def add(self, val: int) -> None:
        self.lens += 1

        current = self.root
        if current==None:
            self.root = Node(val=val)
            return
        while current.next:
            current = current.next

        node = Node(val=val)
        current.next = node
        node.prev = current


    def pop(self):
        current = self.root

        if current.next:
            while current.next.next:
                current = current.next
            nodes = current.next
            self.lens -= 1
            current.next = None
            return nodes
        elif current:
            nodes = self.root
            self.root = None
            self.root -= 1
            return nodes



class Queue:
    items = None
    lens = 0

    def push(self, value) -> None:
        if self.lens>0:
            self.items.add(value)
        else:
            self.items = DoublyLinkedList(Node(val=value))
        self.lens += 1

    def pop(self):
        if self.lens>0:
            self.lens -= 1
            return self.items.pop()
        print('Список пуст!')

    def is_empty(self):
        if self.items == None:
            return True
        return self.items.root is None