import Red_black_tree

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

        if b:
            x.right = y
        y.parent = x

        x.right = y
        y.parent = x


    # 2.2
    def __left_first_rotation(self, x):
        b = x.left
        y = x.parent
        g = y.parent
        g.left = x
        x.parent = g

        if b:
            b.parent = y
        y.right = b

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


    def search(self, value, root):
        current = root
        while current is not None:
            if current.value == value:
                return current
            elif current.value < value:
                current = current.right
            else:
                current = current.left
        return None


    # Функция для поиска минимального узла.
    def find_max(self, node):
        if node is None:
            print('Дерево поиска минимального пусто')
            return None

        while node.right is not None:
            node = node.right
        return node



    def deleted(self, root, value):
        remove_node = self.search(value, root)
        if remove_node is None:
            print('Нет такого узла в дереве')
            return None

        # 1)
        if remove_node.color=='red' and not remove_node.left and not remove_node.right:
            if remove_node.parent:
                if remove_node == remove_node.parent.left:
                    remove_node.parent.left = None
                else:
                    remove_node.parent.right = None
            else:
                self.root = None

        # 3)
        elif ((remove_node.left.color=='red' and not remove_node.right) or (remove_node.right.color=='red' and not remove_node.left) and (remove_node.color == 'black')):
            if remove_node.left:
                remove_node.value = remove_node.left.value
                remove_node.left = None
            else:
                remove_node.value = remove_node.right.value
                remove_node.right = None


        else:

            current = self.root
            while current:
                if current.value == value:
                    break
                if current.value > value:
                    current = current.left
                else:
                    current = current.right

            # Удаляемый красный, с одним ребенок не может существовать.

            # Удаляемый красный с двумя детьми.
            if current.color == 'red' and current.left and current.right:
                new_for_del = self.find_max(root)
                current.value = new_for_del.value
                self.deleted(current.left, new_for_del.value)
                return


            elif current.color == 'black' and current.left and current.right:
                current.value = self.find_max(root.right)
                self.deleted(current.left, current.value)
                return


            if current.color == 'black' and current.left is None and current.right is None:
                g = current.parent
                grand_g = g.parent
                s = g.left
                a_1 = s.left
                b_1 = s.right

                if g.color == 'red' and s.color == 'black' and a_1.color != 'red' and b_1.color != 'red':
                    g.color = 'black'
                    s.color = 'red'
                    g.right = None
                    return

                elif g.color=='red' and s.color=='black' and a_1.color=='red':

                    s.right = g
                    g.parent = s
                    g.left = b_1
                    b_1.parent = g
                    a_1.color = 'black'
                    g.right = None

                    if grand_g:
                        if g == grand_g.left:
                            grand_g.left = s
                        else:
                            grand_g.right = s
                        s.parent = grand_g
                    else:
                        s.color = 'black'
                        self.root = s
                    return

                # ЧК3 — родитель чёрный, левый сын красный, у правого внука чёрные правнуки
                elif g.color == 'black' and s.color == 'red' and b_1.left.color != 'red' and b_1.right.color != 'red':
                    s.right = g
                    g.parent = s
                    g.left = b_1
                    b_1.parent = g
                    b_1.color = 'red'
                    s.color = 'black'
                    g.right = None

                    if grand_g:
                        if g == grand_g.left:
                            grand_g.left = s
                        else:
                            grand_g.right = s
                        s.parent = grand_g
                    else:
                        self.root = s


                    return

                # ЧК4 — родитель чёрны й, левый сын красный, у правого внука левый правнук красный
                elif g.color == 'black' and s.color == 'red' and b_1.left.color == 'red':
                    c = b_1.right
                    b = b_1.left

                    a = g.value
                    g.value = b_1.value
                    current.value = a

                    current.left = c
                    c.parent = current
                    s.right = b
                    b.parent = s
                    b.color = 'black'

                    return

                # ЧЧ5 — родитель чёрный, левый сын чёрный с правым красным внуком.
                elif g.color=='black' and s.color == 'black' and b_1.color=='red':
                    b = b_1.left
                    c = b_1.right
                    s.right = b
                    b.parent = s

                    aaa = g.value
                    g.value = b_1.value
                    current.value = aaa
                    current.left = c
                    c.parent = current

                    return

                # ЧЧ6 — родитель чёрный, левый сын чёрный, его внуки тоже чёрные
                elif g.color == 'black' and s.color == 'black' and a_1.color != 'red' and b_1.color != 'red':
                    s.color = 'red'
                    g.right = None
                    # ??????????




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

        # Сравниваем ключи и цвета узлов
        if node1.value != node2.value or node1.color != node2.color:
            return False

        # Рекурсивно сравниваем левое и правое поддеревья
        return self._compare_trees(node1.left, node2.left) and \
            self._compare_trees(node1.right, node2.right)

tree = RedblackTree()
tree.insert(20)
tree.insert(10)
tree.insert(30)
tree.insert(25)
tree.insert(35)

tree.deleted(30)

print()



