
def multiply_numbers(x, y):
    return x * y
    
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
sol = input("Enter add or sub , mul or div: ")


elif operation == 'mul':
    result = multiply_numbers(num1, num2)
    print(f"The product of {num1} and {num2} is: {result}")

def add_numbers(x, y):
    return x + y

def subtract_numbers(x, y):
    return x - y

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

operation = input("Enter 'add' for addition or 'sub' for subtraction: ")

if operation == 'add':
    result = add_numbers(num1, num2)
    print(f"The sum of {num1} and {num2} is: {result}")
elif operation == 'sub':
    result = subtract_numbers(num1, num2)
    print(f"The difference between {num1} and {num2} is: {result}")
else:
    print("Invalid operation. Please enter 'add' or 'sub'.")

