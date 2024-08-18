class Node:
    def __init__(self, val: int, next=None) -> None:
        self.val = val
        self.next = next

class SinglyLinkedList:
    lens = 0
    def __init__(self, root: Node) -> None:
        self.root = root
        self.lens += 1

    def add(self, val):
        self.lens+=1

        current = self.root
        if current==None:
            self.root = Node(val=val)
            return
        while current.next:
            current = current.next
        current.next = Node(val=val)

    def pop(self):
        if self.root==None: return

        current = self.root
        if current.next:
            while current.next.next:
                current = current.next

            nodes = current.next
            current.next = None
            self.lens-=1
            return nodes
        elif current:
            nodes = self.root
            self.root = None
            self.lens-=1
            return nodes


class Stack:
    items = None
    lens = 0

    def push(self, value):
        if self.lens>0:
            self.items.add(value)
        else:
            self.items = SinglyLinkedList(Node(val=value))
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