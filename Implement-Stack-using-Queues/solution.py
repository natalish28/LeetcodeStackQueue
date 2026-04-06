from collections import deque

class Queue:
    def __init__(self):
        self._data = deque()

    def push(self, x):
        self._data.append(x)

    def pop(self):
        return self._data.popleft()

    def peek(self):
        val = self._data.popleft()
        self._data.append(val)
        return val

    def is_empty(self):
        return len(self._data) == 0

    def size(self):
        return len(self._data)


class MyStack:

    def __init__(self):
        self.queue1 = Queue()
        self.queue2 = Queue()

    def push(self, x: int) -> None:
        self.queue2.push(x)
        while not self.queue1.is_empty():
            self.queue2.push(self.queue1.pop())
        self.queue1, self.queue2 = self.queue2, self.queue1

    def pop(self) -> int:
        return self.queue1.pop()

    def top(self) -> int:
        return self.queue1.peek()

    def empty(self) -> bool:
        return self.queue1.is_empty()
