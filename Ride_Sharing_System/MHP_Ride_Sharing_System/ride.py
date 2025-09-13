from datetime import datetime
from vehicle import Car, Bike, CNG, Truck


class RideSharing:
    def __init__(self, company_name):
        self.company_name = company_name
        self.rides = []
        self.drivers = []
        self.riders = []

    def add_driver(self, driver):
        self.drivers.append(driver)

    def add_rider(self, rider):
        self.riders.append(rider)

    def __str__(self):
        return (f"RideSharing Company: {self.company_name}, "
                f"Drivers: {len(self.drivers)}, Riders: {len(self.riders)}, Rides: {len(self.rides)}")


class Ride:
    def __init__(self, start_location, end_location, vehicle):
        self.start_location = start_location
        self.end_location = end_location
        self.vehicle = vehicle
        self.driver = None
        self.rider = None
        self.start_time = None
        self.end_time = None
        self.estimated_fare = self.calculate_fare(vehicle)

    def set_driver(self, driver):
        self.driver = driver

    def set_rider(self, rider):
        self.rider = rider

    def start_ride(self):
        self.start_time = datetime.now()

    def end_ride(self):
        self.end_time = datetime.now()
        if self.rider and self.driver:
            self.rider.wallet -= self.estimated_fare
            self.driver.wallet += self.estimated_fare

    def calculate_fare(self, vehicle):
        distance = 10  # Fixed distance for simplicity
        fare_per_km = {
            "Car": 10,
            "Bike": 5,
            "CNG": 8,
            "Truck": 15
        }
        return distance * fare_per_km.get(vehicle.vehicle_type, 10)

    def __repr__(self):
        return (f"Ride from {self.start_location} to {self.end_location}, "
                f"Driver: {self.driver.name if self.driver else 'None'}, "
                f"Rider: {self.rider.name if self.rider else 'None'}, "
                f"Start: {self.start_time}, End: {self.end_time}, Fare: {self.estimated_fare}")


class RideRequest:
    def __init__(self, rider, end_location):
        self.rider = rider
        self.start_location = rider.current_location
        self.end_location = end_location


class RideMatching:
    def __init__(self, drivers):
        self.available_drivers = drivers

    def find_nearest_driver(self, rider_request, vehicle_type):
        if not self.available_drivers:
            return None

        driver = self.available_drivers[0]

        # Choose vehicle
        if vehicle_type == "Car":
            vehicle = Car("ABC45", 30)
        elif vehicle_type == "Bike":
            vehicle = Bike("XYZ12", 15)
        elif vehicle_type == "CNG":
            vehicle = CNG("CNG99", 20)
        else:
            vehicle = Truck("TRK77", 50)

        ride = Ride(rider_request.start_location, rider_request.end_location, vehicle)
        ride.set_rider(rider_request.rider)
        driver.accept_ride(ride)
        return ride
