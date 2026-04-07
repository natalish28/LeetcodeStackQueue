class Node:
    def __init__(self, x):
        self.val = x
        self.next = None

class Queue:
    def __init__(self):
        self.head = self.tail = None
    def push(self, x):
        new_node = Node(x)
        if not self.tail: self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
    def pop(self):
        res = self.head.val
        self.head = self.head.next
        if not self.head: self.tail = None
        return res
    def peek(self):
        return self.head.val
    def is_empty(self):
        return self.head is None

class MyStack:
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()
    def push(self, x: int) -> None:
        self.q2.push(x)
        while not self.q1.is_empty():
            self.q2.push(self.q1.pop())
        self.q1, self.q2 = self.q2, self.q1
    def pop(self) -> int:
        return self.q1.pop()
    def top(self) -> int:
        return self.q1.peek()
    def empty(self) -> bool:
        return self.q1.is_empty()
