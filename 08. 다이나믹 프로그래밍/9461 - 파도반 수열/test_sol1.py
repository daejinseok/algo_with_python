from sol1 import sol1


def test_sol1():
    assert sol1(1) == 1
    assert sol1(2) == 1
    assert sol1(3) == 1
    assert sol1(4) == 2
    assert sol1(5) == 2
    assert sol1(6) == 3
    assert sol1(7) == 4
    assert sol1(8) == 5
    assert sol1(9) == 7
    assert sol1(10) == 9
    assert sol1(12) == 16
