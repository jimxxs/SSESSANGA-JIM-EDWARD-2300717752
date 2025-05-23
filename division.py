while True:
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        result = num1 / num2
        print(f"Result: {num1} / {num2} = {result}")
        break  # Exit loop if successful
        
    except ValueError:
        print("Error: Please enter valid numbers")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    
    print("Please try again...\n")