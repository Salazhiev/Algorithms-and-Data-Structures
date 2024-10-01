
# https://www.cs.usfca.edu/~galles/visualization/BTree.html

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

    def find_max(self, root):
        while root.child[-1]:
            root = root.child[-1]
        return root[-1]

    def find_min(self, root):
        pass


    # Понимаю, что нахавеакодил удаление, но нет времени уменьшать код, в общем нормально.
    def delete(self, value):
        self.__delete(self.root, [None, None], value, True)

    # Функция принимает следующие аргументы:
    # root - узел с которым мы работаем на итерации.
    # arr_ - [Родитель root, ]
    def __delete(self, root, arr_, value, in_root):
        if in_root:
            # Если root - корневой узел.
            if root:
                for i in range(len(root.keys)):

                    if root.keys[i]>value and i==0:
                        if root.child and root.child[0]:
                            n_value = self.find_max(root.child[0])
                            root.keys[0] = n_value

                            return self.__delete(root.child[0], [root, 0], n_value, False)

                    elif root.keys[i]==value:

                        # Удаляемый элемент находится в корне и у корня есть дочерние узлы.
                        if root.child and root.child[i]:
                            n_value = self.find_max(root.child[i])
                            root.keys[i] = n_value

                            return self.__delete(root.child[i], [root, i], n_value, False)
                        else:
                            # Удаляемый узел находится на корне и при этом у него нет дочерних элементов.
                            del root.keys[i] # Просто удаляем и все готово.
                            return True

                    elif root.keys[i] > value:

                        if root.child and root.child[i]:
                            return self.__delete(root.child[i], [root, i], value, False)
                        else:
                            # Нет удаляемого узла.
                            return False

                    elif i+1==len(root.keys) and root.keys[-1] < value:
                        if root.child and root.child[-1]:
                            return self.__delete(root.child[-1], [root, -1], value, False)
                        else:
                            return False

        else:
            # Если код зашел сюда, это значит что мы работаем не с корневым узлом.


            # Посмотрим длину узла.
            if len(root.keys)>=self.t:

                # Ищем удаляемый элемент в узле.
                for i in range(len(root.keys)):
                    if root.keys[i] > value and i==0:
                        if root.child and root.child[0]:
                            n_value = self.find_max(root.child[0])
                            root.keys[i] = n_value

                            return self.__delete(root.child[0], [root, 0], n_value, False)
                        else:
                            del root.keys[i]
                            return True

                    elif root.keys[i]==value:

                        if root.child and root.child[i]:
                            n_value = self.find_max(root.child[i])
                            root.keys[i] = n_value

                            return self.__delete(root.child[i], [root, i], n_value, False)
                        else:
                            # Удаляемый узел находиться на листке, значит кайф, просто удаляем его и все.
                            del root.keys[i]
                            return True

                    elif root.keys[i] > value:
                        if root.child and root.child[i]:
                            return self.__delete(self.root.child[i],[root, i], value, False)
                        else:
                            return False

                    elif i+1==len(root.keys) and root.keys[-1] < value:
                        if root.child and root.child[-1]:
                            return self.__delete(root.child[-1], [root, -1], value, False)
                        else:
                            return False

            # Если код зашел в этот else, то мы работаем не с корневым узлом и длина удаляемого < t (т.е. она равна t-1).
            else:

                # Поменять длину и посмотреть нужно ли удалять в этом узле или нужно углубляться.

                # Длина оказалась t-1.
                # Первая попытка все починить.
                parent, index = tuple(arr_)



                # Проверка правого брата.
                if index != len(parent.keys)-1 and len(parent.child[index+1].keys) >= self.t:
                    z = parent.child[index+1].keys[0]
                    y = parent.keys[index]

                    parent.keys[index] = z
                    parent.child[index+1].keys = parent.child[index+1].keys[1:]
                    root.keys.append(y)

                    alpha = parent.child[index+1].child[0]
                    parent.child[index+1].child = parent.child[index+1][1:]

                    root.child.append(alpha)

                    # Длина была нормализована.

                    # Теперь ищем удаляемый элемент в обновленном узле
                    for i in range(len(root.keys)):
                        if root.keys[i] > value and i==0:
                            if root.child and root.child[0]:
                                n_value = self.find_max(root.child[0])
                                root.keys[i] = n_value

                                return self.__delete(root.child[0], [root, 0], n_value, False)
                            else:
                                del root.keys[i]
                                return True

                        elif root.keys[i]==value:

                            if root.child and root.child[i]:
                                n_value = self.find_max(root.child[i])
                                root.keys[i] = n_value

                                return self.__delete(root.child[i], [root, i], n_value, False)
                            else:
                                # Удаляемый узел находиться на листке, значит кайф, просто удаляем его и все.
                                del root.keys[i]
                                return True

                        elif root.keys[i] > value:
                            if root.child and root.child[i]:
                                return self.__delete(self.root.child[i],[root, i], value, False)
                            else:
                                return False

                        elif i+1==len(root.keys) and root.keys[-1] < value:
                            if root.child and root.child[-1]:
                                return self.__delete(root.child[-1], [root, -1], value, False)
                            else:
                                return False


                # Если правый брат нам не подходит, проверим левого брата.
                elif index != 0 and len(parent.child[index-1].keys) >= self.t:

                    z = parent.child[index-1].keys[-1]
                    y = parent.keys[index]

                    parent.keys[index] = z
                    parent.child[index-1].keys = parent.child[index-1].keys[:-1]
                    root.keys = [y] + root.keys

                    alpha = parent.child[index-1].child.pop()

                    root.child = [alpha] + root.child


                    # Теперь ищем удаляемый элемент в обновленном узле.
                    for i in range(len(root.keys)):
                        if root.keys[i] > value and i==0:
                            if root.child and root.child[0]:
                                n_value = self.find_max(root.child[0])
                                root.keys[i] = n_value

                                return self.__delete(root.child[0], [root, 0], n_value, False)
                            else:
                                del root.keys[i]
                                return True

                        elif root.keys[i]==value:

                            if root.child and root.child[i]:
                                n_value = self.find_max(root.child[i])
                                root.keys[i] = n_value

                                return self.__delete(root.child[i], [root, i], n_value, False)
                            else:
                                # Удаляемый узел находиться на листке, значит кайф, просто удаляем его и все.
                                del root.keys[i]
                                return True

                        elif root.keys[i] > value:
                            if root.child and root.child[i]:
                                return self.__delete(self.root.child[i],[root, i], value, False)
                            else:
                                return False

                        elif i+1==len(root.keys) and root.keys[-1] < value:
                            if root.child and root.child[-1]:
                                return self.__delete(root.child[-1], [root, -1], value, False)
                            else:
                                return False


                # Если не получается поработать с братьям, то объеденим два брата с t-1 длиной.
                # А так мы можем сделать так как родитель горантировано будет с длиной >=t, мы сделали его таковым
                # на предыдущей итарации рекурсии.
                elif index!=len(root.keys)-1 and len(root.keys)==self.t-1 and len(parent.child[index+1].keys)==self.t-1:

                    # Сплит с правым братом.

                    y = parent.keys[index]
                    D = parent.child[index+1]
                    del parent.keys[index+1]
                    del parent.child[index+1]


                    root.keys.append(y)
                    root.keys += D.keys
                    root.child += D.child


                    # ХЗ сработает ли, посмотрим.
                    flag = self.__delete(root, [parent, None], value, False)

                    if self.root is parent and len(parent.keys)==0:
                        self.root = root
                    return flag


                elif index!=0 and len(root.keys)==self.t-1 and len(parent.child[index-1].keys)==self.t-1:

                    # Сплит с левым братом.
                    y = parent.keys[index]
                    D = parent.child[index-1]
                    del parent.keys[index-1]
                    del parent.child[index-1]

                    root.keys = [y] + root.keys
                    root.keys = D.keys + root.keys
                    root.child = D.child + root.child


                    flag = self.__delete(root, [parent, None], value, False)
                    if self.root is parent and len(parent.keys)==0:
                        self.root = root
                    return flag

        return False

b = BTree(3)
b.insert(5)
b.insert(10)
b.insert(15)
b.insert(20)
b.insert(25)
b.insert(31)
b.delete(20)
b.delete(31)

print()






