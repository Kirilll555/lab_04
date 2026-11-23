import random


def gen_random(n, seed):
    random.seed(seed)
    return [random.randint(-100, 100) for _ in range(n)]


def gen_sorted(n):
    return list(range(n))


def gen_reverse(n):
    return list(range(n, 0, -1))


def gen_near(n, seed):
    arr = list(range(n))
    if n < 2:
        return arr

    random.seed(seed)
    for _ in range(max(1, n // 10)):
        i = random.randint(0, n - 2)
        arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return arr


def gen_dup(n, seed):
    random.seed(seed)
    return [random.choice([1, 2, 3]) for _ in range(n)]