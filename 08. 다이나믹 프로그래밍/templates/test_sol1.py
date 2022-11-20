from sol1 import sol1


def test_fibonacci():

    dp = {}

    assert sol1(1, 1, 1, dp) == 2
    assert sol1(2, 2, 2, dp) == 4
    assert sol1(10, 4, 6, dp) == 523
    assert sol1(50, 50, 50, dp) == 1048576
    assert sol1(-1, 7, 18, dp) == 1
