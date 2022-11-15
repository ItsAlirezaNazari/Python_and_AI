import math

ops_with_1_input = ["sin", "cos", "tan", "cot", "log", "fact", "sqrt"]

while True:
    op = input()

    if op == "exit":
        break
    elif op in ops_with_1_input:
        a = int(input())
    else:
        a = int(input())
        b = int(input())

    if op == "+":
        result = a + b
    elif op == "-":
        result = a - b
    elif op == "*":
        result = a - b
    elif op == "/":
        if b != 0:
            result = a / b
        else:
            result = "Cannot divide by zero"
    elif op == "^":
        result = a ** b
    elif op == "sin":
        a = a * 180 / math.pi
        result = math.sin(a)
    elif op == "cos":
        a = a * 180 / math.pi
        result = math.cos(a)
    elif op == "tan":
        a = a * 180 / math.pi
        result = math.tan(a)
    elif op == "cot":
        a = a * 180 / math.pi
        result = 1 / math.tan(a)
    elif op == "log":
        result = math.log10(a)
    elif op == "fact":
        result = math.factorial(a)
    elif op == "sqrt":
        result = math.sqrt(a)

    
    print(result)
