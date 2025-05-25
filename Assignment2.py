class PositiveNumberError(Exception):
    pass

def check_number(num):
    if num <= 0:
        raise PositiveNumberError("Number must be positive!")

# Test it
try:
    number = int(input("Enter a number: "))
    check_number(number)
    print("Good! The number is positive")
except PositiveNumberError as e:
    print(e)