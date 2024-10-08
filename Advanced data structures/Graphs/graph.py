# Ребро.
class Edge:
    def __init__(self, from_, to_, weight=1):
        # Ребро с какой вершины. В нем хранится объект класса Vertex.
        self.from_ = from_
        # На какую вершину. В нем храниться объект класса Vertex.
        self.to_ = to_
        # Вес наша графа, если он нагруженный
        self.weight = weight

    def __str__(self):
        return f'({self.from_};{self.to_}) и вес {self.weight}'


# Вершина.
class Vertex:
    def __init__(self, name):
        # Идентификатор вершин.
        self.name = name


# Сам граф.
class Graph:
    def __init__(self, oriented = False):
        # Массив вершин графа. В этом массиве хранятся объекты класса Vertex.
        self.V = []
        # Массив ребер графа. В этом массиве хранятся объекты класса Edge
        self.E = []
        # Ориентированность наша графа.
        self.oriented = oriented



    # Метод для добавления вершин в наш граф.
    def addVertex(self, v):

        self.V.append(v)



    # Метод для добавления ребер в наш граф.
    def addEdge(self, from_, to_):
        edge = Edge(from_, to_)
        self.E.append(edge)



    # Генерирует матрицу смежности.
    def getMatrixGtaphs(self):
        # Матрица смежности, которую будем строить.
        matrix = [ [0]*len(self.V) for _ in range(len(self.V)) ]

        # Перебираем наши ребра.
        for edge in self.E:
            i, j = edge.from_.name, edge.to_.name
            matrix[i-1][j-1] = edge.weight

        for a in matrix:
            print(a)


    # Генерирует список смежных вершин.
    def getVertexLists(self):
        for vertex in self.V:
            self.getOneVertexLists(vertex)


    # Генерирует список смежных вершин с данной.
    def getOneVertexLists(self, vertex):
        # Передаем вершину и получаем все смежные с ней.
        result = []
        # print(vertex.name, end=': ')
        for edge in self.E:
            if edge.from_ is vertex:
                # print(edge.to_.name, end=' ')
                result.append(edge.to_)
        # print()

        return result


    # Волновой алгоритм поиска пути от A до B графе.
    def wave(self, start_, finish_):

        v = [start_]
        visited_vertex = []
        while v:
            vn = []
            for v_ in v:
                if v_ not in visited_vertex:
                    visited_vertex.append(v_)
                    for vertex in self.getOneVertexLists(v_):
                        if vertex is finish_:
                            return True
                        vn.append(vertex)
            v = vn

        return False


    # Волновой алгоритм поиска пути от A до B в графе с выводом пути.
    def wave_road(self, s, f):
        pass




g = Graph(True)
v1 = Vertex(1)
v2 = Vertex(2)
v3 = Vertex(3)
v4 = Vertex(4)
v5 = Vertex(5)
v6 = Vertex(6)
v7 = Vertex(7)

g.addVertex(v1)
g.addVertex(v2)
g.addVertex(v3)
g.addVertex(v4)
g.addVertex(v5)
g.addVertex(v6)
g.addVertex(v7)

g.addEdge(v1, v2)
g.addEdge(v1, v3)
g.addEdge(v3, v4)
g.addEdge(v2, v5)
g.addEdge(v2, v6)
g.addEdge(v6, v5)
g.addEdge(v5, v6)

g.getMatrixGtaphs()
g.getVertexLists()

print()
print(g.wave(v1, v7))