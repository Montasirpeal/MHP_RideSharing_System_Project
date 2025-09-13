from abc import ABC, abstractmethod
from ride import RideRequest, RideMatching


class User(ABC):
    def __init__(self, name, email, nid):
        self.name = name
        self.email = email
        self.nid = nid
        self.wallet = 0

    @abstractmethod
    def display_profile(self):
        raise NotImplementedError("Subclasses must implement this method")


class Rider(User):
    def __init__(self, name, email, nid, current_location, initial_balance):
        super().__init__(name, email, nid)
        self.current_location = current_location
        self.wallet = initial_balance
        self.current_ride = None

    def display_profile(self):
        print(f"Rider Profile:\n"
              f"Name: {self.name}\nEmail: {self.email}\nNID: {self.nid}\n"
              f"Current Location: {self.current_location}\nWallet Balance: {self.wallet}")

    def load_cash(self, amount):
        if amount > 0:
            self.wallet += amount
        else:
            print("Invalid amount. Please enter a positive value.")

    def update_location(self, current_location):
        self.current_location = current_location

    def request_ride(self, ride_sharing, destination, vehicle_type):
        ride_request = RideRequest(self, destination)
        ride_matching = RideMatching(ride_sharing.drivers)
        ride = ride_matching.find_nearest_driver(ride_request, vehicle_type)
        if ride:
            self.current_ride = ride
            ride_sharing.rides.append(ride)
            print("✅ Ride confirmed!")
        else:
            print("❌ No drivers available.")

    def show_current_ride(self):
        print(self.current_ride)


class Driver(User):
    def __init__(self, name, email, nid, current_location):
        super().__init__(name, email, nid)
        self.current_location = current_location
        self.wallet = 0

    def display_profile(self):
        print(f"Driver Profile:\n"
              f"Name: {self.name}\nEmail: {self.email}\nNID: {self.nid}\n"
              f"Current Location: {self.current_location}\nWallet Balance: {self.wallet}")

    def accept_ride(self, ride):
        ride.set_driver(self)
        print(f"🚖 {self.name} has accepted the ride.")

    def reach_destination(self, ride):
        ride.end_ride()
        print(f"✅ {self.name} has completed the ride.")
