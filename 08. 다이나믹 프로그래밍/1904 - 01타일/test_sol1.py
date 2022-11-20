from sol1 import sol1


def test_sol1():

    assert sol1(1) == 1
    assert sol1(2) == 2
    assert sol1(3) == 3
    assert sol1(4) == 5
    assert sol1(5) == 8
    assert sol1(6) == 13
    assert sol1(7) == 21
    assert sol1(29) == (832040 % 15746)
