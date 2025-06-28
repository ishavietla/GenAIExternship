import logging

#logging
logging.basicConfig(filename="error_log.txt",
                    level=logging.ERROR,
                    format="%(asctime)s - %(levelname)s - %(message)s")

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError as e:
            print("Invalid input! Please enter a valid number.")
            logging.error(f"ValueError occurred: {e}")

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        print("Oops! Division by zero is not allowed.")
        logging.error(f"ZeroDivisionError occurred: {e}")
        return None

def calculator():
    print("Welcome to the Error-Free Calculator!")
    while True:
        print("\nChoose an operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        choice = input("> ")

        if choice == '5':
            print("Goodbye!")
            break

        if choice in ['1', '2', '3', '4']:
            num1 = get_number("Enter the first number: ")
            num2 = get_number("Enter the second number: ")

            result = None

            try:
                if choice == '1':
                    result = add(num1, num2)
                elif choice == '2':
                    result = subtract(num1, num2)
                elif choice == '3':
                    result = multiply(num1, num2)
                elif choice == '4':
                    result = divide(num1, num2)

                if result is not None:
                    print(f"The result is: {result}")

            except Exception as e:
                print("An unexpected error occurred.")
                logging.error(f"Unexpected error: {e}")

            finally:
                print("Operation complete.")
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

# run the calculator program
if __name__ == "__main__":
    calculator()

