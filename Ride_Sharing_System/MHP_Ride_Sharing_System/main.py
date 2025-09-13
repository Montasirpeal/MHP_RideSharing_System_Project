from ride import RideSharing
from users import Rider, Driver  # Ensure user.py exists in the same directory as main.py

# Create RideSharing company
MHPRIDE = RideSharing("MHP RIDE")

# Register Rider
rahim = Rider("Rahim", "rahim@gmail.com", 1234, "Mohammadpur", 1200)
MHPRIDE.add_rider(rahim)
print(MHPRIDE)

# Register Driver
kolim = Driver("Kolim", "kolim@gmail.com", 5678, "Dhanmondi")
MHPRIDE.add_driver(kolim)

# Rider requests a ride
rahim.request_ride(MHPRIDE, "Uttara", "Car")
rahim.show_current_ride()

# Complete the ride
if rahim.current_ride:
    rahim.current_ride.start_ride()
    rahim.current_ride.end_ride()
    rahim.show_current_ride()
    kolim.reach_destination(rahim.current_ride)

print(MHPRIDE)

# Show profiles after ride
rahim.display_profile()
kolim.display_profile()

