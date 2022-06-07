# класс Node для определения элемента списка
class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


# Создаем список для того, чтобы поместить туда рейсы, подходящие запросам пользователя
class LinkedList:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def __str__(self):
        if self.first is not None:
            current = self.first
            out = str(current.value) + ' '
            while current.next is not None:
                current = current.next
                out += str(current.value) + ' '
            return out
        return 'LinkedList []'

    def clear(self):
        self.__init__()

    def add(self, x):
        self.length += 1
        if self.first == None:
            # self.first и self.last будут указывать на одну область памяти
            self.last = self.first = Node(x, None)
        else:
            # здесь, уже на разные, т.к. произошло присваивание
            self.last.next = self.last = Node(x, None)

    def Del(self, i):
        if (self.first == None):
            return
        curr = self.first
        count = 0
        if i == 0:
            self.first = self.first.next
            return
        while curr != None:
            if count == i:
                if curr.next == None:
                    self.last = curr
                old.next = curr.next
                break
            old = curr
            curr = curr.next
            count += 1

    def __getitem__(self, key):  # поддержка обращения по ключу
        length = 0
        current = None
        if self.first is not None:
            current = self.first
            while key != length:
                current = current.next
                length += 1
            if key == length:
                current = current.value
        return current
