class Employee:
    def calculate_pay(self, base_salary):
        return base_salary

class Manager(Employee):
    def calculate_pay(self, base_salary, bonus=0):
        # Method overloading with bonus parameter
        return super().calculate_pay(base_salary) + bonus

class Developer(Employee):
    def calculate_pay(self, base_salary):
        # Method overriding with overtime calculation
        overtime_rate = 1.5
        return super().calculate_pay(base_salary) * overtime_rate

# Testing
manager = Manager()
developer = Developer()

print(f"Manager pay: ${manager.calculate_pay(5000, 1000)}")  # 6000
print(f"Developer pay: ${developer.calculate_pay(5000)}")    # 7500