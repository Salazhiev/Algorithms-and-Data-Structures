# Создание класса, для управления и создания дерева.
class Tree:
    def __init__(self, val=None):
        # Присваиваем значение узлу.
        self.value = val
        # Если значение реально было присвоено, создаем правый и левый узел
        if self.value:
            self.left = Tree()
            self.right = Tree()
            print(f'{self.value} is inserted successfully')
        else:
            # Если нет значения у узла, очевидно у него пока нет левого и правого узла.
            self.left = None
            self.right = None



    # Проверка на присутсвие значения у рассматриваемого узла(не важно какого).
    def isempty(self):
        # Если у нас пусто в рассматриваемом узле, вернет True.
        return self.value == None



    # Вывод всех значений на дереве.
    def inorder(self):
        if self.isempty():
            return []
        return self.left.inorder() + [self.value] + self.right.inorder()



    # Вставка в бинарное дерево поиска
    def insert(self, data):
        # Если наш узел пуст.
        if self.isempty():
            # Просто создаем узел.
            self.value = data
            # Также определяем левый и правый узел.
            self.left = Tree()
            self.right = Tree()
            # Вывод на экран успешное добавления значения.
            print(f'{self.value} is inserted successfully')

        # Если у нас рассматриваемый узел не пуст. То выбираем по какому
        # из под узлов, пойти дальше. Важно понимать что дерево работает рекурсивно!
        elif data < self.value:
            self.left.insert(data)
        elif data > self.value:
            self.right.insert(data)
        else:
            # Если Добавляемый узел уже существует, то очевидно нужно завершать работу программы,
            # так как такой узел уже есть.
            return


    # Поиск в бинарном дереве поиска.
    def find(self, data):
        # Если мы достигли конечного узла, то нет узлов, среди которых
        # мы искали бы, тот что мы ищем в дереве.
        if self.isempty():
            # Если условие выполнено выводим, что не нашли такой узел и завершаем программу.
            print(f'{data} is not found.')
            return False

        # Если был найден нужный узел, выводим что он найден и завершаем программу
        if self.value == data:
            print(f'{data} is found.')
            return True

        # Рекурсивно бегаем по нашему дереву, то на левый узел, то на правый,
        # в зависимости от значений на рассматриваемых узлах.
        elif self.value > data:
            self.left.find(data)
        else:
            self.right.find(data)

    # Вывод максимального значения на дереве.
    def maxval(self):
        # Если self.right нет узла, то это не значит что нет объекта, он есть,
        # поэтому для проверки нужно копать по глубже.
        if self.right.right == None:
            return self.value
        return self.right.maxval()


    # Проверка, является ли узел конечным, тоесть без дочерних узлов.
    def isleaf(self):
        if self.right.value == None and self.left.value == None:
            return True
        return False


    # Удаление в бинарном дереве поиска в Python.
    def delete(self, val):
        if self.value == val:
            # Если удаляемый объект оказался на конечном узле.
            if self.isleaf():
                self.value = None
                self.right = None
                self.left = None
            # Если удаляемый объект оказался где то по середине.



t = Tree(20)
t.insert(15)
t.insert(25)
t.insert(8)
t.insert(16)
t.insert(21)
t.insert(27)