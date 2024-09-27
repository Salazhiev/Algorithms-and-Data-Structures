class BTreeNode:
    def __init__(self, leaf=False):
        self.leaf = leaf # Проверка есть ли хоть один ключ в узле.
        self.keys = [] # Количество ключей: если корень [1, 2t-1], если не корень [t-1,2t-1]
        self.child = [] # Количество детей: если дети корня, то [2, 2t], если не корень [t, 2t]

    def display(self, level=0):
        print(f'Level {level}: {self.keys}')
        if not self.leaf:
            for child in self.child:
                child.display(level + 1)


class BTree:
    # t - главный параметр в B-Дереве.
    def __init__(self, t):
        self.root = None
        self.t = t

    # Поиска узла в B-Дереве.
    def search(self, value):
        current = self.root
        while current:
            for i in range(len(current.child)):
                if current.keys[i]==value:
                    return current.child[i]

                if current.keys[i]>value:
                    current = current.child[i]
                elif current.keys[i]<value and i==len(current.child)-1:
                    current = current.child[-1]
        return None


    # Небольшая работа с
    def insert(self,value):
        print()
        if self.root == None:
            self.root = BTreeNode(True)
            self.root.keys.append(value)
            return
        else:
            # Если длина корневого узла избыточна.
            if len(self.root.keys) == (2 * self.t) - 1:
                node = BTreeNode(True)
                node.keys.append(self.root.keys[self.t-1])

                A = BTreeNode(True)
                B = BTreeNode(True)

                for i in range((2 * self.t) - 1):
                    if i < self.t - 1:
                        A.keys.append(self.root.keys[i])
                        if self.root.child:
                            A.child.append(self.root.child[i])
                    elif i > self.t - 1:
                        B.keys.append(self.root.keys[i])
                        if self.root.child:
                            B.child.append(self.root.child[i])
                    else:
                        if self.root.child:
                            A.child.append(self.root.child[i])
                if self.root.child:
                    B.child.append(self.root.child[-1])

                node.child.append(A)
                node.child.append(B)

                self.root = node

        self.__insert(self.root, None ,value)

    def __insert(self, root, parent, value):
        print()
        # Если нет отца, значит его длина не избыточна, так как мы проверяли его
        # избыточность до того как запуститься эта функция.
        if parent:
            if len(root.keys) == 2 * self.t - 1:

                A = BTreeNode(True)
                B = BTreeNode(True)

                for i in range(2*self.t-1):
                    if i < self.t - 1:
                        A.keys.append(root.keys[i])
                        if root.child:
                            A.child.append(root.child[i])
                    elif i > self.t - 1:
                        B.keys.append(root.keys[i])
                        if root.child:
                            B.child.append(root.child[i])
                    else:
                        if root.child:
                            A.child.append(root.child[i])
                if root.child:
                    B.child.append(root.child[-1])

                x = root.keys[self.t - 1] # Элемент который должен быть подвешен на верх
                flag = True
                for i in range(len(parent.keys)):
                    if x < parent.keys[i] and i==0:
                        parent.keys = [x] + parent.keys
                        parent.child[0] = B
                        parent.child = [A] + parent.child
                        flag=False
                        break
                    elif x < parent.keys[i]:
                        parent.keys.append(x)
                        parent.keys.sort()
                        parent.child = parent.child[:i] + [A] + [B] + parent.child[i:]
                        flag=False
                        break

                if x > parent.keys[-1] and flag:
                    parent.keys.append(x)
                    parent.child[-1] = A
                    parent.child.append(B)

                if x < value:
                    root = B
                else:
                    root = A




        for i in range(len(root.keys)):
            if root.child and root.keys[i] > value and i==0:
                if root.child[0]:
                    self.__insert(root.child[0], root, value)
                else:
                    root.keys = [value] + root.keys
                return


            if root.keys[i] > value:
                if root.child and root.child[i]:
                    self.__insert(root.child[i], root, value)
                else:
                    root.keys.append(value)
                    root.keys.sort()
                return
                    

        if root.keys[-1] < value:
            if root.child and root.child[-1]:
                self.__insert(root.child[-1], root, value)
            else:
                root.keys.append(value)
        return


b = BTree(2)
b.insert(1)
b.insert(2)
b.insert(3)
b.insert(4)
b.insert(5)
b.insert(6)
b.insert(0)
print()