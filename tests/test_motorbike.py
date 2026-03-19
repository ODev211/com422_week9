from toll_bridge_project.motorbike import Motorbike

def test_motorbike_fee():
    m = Motorbike("MOTO1", 250)
    assert m.calculate_fee() == 3.00