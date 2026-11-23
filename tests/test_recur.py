import pytest

from lab4.errors import InputError
from lab4.recur import pow_it, pow_rec


def test_pow():
    assert pow_it(2, 3) == 8
    assert pow_rec(2, 3) == 8
    assert pow_it(5, 0) == 1
    assert pow_rec(5, 0) == 1


def test_pow_err():
    with pytest.raises(InputError):
        pow_it(2, -1)
    with pytest.raises(InputError):
        pow_rec(2, -1)