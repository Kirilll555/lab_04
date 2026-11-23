import heapq

from lab4.errors import EmptyError


class PQueue:
    def __init__(self):
        self._items = []

    def push(self, x):
        heapq.heappush(self._items, x)

    def pop(self):
        if not self._items:
            raise EmptyError("Очередь пуста")
        return heapq.heappop(self._items)

    def peek(self):
        if not self._items:
            raise EmptyError("Очередь пуста")
        return self._items[0]

    def __len__(self):
        return len(self._items)

    def __bool__(self):
        return bool(self._items)