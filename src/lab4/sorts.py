def selection(a):
    res = a[:]
    n = len(res)

    for i in range(n):
        min_i = i
        for j in range(i + 1, n):
            if res[j] < res[min_i]:
                min_i = j
        res[i], res[min_i] = res[min_i], res[i]

    return res


def heap(a, n, i):
    x = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and a[left] > a[x]:
        x = left
    if right < n and a[right] > a[x]:
        x = right
    if x != i:
        a[i], a[x] = a[x], a[i]
        heap(a, n, x)


def heap_sort(a):
    res = a[:]
    n = len(res)

    for i in range(n // 2 - 1, -1, -1):
        heap(res, n, i)

    for i in range(n - 1, 0, -1):
        res[i], res[0] = res[0], res[i]
        heap(res, i, 0)

    return res
