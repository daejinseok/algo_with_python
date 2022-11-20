from sol2 import sol2


def test_fibonacci():

    assert sol2(1, 1, 1) == 2
    assert sol2(2, 2, 2) == 4
    assert sol2(10, 4, 6) == 523
    assert sol2(50, 50, 50) == 1048576
    assert sol2(-1, 7, 18) == 1
