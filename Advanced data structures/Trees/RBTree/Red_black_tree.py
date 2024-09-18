import Red_black_tree_my_realization


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


    def __eq__(self, other):
        if isinstance(other, RBNode):
            def dfs(tree1, tree2):


                if tree1.left and not tree2.left or tree1.right and not tree2.right:
                    return False
                elif not tree1.left and not tree2.left and not tree1.right and not tree2.right:
                    return True

                if tree1.value != tree2.value:
                    return False



                return dfs(tree1.left, tree2.left) and dfs(tree1.right, tree2.right)



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



    def __eq__(self, other):
        if isinstance(other, Red_black_tree_my_realization.RedblackTree):
            return self.root == other.root
        return NotImplemented



RBTree = RedblackTree()
RBTree.insert(20)
RBTree.insert(30)
RBTree.insert(10)
RBTree.insert(5)
RBTree.insert(1)