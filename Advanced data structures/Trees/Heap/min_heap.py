# Куча - это дерево, но его реализовывать можно через массив:
# Дело в том, что мое дерево строится по правилу полноты, поэтому обращаться к любому элементу я могу разделением или умножение индекса на 2.
class MinHeap:

    def __init__(self, n=10):
        # Создаем массива определенной длины.
        self.a = [0]*n
        # Будем регулировать массив с помощью кол-ва элементов в нем(нумерация с 1).
        self.n = 0
        # Также длина массива.
        self.lens = len(self.a)


    # Получаю минимальный корневой элемент(минимальный элемент дерева).
    def getMin(self):
        if self.n > 0:
            return self.a[0]

        # Количество узлов в дереве 0, возвращаем None значение.
        return None



    # Удаление минимального(тоесть удаление корня дерева).
    def extractMin(self):
        # Меняем самый последний листовой элемент, на первый корневой элемент дерева.
        self.a[0], self.a[self.n - 1] = self.a[self.n-1], self.a[0]

        # Меняем длину массива.
        self.n -= 1

        # Запускаем функция перестройки дерева.
        # На вход номер корневой вершины, нумерация с 1.
        self.__siftDown(0)


    # Добавляем новый элемент в дерево.
    def insert(self, x):
        # Если длины массва не достаточно, просто увеличиваем длину в два раза.
        if self.n >= self.lens:
            self.a = self.a + [0]*self.lens
            self.lens *= 2

        # Добавление в конец массива нового элемента.
        self.a[self.n] = x
        self.n += 1

        # Перестройка дерева.
        self.__siftUp(self.n-1)


    # Уменьшение значение в каком то узле.
    def decreseKey(self, pos, delta):
        self.a[pos-1] -= delta
        self.__siftUp(pos-1)



    # Перестройка дерева 1.
    # Аргумент - индекс
    def __siftUp(self, v):
        if v == 0: return
        p = v//2 - 1 * (v%2==0)
        if self.a[v] < self.a[p]:
            self.a[v], self.a[p] = self.a[p], self.a[v]
            self.__siftUp(p)





    # Перестройка дерева 2.
    def __siftDown(self, v):
        if 2*v >= self.n:
            return # У узла с номером v - нет детей.

        u = 2*v
        if v == 0:
            u += 1

        if u + 1 <= self.n and self.a[u] > self.a[u+1]:
            u = u + 1

        if self.a[u] < self.a[v]:
            self.a[u], self.a[v] = self.a[v], self.a[u]
            self.__siftDown(u)




t = MinHeap()
array = [21, 55, 21]
for i in array:
    t.insert(i)

t.extractMin()

print()


