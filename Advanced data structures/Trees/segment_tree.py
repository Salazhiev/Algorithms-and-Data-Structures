# Дерево Отрезков
import random
from math import log2

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Segment_Tree:

    lens = 0
    # Конструктор класса, который строит необходимое дерево на основе массива.

    def __init__(self, arr):
        self.__create_tree(arr)



    # Функция построения дерева, на основе массива.
    def __create_tree(self, arr):
        self.root = Node(sum(arr))

        # Вычисление кол-ва элементов которые нужны, чтобы дополнить длину массиву до степени двойки.
        len_ = 2**( int(log2(len(arr)))+1*(int(log2(len(arr))) != log2(len(arr))) ) - len(arr)

        for _ in range(len_):
            arr.append(0)

        self.lens = len(arr)

        # Функция строит дерево таким образом, чтобы на листах были элементы массива, а на вершинах суммы.
        def create_tree(root, arr, l):
            if not len(arr[:l//2])>0:
                return

            root.left = Node(sum(arr[:l//2]))
            root.right = Node(sum(arr[l//2:]))

            create_tree(root.left, arr[:l//2], l//2)
            create_tree(root.right, arr[l//2:], l//2)

        create_tree(self.root, arr, len(arr))





    # Функци для изменения переменной.
    # Сложность выполнения O(logn)
    def update(self, pos, x):
        self.__update(self.root, 0, self.lens-1, pos, x)

    # Функция для замены одного из элементов массива.
    # root - вершина в которой мы работаем на итерации рекурсии.
    # [tl, tr] - контролируемый отрезок root вершины.
    # pos - позиция изменяемого элемента, его индекс в общем.
    # x - число на которое меняется value на pos позиции.
    def __update(self, root, tl, tr, pos, x):
        # Условие выхода из рекурсии
        if tl==tr:
            root.value += x
            return
        # В любом случае увелчиваем вершину на икс.
        root.value += x

        tm = (tl+tr)//2

        # Идем в левое подерево.
        if pos<=tm:
            self.__update(root.left, tl, tm, pos, x)
        else:
            self.__update(root.right, tm+1, tr, pos, x)






    # [l,r] - граница суммы, которую мы хотим вычислить.
    # Сложность выполнения O(logn)
    def get_Sum(self, l, r):
        return self.__get_Sum(self.root, 0, self.lens-1, l, r)

    def __get_Sum(self, root, tl, tr, l, r):
        if tl==l and tr==r:
            return root.value

        # Наша сумма.
        ans = 0
        tm = (tl+tr)//2

        # Есть ли смысли идти в левое потомство / в правое потомство.
        if l <= tm:
            ans += self.__get_Sum(root.left, tl, tm, l, min(r, tm))
        elif r > tm:
            ans += self.__get_Sum(root.right, tm+1, tr, max(l, tm+1), r)

        return ans





arr = [ random.randint(1, 100) for _ in range(8) ] # Придумываем массива.
t = Segment_Tree(arr)