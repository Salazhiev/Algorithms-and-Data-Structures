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


        return NotImplemented


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
                        self.__left_two_rotation(new_node)
                    else:
                        new_node = new_node.parent
                        self.__left_two_rotation(new_node)

            elif new_node.parent == new_node.get_grandparent().right:

                uncle = new_node.get_uncle()

                if uncle and uncle.color == 'red':
                    new_node.parent.color = 'black'
                    uncle.color = 'red'
                    new_node.get_grandparent().color = 'res'
                    new_node = new_node.get_grandparent
                else:

                    if new_node == new_node.parent.right:
                        self.__right_first_rotation(new_node)
                        self.__right_two_rotation(new_node)
                    else:
                        new_node = new_node.parent
                        self.__right_two_rotation(new_node)



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

        if not grand_g:
            if grand_g.right == g:
                grand_g.right = y
            elif grand_g.left == g:
                grand_g.left = y
            y.parent = grand_g

        y.color = 'black'
        g.color = 'red'


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

        y.color = 'black'
        g.color = 'red'



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
        if isinstance(other, Red_black_tree.RedblackTree):
            return self.root == other.root
        return NotImplemented



RBTree = RedblackTree()
RBTree_True = Red_black_tree.RedblackTree()

a = [20, 30, 10, 5, 1]
for i in a:
    RBTree.insert(i)
    RBTree_True.insert(i)

print(RBTree == RBTree_True)