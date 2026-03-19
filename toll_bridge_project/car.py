from toll_bridge_project.vehicle import Vehicle

class Car(Vehicle):
    def calculate_fee(self):
        fee = 5.00
        if self.weight > 1590:
            excess = self.weight - 1590
            # 10p for every 100kg in excess (using floor division)
            fee += (excess // 100) * 0.10
        return round(fee, 2)