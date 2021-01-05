# Implementing Queue ADT
class Queue:
    def __int__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

q = Queue()
#
print(q.enqueue(4))
# print(q.enqueue('dog'))
# print(q.enqueue(True))
# print(q.size())
