import operator
import sys

ops = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
}

def calculate(a, op, b):
    if op not in ops:
        raise ValueError(f"Unsupported operator: {op}")
    return ops[op](a, b)

def main(args):
    if len(args) != 3:
        print("Usage: python calculator.py <a> <op> <b>")
        return 1
    a = float(args[0])
    op = args[1]
    b = float(args[2])
    try:
        result = calculate(a, op, b)
    except ZeroDivisionError:
        print("Error: Division by zero")
        return 1
    except ValueError as e:
        print(e)
        return 1
    print(result)
    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
