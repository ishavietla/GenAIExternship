#comment other two tasks to test each task individually
# Task 1 - Understanding Python Exceptions

def divide_100_by_user_input():
    while True:
        try:
            num = float(input("Enter a number: "))
            result = 100 / num
        except ZeroDivisionError:
            print("Oops! You cannot divide by zero.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")
        else:
            print(f"100 divided by {num} is {result}.")
            break

 divide_100_by_user_input()


# Task 2 - Types of Exceptions

def demonstrate_exceptions():
    # 1. IndexError example
    try:
        my_list = [1, 2, 3]
        
        print(my_list[5])
    except IndexError:
        print("IndexError occurred! List index out of range.")

    # 2. KeyError example
    try:
        my_dict = {"name": "Alice", "age": 30}
        print(my_dict["gender"])
    except KeyError:
        print("KeyError occurred! Key not found in the dictionary.")

    # 3. TypeError example
    try:
        result = "Age: " + 25
    except TypeError:
        print("TypeError occurred! Unsupported operand types.")

 demonstrate_exceptions()


# Task 3 - Using try...except...else...finally

def divide_two_numbers():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = num1 / num2
    except ZeroDivisionError:
        print("Cannot divide by zero.")
    except ValueError:
        print("Invalid input! Please enter numbers.")
    else:
        print(f"The result is {result}.")
    finally:
        print("This block always executes.")

divide_two_numbers()
