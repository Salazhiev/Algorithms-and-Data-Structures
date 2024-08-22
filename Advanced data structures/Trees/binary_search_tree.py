# Бинарное дерево поиска - дерево у которого максимум два потомка, где левый узел с потомства имеет
# значение меньшее чем значение у родителя, соответственно правое значение потомства имеет большее значение чем
# у родителя.


# Класс описыващий отдельный узел дерева.
class Node:
    def __init__(self, data):
        # Значение дерева.
        self.data = data

        # Левый и Правый узел, рассматриваемого узла.
        self.left = None
        self.right = None

# Класс описывающий все дерево целиком.
class Tree:
    # Количество значений в нашем дереве.
    lens = 0

    # Инициализация класса.
    def __init__(self):
        self.root = None



    # Внутренний метод класса.
    # Возращает (узел, к которому должен быть прикреплен новый узел, со значением value ...
    # его родителя ... True - если такой узел уже есть).
    def __find(self, node, parent, value) -> (Node, Node, bool):
        # Если у нас отсутствует узел, с которым мы сравниваем значения value.
        if node is None:
            # По идеи такое исключение должно произойти в самом начале вызова функции, по идеи так.
            return None, parent, False

        # Если в процессе наткнулись на такой же узел, завершаем
        # работу функции возвращая True. Тоесть нам нет смысла искать дальше.
        if value==node.data:
            # Именно поэтому и возвращаем True.
            return node, parent, True


        # Если существует какой-то узел и он не сходится с рассматриваемым узлов,
        # то мы ищем следующий узел.
        if value < node.data:
            # Если рассматриваемый узел не имеет левого подузла, то очевидно туда должен добавиться, наш новый узел.
            # Мы его и возвращаем, если данное условие не выполниться, то программа пойдет к нижнему return и вернет узел, с
            # пустым подузлов, и этот пустой подузел в процессе будет равен нашему новому узлу, со значением value.
            if node.left:
                # А если же у рассматриваемого узла есть левый подузел, то очевидно нам нужно спуститься туда.
                # Следовательно рекурсивно вызываем нашу функцию.
                return self.__find(node.left, node, value)

        # Тут происходит все абсолютно аналогично.
        if value > node.data:
            if node.right:
                return self.__find(node.right, node, value)

        # Возвращаем всегда узел, к которому будет прикреплен новый узел - node.
        return node, parent, False




    # Функция для добавления нового узла в наше дерево.
    # На вход принимает объект класса Node, тоесть полноценный узел.
    def append(self, obj: Node) -> Node:
        # Если наше дерево пусто, то очевидно просто завершаем программу.
        if self.root is None:
            self.root = obj
            return obj


        # Возвращает узел к которому должен быть прикреплен obj. Тоесть
        # фунция отработала таким образом, чтобы в итоге у нас node стал родительским для obj.
        s, p, fl_find = self.__find(self.root, None, obj.data)

        # Успешное добавление узла, это факт того, что такого узла в нашем деревет нет и
        # факт того, что существует узел, к которому мы бы прикрепили наш узел.
        if fl_find == False and s:
            if obj.data < s.data:
                s.left = obj
            else:
                s.right = obj
            # В любом случае будет прикрплен один узел, поэтому увеличиваем количество узлов.
            self.lens += 1
        elif fl_find == True:
            print('Такое узел уже существует.')
        else:
            print('Нет узла, к которому мы смогли бы прикрепить этот.')

        # Возращает узел, который прикрепляли собсна.
        return obj



    # Отображение элементов с обходом дерева в глубину.
    def show_tree(self, node):
        if node is None:
            return

        # Очевидно как отработает данная рекурсия, будем идти с левой глубины к правой.
        self.show_tree(node.left)
        print(node.data)
        self.show_tree(node.right)




    # Отображение элементов с обходом дерева в ширину.
    # Тоесть обход будет происходить по уровням, с начала выводятся все значения с узлов ниже корневого
    # и так последовательно: все значения с первого этажа, со второго и т.д.
    def show_wide_tree(self, node):
        if node is None:
            return

        # Создаем массив со всем узлами на i-ом этаже.
        v = [node]
        # Следовательно, цикл работает до тех пор, пока массив с узлами на i-ом этаже не пуст.
        while v:
            # Внутри цикла создается массив со всем узлами на i+1 - ом этаже.
            vn = []
            # Перебираем все узла с нашего массива узлов.
            for x in v:
                # Выводим на экран все значения узлов с одного этажа.
                print(x.data, end=' ')

                # Добавляем под узлы, рассматриваемых узлов.
                if x.left:
                    vn += [x.left]
                if x.right:
                    vn += [x.right]
            # Просто перенос строки в общем та.
            print()
            # Меняем массивы с узлами.
            v = vn



    # Внутри классовые вспомогательные функции.

    # Функция для удаления подузла s, с узла p.
    def __del_leaf(self, s, p):
        if p.left == s:
            p.left = None
        elif p.right == s:
            p.right = None
    # Функция для удаления подузлы s, с узла p, у которого нет брата.
    def __del_one_child(self, s, p):
        # Если у подузла s нет брата правого.
        if p.left == s:
            # То просто заменяем значение подузла s, на свободное левое подузло либа же правое подузло узла s
            if s.left is None:
                p.left = s.right
            elif s.right is None:
                p.left = s.left
        # Если у подузла s нет брата левого.
        elif p.right == s:
            # То просто заменяем значение подузла s, на свободное левое или правое подузло узла s
            if s.left is None:
                p.right = s.right
            elif s.right is None:
                p.right = s.left
    # Функция для поиска минимального узла, относительно дерева образующегося
    # с корневым элементом удаления(тоесть корневой элементов = тот что должен быть удален).
    def __find_min(self, node, parent):
        if node.left:
            return self.__find_min(node.left, node)
        # Функция возращает, последний элемент, тоесть минимальный и его родителя.
        return node, parent


    # Функция для удаления узла с дерева.
    def del_node(self, key):
        # s - узел, который нужно удалить
        # p - родитель узла, который нужно удалить.
        # Если fl_find = False, значит нет такого узла в нешем дереве, значит не чего удалять.
        s, p, fl_find = self.__find(self.root, None, key)

        # Если на дереве нет узла с таким значением.
        if fl_find==False:
            # Просто завершаем.
            return None

        # Если все же есть узел который нужно удалить, то проверяем является ли этот узел конечным узло
        # на дереве, тоесть есть ли у него потомки, если нет, то вызываем фукнцию __del_leaf
        if s.left is None and s.right is None:
            # Вызиваем функцию для удаления собсна.
            self.__del_leaf(s, p)
        # Если удаляемый узел, имеет только одного наследника.
        elif s.left is None or s.right is None:
            # То вызиваем функцию для
            self.__del_one_child(s, p)
        # Если удаляемый элемент находится посередине где-то, нашего дерева.
        else:
            # sr - узел с минимальным значением на нем.
            # pr - родитель узал sr.
            sr, pr = self.__find_min(s.right, s)
            # Удаляем удаляемый элемент, тоесть заменяем его на найденный минимальный.
            s.data = sr.data
            # Вызиваем функцию для удаления элемента, который был поставлен на место удаленного.
            self.__del_one_child(sr, pr)