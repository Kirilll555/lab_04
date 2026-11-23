import time

from lab4.gens import gen_random, gen_reverse
from lab4.sorts import heap_sort, selection


def measure(func, arr):
    times = []
    for _ in range(5):
        cp = arr[:]
        t0 = time.perf_counter()
        func(cp)
        t1 = time.perf_counter()
        times.append(t1 - t0)
    return sum(times) / 5


def bench():
    sizes = [100_000, 1_000_000, 10_000_000]
    print("| Size | Type | Selection | Heap |")
    print("| ---- | ---- | --------- | ---- |")

    for size in sizes:
        rand = gen_random(size, 42)
        rev = gen_reverse(size)

        if size <= 100_000:
            t_rand = f"{measure(selection, rand):.5f}"
            t_rev = f"{measure(selection, rev):.5f}"
        else:
            t_rand = "-"
            t_rev = "-"

        t_heap_rand = measure(heap_sort, rand)
        t_heap_rev = measure(heap_sort, rev)

        print(f"| {size} | Random | {t_rand} | {t_heap_rand:.5f} |")
        print(f"| {size} | Reverse | {t_rev} | {t_heap_rev:.5f} |")