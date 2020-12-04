# Write a function revstring(mystr) that uses a stack to reverse the characters in a string.

from test import testEqual

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)



def revstring(mystr):
    newstr = ''
    astack = Stack()
    for ch in mystr:
        astack.push(ch)
    while not astack.isEmpty():
        newstr = newstr + astack.pop()

    return newstr

print(revstring('cat'))

testEqual(revstring('apple'), 'elppa')
testEqual(revstring('x'), 'x')
testEqual(revstring('1234567890'), '0987654321')
testEqual(revstring(''), '')
