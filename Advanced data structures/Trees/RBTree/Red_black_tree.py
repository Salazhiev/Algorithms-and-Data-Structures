


# Класс узла Красно - Черного Дерева.
class RBNode:
    def __init__(self, value, color='red'):
        self.value = value
        # Цвет рассматриваемого узла.
        self.color = color
        self.left = None
        self.right = None
        # Родительский узел рассматриваемого узла.
        self.parent = None


    # Функция для получения прародителя узла.
    def get_grandparent(self):
        if self.parent is None:
            return None
        return self.parent.parent


    # Функця для получения брат(тоесть брат по одному родителю - отцу).
    def get_sibling(self):
        if self.parent is None:
            return None

        # Если будет стуация, что у меня нет брата, то функция вернет None значением.
        if self == self.parent.left:
            return self.parent.right
        return self.parent.left


    # Функция для полученя дяди, тоесть брата моего отца.
    def get_uncle(self):
        if self.parent is None:
            return None
        return self.parent.get_sibling()




# Класс самого дерева, с красно-черными узлами.
class RedblackTree:
    def __init__(self):
        self.root = None



    # Реализация вставки в дерево. Состоит из двух частей, стандартная вставка, как и в
    # обычное BST-дерево, а после уже происходит исправление свойства Red-Black, после вставки
    # мы могли нарушить одно из двух свойств:
    #       1 - Ни один красный узел, не может иметь красного потомка.
    #       2 - Все пути от узла до дочерних листьев должны содержать одинаковое количество черн. Узлов.


    # insert_fix - функция для исправления свойств красно-черного дерева после вставки.
    def __insert_fix(self, new_node):
        # Насколько я понял, добавляемый узел всегда красный.

        # Пока у new_node есть два непрерывных красных узла, нам нужно исправлять дерево RB.
        while new_node.parent and new_node.parent.color == 'red':

            # Если родитель является левым сыном дедушки.
            if new_node.parent == new_node.get_grandparent().left:

                # Получаем дядю элемента new_node.
                uncle = new_node.get_uncle()

                # Если дядя красный.
                if uncle and uncle.color == 'red':
                    new_node.parent.color = 'black'
                    uncle.color = 'black'
                    new_node.get_grandparent().color = 'red'
                    new_node = new_node.get_grandparent()
                # Если дядя черный.
                else:
                    if new_node == new_node.parent.right:
                        new_node = new_node.parent
                        self.__rotate_left(new_node)
                    new_node.parent.color = 'black'
                    new_node.get_grandparent().color = 'red'
                    self.__rotate_right(new_node.get_grandparent())


            # Если родитель является правым сыном дедушки.
            else:
                # Получаем дядю элемента new_node.
                uncle = new_node.get_uncle()

                # Если дядя красный.
                if uncle and uncle.color == 'red':
                    new_node.parent.color = 'black'
                    uncle.color = 'black'
                    new_node.get_grandparent().color = 'red'
                    new_node = new_node.get_grandparent()
                # Если дядя черный.
                else:
                    if new_node == new_node.parent.left:
                        new_node = new_node.parent
                        self.__rotate_right(new_node)
                    new_node.parent.color = 'black'
                    new_node.get_grandparent().color = 'red'
                    self.__rotate_left(new_node.get_grandparent())
        self.root.color = 'black'


    # Обычная функция вставки, которая есть в Binary_Search_Tree.
    def insert(self, value):
        # Создаем узел с новым значением.
        new_node = RBNode(value)
        if self.root is None:
            self.root = new_node
        else:
            curr_node = self.root
            while True:
                if value < curr_node.value:
                    if curr_node.left is None:
                        curr_node.left = new_node
                        new_node.parent = curr_node
                        break
                    else:
                        curr_node = curr_node.left
                else:
                    if curr_node.right is None:
                        curr_node.right = new_node
                        new_node.parent = curr_node
                        break
                    else:
                        curr_node = curr_node.right

        # После обычной вставки делаем балансровку дерева.
        self.__insert_fix(new_node)




    # После вставки, нам нужно сбалансировать наше дерево, вот две приватные функции для этого.


    # Левое вращение для Красно-Черного дерева.
    def __rotate_left(self, node):
        right_child = node.right
        node.right = right_child.left

        if right_child.left is not None:
            right_child.left.parent = node

        right_child.parent = node.parent

        if node.parent is None:
            self.root = right_child
        elif node == node.parent.left:
            node.parent.left = right_child
        else:
            node.parent.right = right_child

        right_child.left = node
        node.parent = right_child


    # Правое вращение для Красно-Черного дерева.
    def __rotate_right(self, node):
        left_child = node.left
        node.left = left_child.right

        if left_child.right is not None:
            left_child.right.parent = node

        left_child.parent = node.parent

        if node.parent is None:
            self.root = left_child
        elif node == node.parent.right:
            node.parent.right = left_child
        else:
            node.parent.left = left_child

        left_child.right = node
        node.parent = left_child


    def search(self, value):
        curr_node = self.root
        while curr_node is not None:
            if value == curr_node.value:
                return curr_node
            elif value < curr_node.value:
                curr_node = curr_node.left
            else:
                curr_node = curr_node.right
        return None
    def delete(self, value):
        node_to_remove = self.search(value)

        if node_to_remove is None:
            return

        if node_to_remove.left is None or node_to_remove.right is None:
            self._replace_node(node_to_remove, node_to_remove.left or node_to_remove.right)
        else:
            successor = self._find_min(node_to_remove.right)
            node_to_remove.value = successor.value
            self._replace_node(successor, successor.right)

        self.delete_fix(node_to_remove)

    def delete_fix(self, x):
        while x != self.root and x.color == 'black':
            if x == x.parent.left:
                sibling = x.sibling()
                if sibling.color == 'red':
                    sibling.color = 'black'
                    x.parent.color = 'red'
                    self.__rotate_left(x.parent)
                    sibling = x.sibling()
                if (sibling.left is None or sibling.left.color == 'black') and (sibling.right is None or sibling.right.color == 'black'):
                    sibling.color = 'red'
                    x = x.parent
                else:
                    if sibling.right is None or sibling.right.color == 'black':
                        sibling.left.color = 'black'
                        sibling.color = 'red'
                        self.__rotate_right(sibling)
                        sibling = x.sibling()
                    sibling.color = x.parent.color
                    x.parent.color = 'black'
                    if sibling.right:
                        sibling.right.color = 'black'
                    self.__rotate_left(x.parent)
                    x = self.root
            else:
                sibling = x.sibling()
                if sibling.color == 'red':
                    sibling.color = 'black'
                    x.parent.color = 'red'
                    self.__rotate_right(x.parent)
                    sibling = x.sibling()
                if (sibling.left is None or sibling.left.color == 'black') and (sibling.right is None or sibling.right.color == 'black'):
                    sibling.color = 'red'
                    x = x.parent
                else:
                    if sibling.left is None or sibling.left.color == 'black':
                        sibling.right.color = 'black'
                        sibling.color = 'red'
                        self.__rotate_left(sibling)
                        sibling = x.sibling()
                    sibling.color = x.parent.color
                    x.parent.color = 'black'
                    if sibling.left:
                        sibling.left.color = 'black'
                    self.__rotate_right(x.parent)
                    x = self.root
        x.color = 'black'






# RBTree = RedblackTree()
# RBTree.insert(43)
# RBTree.insert(2)
# RBTree.insert(3)
# RBTree.insert(4)
# RBTree.insert(5)
# RBTree.insert(15)
# RBTree.insert(76)
# RBTree.insert(3)
# RBTree.insert(8)