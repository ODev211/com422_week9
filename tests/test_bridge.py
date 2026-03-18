from toll_bridge_project import bridge_system
import pytest

# First test for motorbike
def test_motorbike_fee():
    motorbike = bridge_system.Motorbike("ABC123", 100)
    assert motorbike.calculate_fee() == 3.00

# Car test
def test_car_fee():
    car = bridge_system.Car("DEF456", 2000)
    assert car.calculate_fee() == 5.00