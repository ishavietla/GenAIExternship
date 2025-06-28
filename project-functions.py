# Recursive Artistry Program
# Showcases recursion: factorial, Fibonacci, and fractal drawing.

import turtle

# Recursive factorial function
def factorial(n):
    """Recursively computes factorial of n."""
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Recursive Fibonacci function
def fibonacci(n):
    """Recursively computes nth Fibonacci number."""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

# Recursive fractal tree drawing using turtle
def draw_fractal_tree(branch_length, t):
    """Draws a recursive fractal tree."""
    if branch_length > 5:
        t.forward(branch_length)
        t.right(20)
        draw_fractal_tree(branch_length - 15, t)
        t.left(40)
        draw_fractal_tree(branch_length - 15, t)
        t.right(20)
        t.backward(branch_length)

# Input validation for positive integers
def get_positive_integer(prompt):
    """Prompts user for positive integer input."""
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                print("Please enter a positive integer.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

# Main menu loop
def main():
    print("Welcome to the Recursive Artistry Program!")
    while True:
        print("\nChoose an option:")
        print("1. Calculate Factorial")
        print("2. Find Fibonacci")
        print("3. Draw a Recursive Fractal")
        print("4. Exit")
        choice = input("> ")

        if choice == '1':
            number = get_positive_integer("Enter a number to find its factorial: ")
            result = factorial(number)
            print(f"The factorial of {number} is {result}.")
        elif choice == '2':
            position = get_positive_integer("Enter the position of the Fibonacci number: ")
            result = fibonacci(position)
            print(f"The {position}th Fibonacci number is {result}.")
        elif choice == '3':
            print("Drawing a fractal tree... Close the window to return to the menu.")
            t = turtle.Turtle()
            screen = turtle.Screen()
            t.left(90)  # Point upwards
            t.color("green")
            t.speed("fastest")
            draw_fractal_tree(100, t)
            screen.exitonclick()
        elif choice == '4':
            print("Thank you for exploring recursion! Goodbye.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

# Run the program
if __name__ == "__main__":
    main()
