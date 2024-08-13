# Создаем класс узлов наших.
class Node:
    def __init__(self, val: int, next=None) -> None:
        # При инициализации создаем значение узла и следующий узел.
        self.val = val
        self.next = next

# Класс для работы непосредственно с самим классом.
class cycle_singly_LinkedList:
    # Переменная для подсчета количества узлов.
    lens = 0
    def __init__(self) -> None:
        # Создаем первый узел без значений в себе.
        # Head - указатель на первый узел.
        # Tail - указатель на последний узел.
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.tail.next = self.head



    # Добавление узла в конец списка.
    def adding_to_the_end(self, val: int) -> None:
        self.lens += 1
        newNode = Node(val=val)
        # Если наш список пустой, то заходим в это условие
        if self.head.val == None:
            # Так как у нас после работы этого куска кода, будет только
            # один узел, то очевидно, что и голова и хвост будут указывать
            # именно на него.
            self.head = newNode
            self.tail = newNode

            # Заворчачиваем списко в себя же.
            newNode.next = self.head
        else:
            # Если у нас в списке есть элементы,
            # добавляем в конец списка новый элемент
            self.tail.next = newNode

            # Меняем указатель на хвостовой элемент, в ново добавленный.
            self.tail = newNode

            # Заворачиваем список в себя же.
            self.tail.next = self.head



    # Добавление узла в начало.
    def addding_to_the_beginnig(self, val: int) -> None:
        self.lens += 1
        # Создание нового узла.
        newNode = Node(val=val)
        # Если наш список пуст, то создаем узел и указываем на этот узел голову и хвост.
        if self.head.val==None:
            # Данную строчку уже объяснял.
            self.head = newNode
            self.tail = newNode

            newNode.next = self.head

        else:
            # В этих двух строчка меняем головной элемент списка.
            newNode.next = self.head
            self.head = newNode

            # В данной строчке, мы зацикливаем наш список.
            self.tail.next = self.head



    # Добавление узла по номеру(после введенного номера), нумерация начинается с 1
    def adding_to_the_number(self, num: int, val: int) -> None or str:
        if num>self.lens:
            num=self.lens
        elif num<0:
            num=0

        self.lens += 1
        newNode = Node(val=val)
        if num==0:
            # Здесь можно просто запустить функцию addding_to_the_beginnig, и особо не париться,
            # но для общего развития я все распишу.

            # Проверка на то, что у нас вообще нет узлов в списке
            if self.head.val == None:
                self.head = newNode
                self.tail = newNode
                newNode.next = self.head
            else:
                newNode.next = self.head
                self.head = newNode
                self.tail.next = self.head
            return

        # Перебираем узлы до тех пор, пока не наткнемся на нужный нам узел.
        current = self.head
        while True:
            # Условие на проверку того, нашли ли мы необходимый узел в списке.
            if num==1:
                # Сохраняем следующий узел относительно указателя current.
                nxt = current.next
                # Меняем слудеющий узел относительно указателя current на новый узел.
                current.next = newNode
                # Следующий узел относительно нового добалвенного узела, будет то самое продолжаение
                # которое было сохранено несколько строчек назад.
                newNode.next = nxt
                return

            # Гуляем по узлам, как цикл над обычным массивом.
            current = current.next
            num -= 1



    # Вывод на экран значений узлов.
    def outputs(self) -> None:
        # Берем головной элемент.
        current = self.head
        # Если головной элемент не содержит в себе элементов, из чего следует что его в общем та нет.
        # То мы выводим на экран просто текст, мол нет тут элементов.
        if current.val==None:
            print('Элементов в списке нет!')
            return

        # Если же нам список не пуст, то мы просто гуляем по списку выводя на экран значение
        # каждого списка.
        a = self.lens
        while a>0:
            print(current.val, end=' ')
            a-=1
            current = current.next
        print()



    # Проверка наличия элемента по значению.
    def search(self, val: int) -> bool:
        # Берем главный головной элемент
        current = self.head
        # Сохраняем количество элементов в переменной, чтобы иметь какой то порог остановления
        # цикла для поиска.
        a = self.lens
        while a>-1:
            a-=1
            # Проверка на равенство значений.
            if current.val==val:
                return True
            # Бегаем по массиву.
            current = current.next
        return False


    # Удаление элемента с конца.
    def pop(self) -> None:
        # Если наш список пустой, то нет смысла что либо удалять.
        if self.head.val==None:
            print('В спиике нет элементов!')
            return

        # Создаем указательно на головной элемент.
        current = self.head
        while current.next!=self.tail:
            # Цикл для поиска узла, стоящего перед хвостовым узлом.
            current = current.next

        # Находим небохдимый узел меняем связи для избавления от него.
        current.next = self.head
        self.tail = current
        self.lens -= 1

    # Перевеорот спрска на О(1)
    def reverse(self) -> None:
        # Создаем указатель на хвост списка.
        prev = self.tail # Предыдущий
        # Создаем указатель на голову списка.
        current = self.head # Этот

        # Создаем счетчик для работы с циклом.
        a = self.lens
        while a>0:
            # В самом начале, мы меняем значений хвостового элемента на головной.
            if a==self.lens:
                self.tail = current
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
            a-=1

        # Меняем головной элемент.
        self.head = prev


    # Получить узел по индексу, индексация начинается с 1
    def get_node_index(self, index: int) -> str or Node:
        # Если инедкс не входит в рамки массива, то смысла нет в поиске.
        if index>self.lens or index <= 0:
            return 'Такого индекса нет в списке'

        # Берем головной элемент.
        current = self.head
        # Бегаем по узлам и останавлеваемся когда доходим до индекса index хаха смешно.
        for _ in range(index-1):
            current = current.next
        # Ну и возвращаем этот элемент, на котором мы остановились.
        return current


    # Получить узел по значению.
    def get_node_val(self, val: int) -> str or Node:
        current = self.head

        # Думаю с этим кодом все максимально понятно.
        for _ in range(self.lens):
            if current.val==val:
                return current
            current = current.next
        return 'Нет узла с таким значением'


    # Удаление узла по индексу, индексация начинается 1.
    def remove_node_index(self, index: int) -> None:
        if index>self.lens or index<=0:
            print('Такого индекса нет в списке')
            return

        self.lens -= 1
        if index==1:
            if self.lens==1:
                self.head.val = None
                self.tail.val = None
                return

            self.head = self.head.next
            self.tail.next = self.head

        # НЕ РАБОТАЕТ ДАННАЯ ФУНКЦИЯ, ТАКЖЕ ПРОВЕРИТЬ РАБОТАЕТ ЛИ ВСЕ В ДВУХ ДРУГИХ ПРОЕКТАХ,  ТАК КАК
        # ПОЯВИЛИСЬ СОМНЕНИЯ, ЧТО ВСЕ РАБОТАЕТ!!!




# проверим для начала вывод на экран элементов, дальше проверим функцию добавления по номеру.

l = cycle_singly_LinkedList()
l.adding_to_the_end(10)
l.adding_to_the_end(11)
l.adding_to_the_end(12)
l.adding_to_the_end(13)
l.adding_to_the_end(14)
l.outputs()
l.remove_node_index(1)
l.outputs()

print(1)
