import fibo_topdown as td
import fibo_bottomup as bt

def test_td():
    assert td.fibo(3) == 2
    assert td.fibo(4) == 3
    assert td.fibo(99) == 218922995834555169026

def test_bt():
    assert bt.fibo(3) == 2
    assert bt.fibo(4) == 3
    assert bt.fibo(99) == 218922995834555169026    

