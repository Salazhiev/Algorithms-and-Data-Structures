class Node:
    def __init__(self, val: int, next=None, prev=None) -> None:
        self.val = val
        self.next = next
        self.prev = prev

# Циклический двусвязный список
class cycle_doubly_LinkedList:
    lens = 0
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.next = self.head
        self.head.prev = self.tail
        self.tail.prev = self.head

    def adding_to_the_end(self, val: int) -> None:
        self.lens += 1
        newNode = Node(val=val)
        if self.head.val ==  None:
            self.head = newNode
            self.tail = newNode

            newNode.next = self.head
            newNode.prev = self.head
        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
            self.tail.next = self.head
            self.head.prev = self.tail

    def adding_to_the_beginnig(self, val: int) -> None:
        self.lens += 1
        newNode = Node(val=val)
        if self.head.val==None:
            self.head = newNode
            self.tail = newNode

            newNode.next = self.head
            newNode.prev = self.head

        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode

            self.tail.next = self.head



    # Добавление узла по номеру(после введенного номера), нумерация начинается с 1
    def adding_to_the_number(self, num: int, val: int) -> None or str:
        if num>self.lens:
            num=self.lens
        elif num<0:
            num=0
        self.lens+=1
        newNode=Node(val=val)

        if num==0:
            if self.head.val==None:
                self.head = newNode
                self.tail = newNode
                newNode.next = self.head
                newNode.prev = self.head
            else:
                newNode.next = self.head
                self.head.prev = newNode
                self.head = newNode
                self.tail.next = self.head
                self.head.prev = self.tail
            return
        if num==self.lens-1:
            if self.head.val==None:
                self.head = newNode
                self.tail = newNode
                newNode.next = self.head
                newNode.prev = self.head
            else:
                self.tail.next = newNode
                newNode.prev = self.tail
                self.tail = newNode
                self.tail.next = self.head
                self.head.prev = self.tail
            return

        current = self.head
        while True:
            if num==1:
                nxt = current.next
                current.next = newNode
                newNode.prev = current
                newNode.next = nxt
                nxt.prev = newNode
                return

            current = current.next
            num -= 1
    def outputs(self):
        current = self.head
        if current.val==None:
            print('Элементов в списке нет!')
            return

        a = self.lens
        while a>0:
            print(current.val ,end=' ')
            a-=1
            current = current.next
        print()
    def upgrade_outputs(self, k: int):
        current = self.head
        if current.val==None:
            print('Элементов в списке нет!')

        print(f'Длина списка {self.lens}: => ', end='')
        a = self.lens * 2 + k
        while a>0:
            if self.head == current:
                print(f"head val:{current.val} --> ", end='')
            elif self.tail == current:
                print(f"tail val:{current.val} --> ", end='')
            else:
                print(f"alpha val:{current.val} --> ", end='')

            a-=1
            current = current.next

        print()

        print(f'Длина списка {self.lens}: => ', end='')
        a = self.lens * 2 + k
        while a>0:
            if self.head == current:
                print(f"head val:{current.val} <-- ", end='')
            elif self.tail == current:
                print(f"tail val:{current.val} <-- ", end='')
            else:
                print(f"alpha val:{current.val} <-- ", end='')

            a-=1
            current = current.prev

        print()

