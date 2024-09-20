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


    def search(self, value):
        current = self.root
        while current is not None:
            if current.value == value:
                return current
            elif current.value < value:
                current = current.right
            else:
                current = current.left
        return None

    # Функция для поиска минимального узла.
    def find_min(self, node):
        if node is None:
            print('Дерево поиска минимального пусто')
            return None

        while node.left is not None:
            node = node.left
        return node



    # Проверяем, если удаляемый узел черный
    def __kch0(self, node):
        pass



    def deleted(self, value):
        # С начала найдем узел, который необходимо удалить.
        remove_node = self.search(value)
        if remove_node is None:
            print('такого узла в дереве нет')
            return

        if remove_node.parent is None:
            self.root = None
            return

        # Рассмотрим ситуация, что удаляемый элемент красный.
        if remove_node.color == 'red':


            # Рассмотрим ситуация, что у удаляемого элемента нет детей(К0)
            if remove_node.left is None and remove_node.right is None:
                # Удаляемый узел левый сын своего отца.
                if remove_node == remove_node.parent.left:
                    remove_node.parent.left = None
                else:
                    remove_node.parent.right = None
                return

            # Рассмотрим ситуацию, что у удаляемого элемента есть оба сына(К2)
            elif remove_node.left and remove_node.right:
                new_node = self.find_min(remove_node.right)
                remove_node.value = new_node.value
                self.deleted(new_node)
                return

            # Рассмотрим случай, когда у удаляемого элемент есть ровно один сын(К1)
            # дело в том, что это невозможно


        # Удаляемый элемент черный
        if remove_node.color == 'black':

            # Случай когда у удаляемого элемента нет детей(Ч0)
            if remove_node.left is None and remove_node.right is None:

                # Мне нужна сторона для рассмотрения этого случая.
                if remove_node == remove_node.parent.right:

                    # Рассмотрим случай - Родитель красный, Левый ребенок черный с черными внуками(КЧ1)
                    y = remove_node.parent.left
                    if y.left != 'red' and y.right != 'red' and y.parent.color == 'red' and y.color=='red':
                        remove_node.parent.color = 'black'
                        y.color = 'red'
                        remove_node.parent.right = None
                        return

                    # Рассмотрим случай - Родитель красный, левый ребенок черный с левым красным внуком(ЧК2).
                    elif remove_node.parent.color == 'red' and y.color=='black' and y.left.color=='red':
                        c = y.right
                        g = y.parent
                        grand_g = g.parent

                        g.left = c
                        y.right = g
                        g.parent = y

                        if grand_g:
                            if g == grand_g.left:
                                grand_g.left = y
                            elif g == grand_g.right:
                                grand_g.right = y
                            y.parent = grand_g
                        else:
                            y.parent = None
                            self.root = y

                        y.left.color = 'black'

                        # ТУТ УДАЛИТЬ ЗАБЫЛ!!!!!!!!!

                    # Родитель черный, левый сын красный, у правого внука черные правнуки(ЧК3).
                    elif remove_node.parent.color == 'black' and y.color == 'red' and y.right.left != 'red' and y.right.right != 'red':
                        pass



            # Случай, когда у удаляемого элемента есть оба сына(Ч2)
            elif remove_node.left and remove_node.right:
                new_node = self.find_min(remove_node.right)
                remove_node.value = new_node.value
                self.deleted(new_node)
                return

            # Случай, когда у удаляемого элемента, есть ровно один сын(Ч1)
            else:
                if remove_node.left:
                    remove_node.value = remove_node.left.value
                    remove_node.left = None
                    return
                else:
                    remove_node.value = remove_node.right.value
                    remove_node.right = None
                    return



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



