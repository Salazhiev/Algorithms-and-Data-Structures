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
    # Количесто вершин.
    len_vertex = 0
    # Количество ребер.
    len_edge = 0
    # Матрица смежности.
    matrix = []

    def __init__(self, oriented = False):
        # Массив вершин графа. В этом массиве хранятся объекты класса Vertex.
        self.V = []
        # Массив ребер графа. В этом массиве хранятся объекты класса Edge
        self.E = []
        # Ориентированность наша графа.
        self.oriented = oriented



    # Метод для добавления вершин в наш граф.
    # Понятно, что можно по манипулировать с этим методом, чтобы он не принимал на вход
    # сами непосредственно объекты класса Vertex, а в этом методе, их создавать и добавлять
    # в наш класс.
    def addVertex(self, v):
        # Получаем объект класса Vertex, добавляем его просто в массив вершин.
        self.V.append(v)
        self.len_vertex += 1

        # обновляем матрицу смежности.
        self.matrix.append([0]*self.len_vertex)
        for i in range(self.len_vertex):
            self.matrix[i].append(0)




    # Метод для добавления ребер в наш граф.
    # На вход принимает два объекта класса Edge, откуда и куда.
    def addEdge(self, from_, to_):
        # Вспомогательный флаг, для неориентированного графа, а если точнее
        # не произошла хрень, при добавлении элементов.
        flag = True
        self.len_edge += 1

        # Создаем экземпляр класса Edge - ребро
        edge = Edge(from_, to_)

        # Если наш граф неориентированный, то добавляем как один путь, так и второй.
        if self.oriented == False:
            edge_ = Edge(to_, from_)

            # Важно учитывать также, что мы случайно можем добавить один и тот же путь дважды, поэтому
            # Этот момент тоже надо контролировать.
            for e in self.E:
                if e.from_ is edge_.from_ and e.to_ is edge_.to_:
                    flag = False
            if flag:
                # Обновляем матрицу смежности.
                self.matrix[edge_.from_.name-1][edge_.to_.name-1] = edge_.weight
                # Добавляем в массив ребер, новое ребро.
                self.E.append(edge_)

        # Опять проверка на случай, если наш граф ориентированнный.
        flag = True
        if self.oriented==False:
            for e in self.E:
                if e.from_ is edge.from_ and e.to_ is edge.to_:
                    flag = False
        if flag:
            # Обновляем матрицу смежности.
            self.matrix[edge.from_.name-1][edge.to_.name-1] = edge.weight
            # Добавляем в массив ребер, новое ребро.
            self.E.append(edge)



    # Генерирует список смежных вершин.
    def getVertexLists(self):
        for vertex in self.V:
            self.getOneVertexLists(vertex)



    # Генерирует список смежных вершин с данной.
    def getOneVertexLists(self, vertex):
        # Передаем вершину и получаем все смежные с ней.
        result = []
        print(vertex.name, end=': ')
        for edge in self.E:
            if edge.from_ is vertex:
                print(edge.to_.name, end=' ')
                result.append(edge.to_)
        print()

        return result


    # Волновой алгоритм поиска пути от A до B графе.
    # Насколько я понял, это также обход графа в ширину.
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

                        # Данное условие нужно для неориентированного графа.
                        if self.oriented==False and vertex not in visited_vertex:
                            vn.append(vertex)
                        elif self.oriented==True:
                            vn.append(vertex)
            v = vn

        return False


    # Обход графа в глубину для поиска элемента в графе.
    # ПОЕБНЯ НЕ РАБОТАЕТ ПОКА ЧТО, НУЖНО ИСПРАВИТЬ ХРЕНЬ В ОБЩЕМ.
    def search(self, s, f, arr):
        if s is f:
            return True


        for vertex in self.getOneVertexLists(s):
            if vertex is arr:
                continue

            arr.append(vertex)
            return self.search(vertex, f, arr)







    # Волновой алгоритм поиска пути от A до B в графе с выводом пути.
    def wave_road(self, s, f):
        pass


    def __len__(self):
        flag = 'Ориентированном'
        if self.oriented == False:
            flag = 'Неориентированном'
        return f'Количество вершин в {flag}:{self.len_vertex},  ребер{self.len_edge}'


    def __str__(self):
        result = ''
        for a in self.matrix:
            result += str(a)+'\n'
        return result




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
g.addEdge(v1, v7)

g.getVertexLists()


print(g)
print(g.wave(v1, v6))

print(g.search(v1, v4, []))