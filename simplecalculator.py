def add(x, y):
    z = x + y
    return z

def subtract(x, y):
    z = x - y
    return z

def multiply(x, y):
    z = x * y
    return z

def divide(x, y):
    if y == 0:
        return "Error: Cannot divide by zero."
    else:
        return x / y

def main():
    print("Welcome to the Simple Calculator!")
    choice = input("Choose an operation:\n1. Add\n2. Subtract\n3. Multiply\n4. Divide\n")

    x = int(input("Enter first number:\n"))
    y = int(input("Enter second number:\n"))
    
    if choice == '1':
        print("Result:", add(x, y))
    elif choice == '2':
        print("Result:", subtract(x, y))
    elif choice == '3':
        print("Result:", multiply(x, y))
    elif choice == '4':
        print("Result:", divide(x, y))
    else:
        print("Invalid choice.")

main()