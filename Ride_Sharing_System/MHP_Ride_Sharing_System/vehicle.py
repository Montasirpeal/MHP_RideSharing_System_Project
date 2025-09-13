from abc import ABC


class Vehicle(ABC):
    def __init__(self, vehicle_type, license_plate, rate_per_km):
        self.vehicle_id = id(self)
        self.vehicle_type = vehicle_type
        self.license_plate = license_plate
        self.rate_per_km = rate_per_km

    def __str__(self):
        return f"{self.vehicle_type} ({self.license_plate}) - {self.rate_per_km}/km"


class Car(Vehicle):
    def __init__(self, license_plate, rate_per_km):
        super().__init__("Car", license_plate, rate_per_km)


class Bike(Vehicle):
    def __init__(self, license_plate, rate_per_km):
        super().__init__("Bike", license_plate, rate_per_km)


class CNG(Vehicle):
    def __init__(self, license_plate, rate_per_km):
        super().__init__("CNG", license_plate, rate_per_km)


class Truck(Vehicle):
    def __init__(self, license_plate, rate_per_km):
        super().__init__("Truck", license_plate, rate_per_km)
