class RBNode:
    def __init__(self, value, color='red'):
        self.value = value
        self.color = color
        self.left = None
        self.right = None
        self.parent = None


    # Возвращает дедушку.
    def __get_grandparent(self):
        if self.parent is None:
            return None
        return self.parent.parent


    # Возвращает брата.
    def __get_sibling(self):
        if self.parent is None:
            return None

        if self.parent.left == self:
            return self.parent.right
        return self.parent.left


    # Возращает дядю, тоесть брата моего отца.
    def get_uncle(self):
        if self.parent is None:
            return None
        return self.parent.__get_sinling()


class RedblackTree:
    # Конструктор класса.
    def __init__(self):
        self.root = None

    def __insert_fix(self, new_node):

        while new_node.parent and new_node.parent.color == 'red':
            # Рассмотрим случай, когда отец является левый сыном дедушки.
            if new_node.parent == new_node.__get_grandparent().left:

                # Берем брата отца, чтобы проверить красный он или синый, тоесть расс
                # матриваем левый или правый первый случай с картинки.
                uncle = new_node.__get_uncle()

                # Если дяд красный.
                if uncle and uncle.color == 'red':
                    new_node.parent.color = 'black'
                    new_node.__get_grandparent().color = 'red'
                    uncle.color = 'black'
                    new_node = new_node.__get_grandparent()

                # Если дядя черный.
                else:
                    # Случай 2.2 с картинки.
                    if new_node == new_node.parent.right:
                        pass




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




