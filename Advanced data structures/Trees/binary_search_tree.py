class Tree:
    def __init__(self, val=None):
        self.value = val
        if self.value:
            self.left = Tree()
            self.right = Tree()
            print(f'{self.value} is inserted successfully')
        else:
            self.left = None
            self.right = None



    # Проверка на присутсвие корневого листа.
    def isempty(self):
        return self.value == None



    # Проверка, является ли узел дерева конечным.
    def inorder(self):
        if self.isempty():
            return []
        return self.left.inorder() + [self.value] + self.right.inorder()



    # Вставка в бинарное дерево поиска
    def insert(self, data):
        # Если наше дерево полностью пусто.
        if self.isempty():
            self.value = data

            self.left = Tree()
            self.right = Tree()
            print(f'{self.value} is inserted successfully')

        elif data < self.value:
            self.left.insert(data)
        elif data > self.value:
            self.right.insert(data)


    # Поиск в бинарном дереве поиска.
    def find(self, data):
        if self.isempty():
            print(f'{data} is not found.')
            return False

        if self.value == data:
            print(f'{data} is found.')
            return True
        elif self.value > data:
            self.left.find(data)
        else:
            self.right.find(data)

    


t = Tree(20)
t.insert(15)
t.insert(25)
t.insert(8)
t.insert(16)
t.find(25)
print(t.inorder())
print()
