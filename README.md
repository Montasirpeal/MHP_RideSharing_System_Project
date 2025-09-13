# MHP_RideSharing_System_Project

🔎 Project Overview

MHP Ride Sharing System is a simple Python project built using Object-Oriented Programming (OOP) concepts.
It simulates a basic ride-sharing platform (like Uber, Pathao, Shohoz) where Riders can request rides and Drivers can accept them. The project demonstrates real-life ride management in a simplified way.

⚙️ Features

User Management

Separate classes for Riders and Drivers (inherited from an abstract User class).

Each user has profile info, email, NID, location, and wallet balance.

Rider Functionalities

View profile and wallet balance.

Load money into wallet.

Request rides with specific vehicle type (Car, Bike, CNG, Truck).

Track current ride details.

Driver Functionalities

View profile.

Accept and complete rides.

Earn fare directly into wallet after completing rides.

Vehicle Management

Vehicle classes: Car, Bike, CNG, Truck.

Each vehicle has a license plate and rate per km.

Ride Management

Rider requests create Ride objects.

Matching system assigns the nearest driver (simplified: first available driver).

Start and end time recorded.

Fare calculated based on distance & vehicle type.

Wallets updated automatically.

RideSharing Platform

Keeps track of all riders, drivers, and completed rides.

Can show summary at any point.

🛠️ Technologies Used

Language: Python 3

Concepts: OOP (Abstraction, Inheritance, Polymorphism, Encapsulation)

Modules: abc, datetime

▶️ Demo Flow

A Rider (Rahim) registers with initial balance.

A Driver (Kolim) registers with location.

Rahim requests a ride to Uttara with a Car.

System assigns Kolim as the driver.

Ride starts → ends → wallets update.

Summary and profiles printed.


▶️Example Output (Simplified) 


RideSharing Company: MHP RIDE, Drivers: 1, Riders: 1, Rides: 0
✅ Ride confirmed!
Ride from Mohammadpur to Uttara, Driver: Kolim, Rider: Rahim, Fare: 100
🚖 Kolim has accepted the ride.
✅ Kolim has completed the ride.
RideSharing Company: MHP RIDE, Drivers: 1, Riders: 1, Rides: 1

Rider Profile:
Name: Rahim
Wallet Balance: 1100

Driver Profile:
Name: Kolim
Wallet Balance: 100
