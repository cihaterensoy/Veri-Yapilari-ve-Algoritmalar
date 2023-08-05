from queue import Queue
from typing import Deque


class MyStack():

    def __init__(self):
        self.elements = Deque()
    def push(self,element):
        self.elements.append(element)
    def pop(self):
        for i in range(len(self.elements)-1):
            self.elements.append(self.elements.popleft())
        return self.elements.popleft()

    def top(self):
        return self.elements[-1]
    def empty(self):
        return len(self.elements) == 0

veri = MyStack()

veri.push(10)
veri.push(20)
veri.push(30)
print(veri.pop())


"""
**********LeetCode'da kabul edilmeyen kod************

class ImplementStackUsingQueues():

    def __init__(self):
        self.elements = Queue()


    def push(self,element):
        self.elements.put(element)

    def pop(self):
        value = 0
        yeniStack = Queue()
        for i in range(self.elements.qsize()-1):
            value = self.elements.queue[i]
            yeniStack.put(value)
        self.elements = yeniStack

    def empty(self):
        return self.elements.empty()
    def top(self):
        return self.elements.queue[-1]
    def yazdir(self):
        print(self.elements.queue)




myStack = ImplementStackUsingQueues()

myStack.push(10)
myStack.push(20)
myStack.push(30)

#print(myStack.top())
myStack.yazdir()
myStack.pop()
#print(myStack.top())
myStack.yazdir()







"""