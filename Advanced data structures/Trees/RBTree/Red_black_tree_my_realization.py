import Red_black_tree
import random

class RBNode:
    def __init__(self, value, color='red'):
        self.value = value
        self.color = color
        self.left = None
        self.right = None
        self.parent = None


    # Возвращает дедушку.
    def get_grandparent(self):
        if self.parent is None:
            return None
        return self.parent.parent


    # Возвращает брата.
    def get_sibling(self):
        if self.parent is None:
            return None

        if self.parent.left == self:
            return self.parent.right
        return self.parent.left


    # Возращает дядю, тоесть брата моего отца.
    def get_uncle(self):
        if self.parent is None:
            return None
        return self.parent.get_sibling()



class RedblackTree:
    # Конструктор класса.
    def __init__(self):
        self.root = None

    def __insert_fix(self, new_node):

        # До тех пор, пока есть два подряд идущих красных.
        while new_node and new_node.parent and new_node.parent.color == 'red':

            # Если родитель является левым сыном дедушки.
            if new_node.parent == new_node.get_grandparent().left:
                # Если код зайдет сюда, значит у нового элемента по любому есть дедушка.

                # Взяли брата отца.
                uncle = new_node.get_uncle()

                # Если брат отца красный(повторение случая 1 с конспекта).
                if uncle and uncle.color == 'red':
                    new_node.parent.color = 'black'
                    uncle.color = 'black'
                    new_node.get_grandparent().color = 'red'
                    # Идем вверх проверяя есть ли сверху какие-то конфликты.
                    new_node = new_node.get_grandparent()
                else:
                    # Если код зашел сюда, значит брат отца черный.


                    if new_node == new_node.parent.right:
                        self.__left_first_rotation(new_node)
                        new_node = self.__left_two_rotation(new_node)

                        if not new_node.parent:
                            self.root = new_node

                    else:
                        new_node = new_node.parent
                        new_node = self.__left_two_rotation(new_node)

                        if not new_node.parent:
                            self.root = new_node
                    break


            elif new_node.parent == new_node.get_grandparent().right:

                uncle = new_node.get_uncle()

                if uncle and uncle.color == 'red':
                    new_node.parent.color = 'black'
                    uncle.color = 'black'
                    new_node.get_grandparent().color = 'red'
                    new_node = new_node.get_grandparent()
                else:

                    if new_node == new_node.parent.left:
                        self.__right_first_rotation(new_node)
                        new_node = self.__right_two_rotation(new_node)

                        if not new_node.parent:
                            self.root = new_node
                    else:
                        new_node = new_node.parent
                        new_node = self.__right_two_rotation(new_node)

                        if not new_node.parent:
                            self.root = new_node
                    break




        self.root.color = 'black'


    # 2.1
    def __right_two_rotation(self, y):
        grand_g = y.parent.parent
        g = y.parent


        c = y.left
        g.right = c

        if c:
            c.parent = g

        y.left = g
        g.parent = y

        if grand_g:
            if grand_g.right == g:
                grand_g.right = y
            elif grand_g.left == g:
                grand_g.left = y
            y.parent = grand_g
        else:
            y.parent = None

        y.color = 'black'
        g.color = 'red'

        return y


    # 2.2
    def __right_first_rotation(self, x):
        b = x.right
        y = x.parent
        g = y.parent
        g.right = x
        x.parent = g

        y.left = b

        if b:
            b.parent = y


        x.right = y
        y.parent = x


    # 2.2
    def __left_first_rotation(self, x):
        b = x.left
        y = x.parent
        g = y.parent
        g.left = x
        x.parent = g

        y.right = b

        if b:
            b.parent = y

        x.left = y
        y.parent = x


    # 2.1
    def __left_two_rotation(self, y):
        # Принимает отца нового добавляемого узла.
        grand_g = y.parent.parent
        g = y.parent


        c = y.right
        g.left = c

        if c:
            c.parent = g

        y.right = g
        g.parent = y

        if grand_g:
            if grand_g.left == g:
                grand_g.left = y
            elif grand_g.right == g:
                grand_g.right = y
            y.parent = grand_g
        else:
            y.parent = None

        y.color = 'black'
        g.color = 'red'

        return y



    def insert(self, value):
        new_node = RBNode(value)

        # Если дерево пусто, то корневой узел, равен этому новому узлу.
        if self.root is None:
            self.root = new_node
        else:
            current = self.root
            while True:
                if value < current.value:
                    if current.left is None:
                        current.left = new_node
                        new_node.parent = current
                        break
                    else:
                        current = current.left
                else:
                    if current.right is None:
                        current.right = new_node
                        new_node.parent = current
                        break
                    else:
                        current = current.right

        self.__insert_fix(new_node)


    def __eq__(self, other):
        if other is None:
            return False
        return self._compare_trees(self.root, other.root)
    def _compare_trees(self, node1, node2):
        # Если оба узла None, то они равны
        if node1 is None and node2 is None:
            return True

        # Если только один из узлов None, то деревья не равны
        if node1 is None or node2 is None:
            return False

        if (node1.parent is None and node2.parent is not None) or \
                (node1.parent is not None and node2.parent is None):
            return False

        # Сравниваем ключи и цвета узлов
        if node1.value != node2.value or node1.color != node2.color:
            return False

        # Рекурсивно сравниваем левое и правое поддеревья
        return self._compare_trees(node1.left, node2.left) and \
            self._compare_trees(node1.right, node2.right)


    def search(self, root, value):
        current = root
        while current is not None:
            if current.value == value:
                return current
            elif current.value < value:
                current = current.right
            else:
                current = current.left
        return None


    # Функция для поиска максимального узла.
    def find_max(self, node):
        if node is None:
            print('Дерево поиска минимального пусто')
            return None

        while node.right is not None:
            node = node.right
        return node

    def deleted(self, value):
        remove_node = self.search(self.root, value)
        if remove_node is None:
            print('Нет такого узла')
            return
        if remove_node == self.root and remove_node.left is None and remove_node.right is None:
            self.root = None
            return

        if remove_node.left and remove_node.right:
            new_remove_node = self.find_max(remove_node.left)
            remove_node.value = new_remove_node.value
            remove_node = new_remove_node

        # 1) РАБОТАЕТ!!!
        if remove_node.color == 'red' and not remove_node.left and not remove_node.right:
            if remove_node.parent:
                if remove_node == remove_node.parent.left:
                    remove_node.parent.left = None
                else:
                    remove_node.parent.right = None
            return



        # 3)
        elif remove_node.color == 'black' and remove_node.left and remove_node.left.color == 'red' and remove_node.right == None:
            remove_node.value = remove_node.left.value
            remove_node.left = None
            return
        elif remove_node.color == 'black' and remove_node.right and remove_node.right.color == 'red' and remove_node.left == None:
            remove_node.value = remove_node.right.value
            remove_node.right = None
            return

        # 2)
        if remove_node.parent:
            if remove_node.parent.right == remove_node:
                self.__balanced_for_deleted_right(remove_node, True)
            else:
                self.__balanced_for_deleted_left(remove_node, True)


    def __balanced_for_deleted_right(self, remove_node, flag):
        a = remove_node.parent
        b = a.left
        c = b.right
        r = b.left
        # 2.1.1
        if a and a.color=='red' and b and c and c.color == 'red': # РАБОТАЕТ!!!
            if a:
                g = a.parent

            B = c.left
            C = c.right

            c.left = b
            b.parent = c

            if g:
                if a == g.left:
                    g.left = c
                else:
                    g.right = c
                c.parent = g
            else:
                c.color = 'black'
                self.root = c
                c.parent = None

            c.right = a
            a.parent = c
            if flag:
                a.right = None
            a.left = C
            if C:
                C.parent = a

            b.right = B
            if B:
                B.parent = b

            a.color='black'

            return

        # 2.1.1
        elif a and a.color=='red' and b and r and r.color == 'red': # РАБОТАЕТ !!!
            if a:
                g = a.parent

            b.right = a
            a.parent = b

            a.left = c
            if c:
                c.parent = a

            if flag:
                a.right = None

            if g:
                if a == g.left:
                    g.left = b
                else:
                    g.right = b
                b.parent = g
            else:
                b.color = 'black'
                self.root = b
                b.parent = None

            return

        # 2.1.2
        elif a and a.color == 'red' and b:
            b.color = 'red'
            a.color = 'black'
            if flag:
                a.right = None
            return

        # 2.2.1
        elif a and a.color == 'black' and b and b.color=='red':

            g = a.parent

            # 2.2.1.1
            if c and c.color == 'black':
                d_1 = c.left
                d_2 = c.right
                if d_1 and d_1.color=='red':
                    c.left = b
                    b.parent = c

                    c.right = a
                    a.parent = c
                    a.left = d_2
                    if flag:
                        a.right = None
                    if d_2:
                        d_2.parent = a

                    if g:
                        if a == g.left:
                            g.left = d_1
                        else:
                            g.right = d_1
                        d_1.parent = g
                    else:
                        self.root = d_1
                        d_1.parent = None



                    b.right = d_1
                    d_1.parent = b
                    d_1.color = 'black'
                elif d_2 and d_2.color=='red':
                    d_2.left = b
                    b.parent = d_2

                    d_2.right = a
                    a.parent = d_2

                    C = d_2.left
                    e = d_2.right

                    if g:
                        if a == g.left:
                            g.left = d_2
                        else:
                            g.right = d_2
                        d_2.parent = g
                    else:
                        self.root = d_2

                        d_2.parent = None


                    a.left = e
                    if e:
                        e.parent = a

                    if flag:
                        a.right = None

                    c.right = C
                    if C:
                        C.parent = c
                    d_2.color = 'black'


                # 2.2.1.2
                else: # ВЕРНО!!!!!!!
                    b.right = a
                    a.parent = b
                    a.left = c
                    if c:
                        c.parent = a

                    if flag:
                        a.right = None


                    c.color='red'
                    b.color='black'

                    if g:
                        if a==g.left:
                            g.left = b
                        else:
                            g.right = b

                        b.parent = g
                    else:
                        self.root = b
                        b.parent = None
                return

        elif a and a.color=='black' and b and b.color=='black':

            b_1 = b.left
            b_2 = b.right
            g = a.parent

            # 2.2.2.1
            if b_2 and b_2.color=='red':
                b_2_1 = b_2.left
                b_2_2 = b_2.right

                b_2.left = b
                b.parent = b_2

                b_2.right = a
                a.parent = b_2
                a.left = b_2_2
                if b_2_2:
                    b_2_2.parent = a

                b.right = b_2_1
                if b_2_1:
                    b_2_1.parent = b

                if g:
                    if a==g.left:
                        g.left = b_2
                    else:
                        g.right = b_2
                    b_2.parent = g
                else:
                    self.root = b_2
                    b_2.parent = None

                if flag:
                    a.right = None
                b_2.color = 'black'

            elif b_1 and b_1.color=='red':

                b.right = a
                a.parent = b

                a.left = b_2
                if b_2:
                    b_2.parent = a


                if g:
                    if a == g.left:
                        g.left = b
                    else:
                        g.right = b
                    b.parent = g
                else:
                    self.root = b
                    b.parent = None

                if flag:
                    a.right = None

                b_1.color = 'black'


            # 2.2.2.2
            else:
                b.color = 'red'
                a.right = None
                if a.parent:
                    if a == a.parent.right:
                        self.__balanced_for_deleted_right(a, False)
                    else:
                        self.__balanced_for_deleted_left(a, False)
                else:
                    a.left.color = 'red'
                    a.right = None

            return

    def __balanced_for_deleted_left(self, remove_node, flag):
        a = remove_node.parent
        b = a.right
        c = b.left
        r = b.right
        # 2.1.1
        if a and a.color=='red' and b and c and c.color == 'red':
            if a:
                g = a.parent

            B = c.right
            C = c.left

            c.right = b
            b.parent = c

            if g:
                if a == g.right:
                    g.right = c
                else:
                    g.left = c
                c.parent = g
            else:
                c.color = 'black'
                self.root = c

            c.left = a
            a.parent = c
            if flag:
                a.left = None
            a.right = C
            if C:
                C.parent = a

            b.left = B
            if B:
                B.parent = b

            return

        # 2.1.1
        elif a and a.color=='red' and b and r and r.color == 'red': # РАБОТАЕТ!!!
            if a:
                g = a.parent

            b.left = a
            a.parent = b

            a.right = c
            if c:
                c.parent = a

            if flag:
                a.left = None

            if g:
                if a == g.right:
                    g.right = b
                else:
                    g.left = b
                b.parent = g
            else:
                b.color = 'black'
                self.root = b

            return

        # 2.1.2
        elif a and a.color == 'red' and b:
            b.color = 'red'
            a.color = 'black'
            if flag:
                a.left = None
            return

        # 2.2.1
        elif a and a.color == 'black' and b and b.color=='red':

            g = a.parent

            # 2.2.1.1
            if c and c.color == 'black':
                d_1 = c.right
                d_2 = c.left
                if d_1 and d_1.color=='red':
                    c.right = b
                    b.parent = c

                    c.left = a
                    a.parent = c
                    a.right = d_2
                    if flag:
                        a.left = None
                    if d_2:
                        d_2.parent = a

                    if g:
                        if a == g.right:
                            g.right = d_1
                        else:
                            g.left = d_1
                        d_1.parent = g
                    else:
                        self.root = d_1



                    b.left = d_1
                    d_1.parent = b
                    d_1.color = 'black'


                elif d_2 and d_2.color=='red':
                    d_2.right = b
                    b.parent = d_2

                    d_2.left = a
                    a.parent = d_2

                    C = d_2.right
                    e = d_2.left

                    if g:
                        if a == g.right:
                            g.right = d_2
                        else:
                            g.left = d_2
                        d_2.parent = g
                    else:
                        self.root = d_2


                    a.right = e
                    if e:
                        e.parent = a

                    if flag:
                        a.left = None

                    c.left = C
                    if C:
                        C.parent = c
                    d_2.color = 'black'


                # 2.2.1.2
                else:
                    b.left = a
                    a.parent = b
                    a.right = c
                    if c:
                        c.parent = a

                    if flag:
                        a.left = None


                    c.color='red'
                    b.color='black'

                    if g:
                        if a==g.right:
                            g.right = b
                        else:
                            g.left = b

                        b.parent = g
                    else:
                        self.root = b
                return

        elif a and a.color=='black' and b and b.color=='black':

            b_1 = b.left
            b_2 = b.right
            g = a.parent

            # 2.2.2.1
            if b_2 and b_2.color=='red': # РАБОТАЕТ!!!
                b.left = a
                a.parent = b

                if flag:
                    a.left = None

                a.right = b_1
                if b_1:
                    b_1.parent = a

                if g:
                    if a==g.left:
                        g.left = b
                    else:
                        g.right = b
                    b.parent = g
                else:
                    self.root = b
                    b.parent = None

                b_2.color = 'black'

                return




            elif b_1 and b_1.color=='red':
                b_1_1 = b_1.left
                b_1_2 = b_1.right

                b_1.left = a
                a.parent = b_1
                a.right = b_1_1
                if b_1_1:
                    b_1_1.parent = a

                b_1.right = b
                b.parent = b_1
                b.left = b_1_2
                if b_1_2:
                    b_1_2.parent = b

                b_1.color = 'black'

                if g:
                    if a == g.right:
                        g.right = b_1
                    else:
                        g.left = b_1
                    b_1.parent = b_1
                else:
                    self.root = b_1
                    b_1.parent = None
                a.left = None

                return

            # 2.2.2.2
            else:
                b.color = 'red'
                a.left = None
                if a.parent:
                    if a == a.parent.right:
                        self.__balanced_for_deleted_right(a, False)
                    else:
                        self.__balanced_for_deleted_left(a, False)
                else:
                    a.right.color = 'red'
                    a.left = None
            return




tree_my = RedblackTree()
tree_true = Red_black_tree.RedBlackTree()

a = [20,10,25,4,16,23,20,2,5,14,17,3,12,15,19,11]


for i in a:
    tree_my.insert(i)

tree_my.deleted(3)
tree_my.deleted(2)

print()