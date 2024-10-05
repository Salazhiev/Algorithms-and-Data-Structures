class MaxHeap:
    def __init__(self, n=10):
        self.a = [0]*n
        self.n = 0
        self.lens = len(self.a)

    def getMax(self):
        if self.n > 0:
            return self.a[0]
        return None

    def extractMax(self):
        self.a[0], self.a[self.n-1] = self.a[self.n-1], self.a[0]

        self.n -= 1
        self.__siftDown(0)

    def insert(self, x):
        if self.n >= self.lens:
            self.a = self.a + [0] * self.lens
            self.lens *= 2

        self.a[self.n] = x
        self.n += 1

        self.__siftUp(self.n-1)


    def decreseKey(self, pos, delta):
        self.a[pos-1] += delta
        self.__siftUp(pos-1)


    def __siftUp(self, v):
        if v == 0: return
        p = v // 2 - 1 * (v % 2 == 0)
        if self.a[v] > self.a[p]:
            self.a[v], self.a[p] = self.a[p], self.a[v]
            self.__siftUp(p)


    def __siftDown(self, v):
        if 2*v >= self.n: return

        u = 2*v
        if v == 0:
            u += 1

        if u + 1 <= self.n and self.a[u] < self.a[u+1]:
            u += 1

        if self.a[u] < self.a[v]:
            self.a[u], self.a[v] = self.a[v], self.a[u]
            self.__siftDown(u)


