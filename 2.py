''' Под категорию FIFO попадает всем известое queue
    Сначала будет приведена неоптимальная реализация
    на базе массива Queue1. Неоптимальность заключается
    в линейности операции вставки.

    Далее будет более оптимальный (O(1) для insert) вариант Queue2
'''

class Queue1:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

#-----------------------------------------------------------------#


class Node:
    ''' Класс узла -- очередь будет на основе list'''
    def __init__(self, item = None):
        self.item = item
        self.next = None
        self.previous = None


class Queue2:
    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None

    def enqueue(self, value):
        newNode = Node(value)
        if self.head is None:
            self.head = self.tail = newNode
        else:
            self.head.previous = NewNode
            NewNode.next = self.head
            self.head = NewNode
        self.length += 1

    def dequeue(self):
        if self.head is None:
            return None

        elif self.head == self.tail:
            item = self.head.item
            self.head = self.tail = None
            self.length -= 1
            return item

        else:
            item = self.tail.item
            self.tail = self.tail.prev 
            self.length -= 1
        return item

    def size(self):
        return self.length

    def isEmpty(self):
        return self.head == None

