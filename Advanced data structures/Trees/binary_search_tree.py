class Tree:
    def __init__(self, val=None):
        self.value = val
        if self.value:
            self.left = Tree()
            self.right = Tree()
        else:
            self.left = None
            self.right = None

    # Вставка в бинарное дерево поиска
