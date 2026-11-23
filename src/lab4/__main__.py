from lab4.bench import bench
from lab4.recur import pow_it, pow_rec
from lab4.sorts import heap_sort, selection
from lab4.structs import PQueue


def main():
    print("Быстрая степень 2^10:", pow_it(2, 10))
    print("Быстрая степень 2^10:", pow_rec(2, 10))

    arr = [5, 2, 8, 1]
    print("Дано:", arr)
    print("Selection:", selection(arr))
    print("Heap:", heap_sort(arr))

    q = PQueue()
    q.push(10)
    q.push(5)
    print("Приоритетная очередь:", q.pop())

    print("\nЗапуск:")
    bench()


if __name__ == '__main__':
    main()