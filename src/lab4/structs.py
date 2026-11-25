from lab4.errors import EmptyError


class PQueue:
    def __init__(self):
        self._items = []

    def _sift_up(self, i):
        while i > 0:
            p = (i - 1) // 2
            if self._items[i] < self._items[p]:
                self._items[i], self._items[p] = self._items[p], self._items[i]
                i = p
            else:
                break

    def _sift_down(self, i):
        n = len(self._items)
        while True:
            left = 2 * i + 1
            right = 2 * i + 2
            mini = i

            if left < n and self._items[left] < self._items[mini]:
                mini = left
            if right < n and self._items[right] < self._items[mini]:
                mini = right
            if mini != i:
                self._items[i], self._items[mini] = self._items[mini], self._items[i]
                i = mini
            else:
                break

    def push(self, x):
        self._items.append(x)
        self._sift_up(len(self._items) - 1)

    def pop(self):
        if not self._items:
            raise EmptyError("Очередь пуста")
        if len(self._items) == 1:
            return self._items.pop()

        root = self._items[0]
        self._items[0] = self._items.pop()
        self._sift_down(0)
        return root

    def peek(self):
        if not self._items:
            raise EmptyError("Очередь пуста")
        return self._items[0]

    def __len__(self):
        return len(self._items)

    def __bool__(self):
        return bool(self._items)