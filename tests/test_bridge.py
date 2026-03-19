import pytest
from toll_bridge_project.bridge import Bridge
from toll_bridge_project.motorbike import Motorbike

def test_bridge_weight_limit():
    b = Bridge()
    # Adding a very heavy vehicle
    heavy_truck = Motorbike("TANK", 30001) 
    assert b.add_vehicle(heavy_truck) is False

def test_bridge_capacity():
    b = Bridge()
    for i in range(20):
        b.add_vehicle(Motorbike(f"M{i}", 100))
    # 21st vehicle should fail
    assert b.add_vehicle(Motorbike("M21", 100)) is False