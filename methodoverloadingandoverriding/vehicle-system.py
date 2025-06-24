class Vehicle:
    def calculate_rental_cost(self, days, insurance=False):
        # Base rental calculation
        base_cost = 0
        if insurance:
            base_cost += 20
        return base_cost

class Car(Vehicle):
    def calculate_rental_cost(self, days, insurance=False, luxury=False):
        # Method overloading with additional parameter
        base_cost = super().calculate_rental_cost(days, insurance)
        daily_rate = 100 if luxury else 50
        return base_cost + (days * daily_rate)

class Motorcycle(Vehicle):
    def calculate_rental_cost(self, days, insurance=False):
        # Method overriding
        base_cost = super().calculate_rental_cost(days, insurance)
        return base_cost + (days * 30)

# Testing
car = Car()
motorcycle = Motorcycle()

print(f"Car rental cost: ${car.calculate_rental_cost(3, True, luxury=True)}")  # 320
print(f"Motorcycle rental cost: ${motorcycle.calculate_rental_cost(3, True)}")  # 110