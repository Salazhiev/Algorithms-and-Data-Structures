class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None


    def __find(self, node, parent, value):
        if node is None:
            return None, parent, False

        if value==node.data:
            return node, parent, True

        if value < node.data:
            if node.left:
                return self.__find(node.left, node, value)
        if value > node.data:
            if node.right:
                return self.__find(node.right, node, value)
        # node - узел к которому мы будем добавлять новый узел.
        # parent - родительский узел для node.
        return node, parent, False


    def append(self, obj: Node):
        if self.root is None:
            self.root = obj
            return obj

        s, p, fl_find = self.__find(self.root, None, obj.data)

        if fl_find == False and s:
            if obj.data < s.data:
                s.left = obj
            else:
                s.right = obj

        return obj


    # Отображение элементов с обходом дерева в глубину.
    def show_tree(self, node):
        if node is None:
            return

        self.show_tree(node.left)
        print(node.data)
        self.show_tree(node.right)


    # Отображение элементов с обходом дерева в ширину
    def show_wide_tree(self, node):
        if node is None:
            return

        v = [node]
        while v:
            vn = []
            for x in v:
                print(x.data, end=' ')
                if x.left:
                    vn += [x.left]
                if x.right:
                    vn += [x.right]
            print()
            v = vn


    def __del_leaf(self, s, p):
        if p.left == s:
            p.left = None
        elif p.right == s:
            p.right = None
    def __del_one_child(self, s, p):
        if p.left == s:
            if s.left is None:
                p.left = s.right
            elif s.right is None:
                p.left = s.left
        elif p.right == s:
            if s.left is None:
                p.right = s.right
            elif s.right is None:
                p.right = s.left
    def __find_min(self, node, parent):
        if node.left:
            return self.__find_min(node.left, node)

        return node, parent


    def del_node(self, key):
        s, p, fl_find = self.__find(self.root, None, key)

        if fl_find==False:
            return None

        if s.left is None and s.right is None:
            self.__del_leaf(s, p)
        elif s.left is None or s.right is None:
            self.__del_one_child(s, p)
        else:
            sr, pr = self.__find_min(s.right, s)
            s.data = sr.data
            self.__del_one_child(sr, pr)



v = [10, 5 ,7 ,16 ,13 ,2 ,20]
t = Tree()

for x in v:
    t.append(Node(x))

t.del_node(5)
t.show_wide_tree(t.root)
