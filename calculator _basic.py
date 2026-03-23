def add(x, y): return x + y 
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y):
    if y == 0: return "Error: Divide by zero!"
    return x / y

print("Calculator: +,-,*, / (type 'quit' to exit)")
while True:
    user_input = input("Enter e.g., 10 + 5: ").strip().split()
    if user_input[0].lower() == 'quit': break
    if len(user_input) != 3: print("Format: num1 op num2"); continue
    num1, op, num2 = float(user_input[0]), user_input[1], float(user_input[2])

    if op == '+': print(f"Result: {add(num1, num2)}")
    elif op == '-': print(f"Result: {subtract(num1, num2)}")
    elif op == '*': print(f"Result: {multiply(num1, num2)}")
    elif op == '/': print(f"Result: {divide(num1, num2)}")
    else: print("Invalid operator")