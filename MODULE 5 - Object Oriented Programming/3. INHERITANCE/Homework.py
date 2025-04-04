class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def display_info(self):
        return f"Vehicle: {self.year} {self.make} {self.model}"
class Bus(Vehicle):
    def __init__(self, make, model, year, num_passengers, fare_per_passenger):
        super().__init__(make, model, year)
        self.num_passengers = num_passengers
        self.fare_per_passenger = fare_per_passenger

    def calculate_fare(self):
        return self.num_passengers * self.fare_per_passenger
    def display_info(self):
        vehicle_info = super().display_info()
        return f"{vehicle_info}\nNumber of passengers: {self.num_passengers}\nFare per passenger: ${self.fare_per_passenger}"
bus = Bus("Mercedes", "Sprinter", 2022, 20, 2.50)
print(bus.display_info())
total_fare = bus.calculate_fare()
print(f"Total fare collected: ${total_fare:.2f}")