class Node:
    def __init__(self, x):
        self.val = x
        self.next = None

class Stack:
    def __init__(self):
        self.top_node = None
    def push(self, x):
        new_node = Node(x)
        new_node.next = self.top_node
        self.top_node = new_node
    def pop(self):
        res = self.top_node.val
        self.top_node = self.top_node.next
        return res
    def peek(self):
        return self.top_node.val
    def is_empty(self):
        return self.top_node is None

class MyQueue:
    def __init__(self):
        self.stack_in = Stack()
        self.stack_out = Stack()
    def push(self, x: int) -> None:
        self.stack_in.push(x)
    def pop(self) -> int:
        self.peek()
        return self.stack_out.pop()
    def peek(self) -> int:
        if self.stack_out.is_empty():
            while not self.stack_in.is_empty():
                self.stack_out.push(self.stack_in.pop())
        return self.stack_out.peek()
    def empty(self) -> bool:
        return self.stack_in.is_empty() and self.stack_out.is_empty()
