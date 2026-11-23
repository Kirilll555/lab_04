from lab4.errors import InputError


def pow_it(x, n):
    if n < 0:
        raise InputError("Степень не может быть отрицательной")

    res = 1
    while n > 0:
        if n % 2 == 1:
            res *= x
        x *= x
        n //= 2
    return res


def pow_rec(x, n):
    if n < 0:
        raise InputError("Степень не может быть отрицательной")
    if n == 0:
        return 1
    if n % 2 == 0:
        res = pow_rec(x, n // 2)
        return res * res
    return x * pow_rec(x, n - 1)