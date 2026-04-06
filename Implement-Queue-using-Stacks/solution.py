from collections import deque

class Stack:
    def __init__(self):
        self._data = deque()

    def push(self, x):
        self._data.append(x)

    def pop(self):
        return self._data.pop()

    def peek(self):
        val = self._data.pop()
        self._data.append(val)
        return val

    def is_empty(self):
        return len(self._data) == 0

    def size(self):
        return len(self._data)



class MyQueue:

    def __init__(self):
        self.stack_in = Stack() 
        self.stack_out = Stack() 

    def push(self, x: int) -> None:
        self.stack_in.push(x)

    def _transfer(self):
        if self.stack_out.is_empty():
            while not self.stack_in.is_empty():
                self.stack_out.push(self.stack_in.pop())

    def pop(self) -> int:
        self._transfer()
        return self.stack_out.pop()

    def peek(self) -> int:
        self._transfer()
        return self.stack_out.peek()

    def empty(self) -> bool:
        return self.stack_in.is_empty() and self.stack_out.is_empty()
