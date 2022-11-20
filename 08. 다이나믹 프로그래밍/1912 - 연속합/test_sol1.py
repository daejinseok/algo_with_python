from sol1 import sol1


def test_fibonacci():

    assert sol1([10, -4, 3, 1, 5, 6, -35, 12, 21, -1], 10) == 33
    assert sol1([2, 1, -4, 3, 4, -4, 6, 5, -5, 1], 10) == 14
    assert sol1([-1, -2, -3, -4, -5], 5) == -1
