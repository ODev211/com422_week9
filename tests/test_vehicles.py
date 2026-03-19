from toll_bridge_project.car import Car
from toll_bridge_project.lorry import Lorry

def test_car_fees():
    assert Car("C1", 1500).calculate_fee() == 5.00    # Base
    assert Car("C2", 1690).calculate_fee() == 5.10    # 100kg over
    assert Car("C3", 1789).calculate_fee() == 5.10 # Not quite 200kg over

def test_lorry_fees():
    assert Lorry("L1", 7000).calculate_fee() == 10.00
    assert Lorry("L2", 8001).calculate_fee() == 15.00