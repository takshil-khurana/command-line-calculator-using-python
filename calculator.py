# calculator.py

# Step 1: Define functions for operations
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero."
    return a / b

# Step 2: Display menu and take user input in a loop
def main():
    while True:
        print("\n--- Simple Calculator ---")
        print("Select operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")

        if choice == '5':
            print("Exiting calculator. Goodbye!")
            break

        # Validate choice
        if choice not in ['1', '2', '3', '4']:
            print("Invalid choice. Please select a valid option.")
            continue

        # Step 3: Get numbers from user
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue

        # Step 4: Perform calculation
        if choice == '1':
            result = add(num1, num2)
        elif choice == '2':
            result = subtract(num1, num2)
        elif choice == '3':
            result = multiply(num1, num2)
        elif choice == '4':
            result = divide(num1, num2)

        print("Result:", result)

# Step 5: Run the main loop
if __name__ == "__main__":
    main()
