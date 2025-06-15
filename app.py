# Simple Calculator in Python

def add(x, y):
    return x + y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Cannot divide by zero!"
    return x / y

print("Simple Calculator")
print("Select operation:")
print("1. Add")

print("2. Multiply")
print("3. Divide")

choice = input("Enter choice (1/2/3): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == '1':
    print("Result:", add(num1, num2))
elif choice == '2':
    print("Result:", multiply(num1, num2))
elif choice == '3':
    print("Result:", divide(num1, num2))
else:
    print("Invalid choice.")
