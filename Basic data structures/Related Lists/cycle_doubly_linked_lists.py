class Node:
    def __init__(self, val: int, next=None, prev=None) -> None:
        self.val = val
        self.next = next
        self.prev = prev

# ВРОДЕ ВСЕ РАБОТАЕТ.
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

    def search(self, val: int) -> bool:
        current = self.head

        a = self.lens
        while a>-1:
            if current.val==val:
                return True
            current = current.next
            a-=1
        return False


    def pop(self) ->  None:
        if self.head.val == None:
            print('В списке нет элементов!')
            return

        if self.lens==1:
            self.head.val = None
            self.tail.val = None
            self.lens = 0
            return

        self.lens -= 1

        current = self.head
        while current.next != self.tail:
            current = current.next

        current.next = self.head
        self.tail = current
        self.head.prev = self.tail
        self.tail.next = self.head

    def reverse(self) -> None:
        prev = self.tail
        current = self.head
        a = self.lens
        while a>0:
            if a==self.lens:
                self.tail = current
            nxt = current.next
            current.next = prev
            prev.prev = current
            prev = current
            current = nxt
            a-=1
        self.head = prev

    def get_node_index(self, index: int) -> str or Node:
        if index>self.lens or index <= 0:
            return 'Такого индекса нет в списке'

        current = self.head
        for _ in range(index-1):
            current = current.next
        return current

    def get_node_value(self, val: int) -> str or Node:
        current = self.head

        for _ in range(self.lens):
            if current.val==val:
                return current
            current = current.next
        return 'Нет узла с таким значением'


    def remove_node_index(self, index: int) -> None:
        if index>self.lens or index<=0:
            print('Такого иднекса нет в списке')
            return

        if index==1:
            if self.lens == 1:
                self.head.val=None
                self.tail.val=None
            else:
                self.head = self.head.next
                self.head.prev = self.tail
                self.tail.next = self.head
            self.lens -= 1
            return

        prev = None
        check = index
        current = self.head
        while index-1>0:
            prev = current
            current = current.next
            index -= 1

        prev.next = current.next
        current.next.prev = prev
        if self.lens==check:
            self.tail = prev
        self.lens -= 1

    def remove_node_value(self, val: int) -> None:
        prev = None
        current = self.head
        check = self.lens
        self.lens-=1
        if current.val==val:
            if self.lens > 0:
                self.head = self.head.next
                self.head.prev = self.tail
                self.tail.next = self.head
            else:
                self.head.val = None
                self.tail.val = None
                self.head.next = self.tail
                self.tail.next = self.head
                self.head.prev = self.tail
                self.tail.prev = self.head

            return

        while check>0:
            if current.val==val:
                if check==1:
                    self.tail = prev
                    self.tail.next = self.head
                    self.head.prev = self.tail
                else:
                    prev.next = current.next
                    current.next.prev = prev
                return

            prev = current
            current = current.next
            check -= 1

        self.lens+=1
        print('Нет узла с таким значением!')