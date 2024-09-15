import random

class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None
        self.height = 1


class AVLTree:
    def __init__(self):
        self.root = None

    def height(self, node):
        if not node:
            return 0
        return node.height


    # Функция возвращает разницу между высотой левым подузлом и правым подузлом.
    # Тоесть на вход некий узел.
    def balance(self, node):
        if not node:
            return 0
        return self.height(node.left) - self.height(node.right)

    # Вспомогательная функция для добавления элемента, на вход поступает
    # значение добавляемого узла, а вернуть должен корневой узел, старый либа новый.
    def __insert(self, root, value):
        # Для начала мы добавляем новый элемент рекурсей.
        if not root:
            return Node(value)
        elif value < root.value:
            root.left = self.__insert(root.left, value)
        else:
            root.right = self.__insert(root.right, value)
        
        # После того как мы добавили новый узел в нужное место, важно понимать что балансировку
        # нужно делать снизу верх, поэтому мы не выходим с "конеченые липистик".
        
        # Вычисляем новую высоту.
        root.height = 1 + max(self.height(root.left), self.height(root.right))
        # Вычисляем ту самую разницу.
        b = self.balance(root)

        # Смотрим сбалнсированно ли наше дерево и если оно будет не сбалансированным балансируем его.



        # Провека на необходимость малого левого вращения.
        if b == -2 and value > root.right.value:
            # Высота левого под дерева - высота правого под дерева = 2 и
            # высота правого под дерева правого под дерева больше или равно высоте левого под дерева правого под дерева.
            return self.left_rotation(root)


        # Проверека на необходмость большого левого вращения.
        if b == -2 and value < root.right.value:
            return self.big_left_rotation(root)



        # Провека на необходимость малого правого вращения.
        if b == 2 and value < root.left.value:
            return self.right_rotation(root)



        #Проверка на необходмость большого правого вращения
        if b == 2 and value > root.left.value:
            return self.big_right_rotation(root)

        return root

    def __delete(self, root, value):
            


    def delete_value(self, value):
        self.root = self.__delete(self.root, value)


    # Левое вращение
    def left_rotation(self, a):
        b = a.right
        C = b.left

        b.left = a
        a.right = C


        a.height = 1 + max(self.height(a.left), self.height(a.right))
        b.height = 1 + max(self.height(b.left), self.height(b.right))


        return b

    # Правое вращение
    def right_rotation(self, b):
        a = b.left
        C = a.right

        a.right = b
        b.left = C


        b.height = 1 + max(self.height(b.left), self.height(b.right))
        a.height = 1 + max(self.height(a.left), self.height(a.right))


        return a

    # Большое левое вращение
    def big_left_rotation(self, a):
        b = a.right
        c = b.left
        M = c.left
        N = c.right


        a.right = M
        b.left = N
        c.left = a
        c.right = b

        a.height = 1 + max(self.height(a.left), self.height(a.right))
        b.height = 1 + max(self.height(b.left), self.height(b.right))
        c.height = 1 + max(self.height(c.left), self.height(c.right))

        return c

    def big_right_rotation(self, a):
        b = a.left
        c = b.right
        M = c.right
        N = c.left

        a.left = M
        b.right = N
        c.left = b
        c.right = a

        a.height = 1 + max(self.height(a.left), self.height(a.right))
        b.height = 1 + max(self.height(b.left), self.height(b.right))
        c.height = 1 + max(self.height(c.left), self.height(c.right))

        return c


    # функция, которая вызивает вспомогательную функцию добавления, а данная функця меняет
    # корневой узел на новый, если он измениться.
    def insert_value(self, value):
        self.root = self.__insert(self.root, value)


    def min_value_node(self, root):
        current = root
        while current.left:
            current = current.left
        return current

    # Нужно вернуть узел, с таким значением value, на вход корневой узел и значение value
    def __search(self, root, value):
        if not root or root.value == value:
            return root
        if root.value < value:
            return self.__search(root.right, value)
        else:
            return self.__search(root.left, value)

    def search_value(self, value):
        return self.__search(self.root, value)






arr = [
    [1,2,3,4,5,6,7,8]
]

for i in range(8):
    tree = AVLTree()
    for j in range(8):
        tree.insert_value(arr[i][j])

    print()
