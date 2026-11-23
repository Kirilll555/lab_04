from lab4.gens import gen_dup, gen_near, gen_random, gen_reverse, gen_sorted


def test_seed():
    a1 = gen_random(10, 42)
    a2 = gen_random(10, 42)
    a3 = gen_random(10, 43)
    assert a1 == a2
    assert a1 != a3

    b1 = gen_near(10, 42)
    b2 = gen_near(10, 42)
    assert b1 == b2

    c1 = gen_dup(10, 42)
    c2 = gen_dup(10, 42)
    assert c1 == c2


def test_base():
    assert gen_sorted(3) == [0, 1, 2]
    assert gen_reverse(3) == [3, 2, 1]
    assert len(gen_random(5, 1)) == 5