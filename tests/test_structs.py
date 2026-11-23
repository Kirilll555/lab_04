import pytest

from lab4.errors import EmptyError
from lab4.structs import PQueue


def test_pq():
    q = PQueue()
    assert len(q) == 0
    assert not q

    q.push(3)
    q.push(1)
    q.push(2)

    assert len(q) == 3
    assert q

    assert q.peek() == 1
    assert q.pop() == 1
    assert q.pop() == 2
    assert q.pop() == 3


def test_pq_empty():
    q = PQueue()
    with pytest.raises(EmptyError):
        q.pop()
    with pytest.raises(EmptyError):
        q.peek()


def test_pq_invar():
    q = PQueue()
    for x in [5, 1, 3, 3, 2, 4, 0]:
        q.push(x)
    out = [q.pop() for _ in range(7)]
    assert out == sorted(out)
    with pytest.raises(EmptyError):
        q.pop()