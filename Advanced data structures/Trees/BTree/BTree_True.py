class BTreeNode:
    def __init__(self, leaf=False):
        self.keys = []
        self.child = []
        self.leaf = leaf


class BTree:
    def __init__(self, t):
        self.root = BTreeNode(True)
        self.t = t

    def insert(self, k):
        root = self.root
        if len(root.keys) == (2 * self.t) - 1:
            temp = BTreeNode()
            self.root = temp
            temp.child.insert(0, root)
            self.split_child(temp, 0)
            self.insert_non_full(temp, k)
        else:
            self.insert_non_full(root, k)

    def insert_non_full(self, x, k):
        i = len(x.keys) - 1
        if x.leaf:
            x.keys.append((None, None))
            while i >= 0 and k < x.keys[i]:
                x.keys[i + 1] = x.keys[i]
                i -= 1
            x.keys[i + 1] = k
        else:
            while i >= 0 and k < x.keys[i]:
                i -= 1
            i += 1
            if len(x.child[i].keys) == (2 * self.t) - 1:
                self.split_child(x, i)
                if k > x.keys[i]:
                    i += 1
            self.insert_non_full(x.child[i], k)

    def split_child(self, x, i):
        t = self.t
        y = x.child[i]
        z = BTreeNode(y.leaf)
        x.child.insert(i + 1, z)
        x.keys.insert(i, y.keys[t - 1])
        z.keys = y.keys[t:(2 * t) - 1]
        y.keys = y.keys[0:t - 1]
        if not y.leaf:
            z.child = y.child[t:(2 * t)]
            y.child = y.child[0:t - 1]

    def delete(self, k):
        self.delete_recursive(self.root, k)

    def delete_recursive(self, x, k):
        i = 0
        while i < len(x.keys) and k > x.keys[i]:
            i += 1

        if i < len(x.keys) and k == x.keys[i]:
            if x.leaf:
                x.keys.pop(i)
            else:
                y = x.child[i]
                z = x.child[i + 1]
                if len(y.keys) >= self.t:
                    predecessor = self.get_predecessor(y)
                    x.keys[i] = predecessor
                    self.delete_recursive(y, predecessor)
                elif len(z.keys) >= self.t:
                    successor = self.get_successor(z)
                    x.keys[i] = successor
                    self.delete_recursive(z, successor)
                else:
                    self.merge_nodes(x, i, y, z)
                    self.delete_recursive(y, k)
        else:
            if x.leaf:
                print(f"Key {k} does not exist in the B-tree.")
            else:
                if len(x.child[i].keys) < self.t:
                    self.fix_child(x, i)

                self.delete_recursive(x.child[i], k)

    def get_predecessor(self, x):
        while not x.leaf:
            x = x.child[-1]
        return x.keys[-1]

    def get_successor(self, x):
        while not x.leaf:
            x = x.child[0]
        return x.keys[0]

    def merge_nodes(self, x, i, y, z):
        y.keys.append(x.keys[i])
        y.keys.extend(z.keys)
        y.child.extend(z.child)
        x.keys.pop(i)
        x.child.pop(i + 1)

        if len(x.keys) == 0:
            self.root = y

    def fix_child(self, x, i):
        if i > 0 and len(x.child[i - 1].keys) >= self.t:
            self.borrow_from_left(x, i)
        elif i < len(x.child) - 1 and len(x.child[i + 1].keys) >= self.t:
            self.borrow_from_right(x, i)
        else:
            if i > 0:
                self.merge_nodes(x, i - 1, x.child[i - 1], x.child[i])
                i -= 1
            else:
                self.merge_nodes(x, i, x.child[i], x.child[i + 1])

    def borrow_from_left(self, x, i):
        child = x.child[i]
        sibling = x.child[i - 1]

        child.keys.insert(0, x.keys[i - 1])
        x.keys[i - 1] = sibling.keys.pop()
        if not child.leaf:
            child.child.insert(0, sibling.child.pop())

    def borrow_from_right(self, x, i):
        child = x.child[i]
        sibling = x.child[i + 1]

        child.keys.append(x.keys[i])
        x.keys[i] = sibling.keys.pop(0)
        if not child.leaf:
            child.child.append(sibling.child.pop(0))

    def search(self, k, x=None):
        x = x or self.root
        if isinstance(x, BTreeNode):
            i = 0
            while i < len(x.keys) and k > x.keys[i]:
                i += 1
            if i < len(x.keys) and k == x.keys[i]:
                return x, i
            elif x.leaf:
                return None
            else:
                return self.search(k, x.child[i])
        else:
            return self.search(k, self.root)

    def display(self, x=None):
        x = x or self.root
        for i in x.keys:
            if i != (None, None):
                print(i, end=" ")
        if not x.leaf:
            for i in x.child:
                self.display(i)


b = BTree(3)
b.insert(1)
b.insert(2)
b.insert(3)
b.insert(4)
b.insert(5)
b.insert(6)
b.insert(0)
print()