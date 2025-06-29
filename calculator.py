import operator
import sys
import tkinter as tk

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

class CalculatorGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Calculator")

        tk.Label(self.root, text="A").grid(row=0, column=0, padx=5, pady=5)
        self.entry_a = tk.Entry(self.root)
        self.entry_a.grid(row=0, column=1, padx=5, pady=5)

        self.op_var = tk.StringVar(value='+')
        tk.OptionMenu(self.root, self.op_var, '+', '-', '*', '/').grid(row=0, column=2, padx=5, pady=5)

        tk.Label(self.root, text="B").grid(row=0, column=3, padx=5, pady=5)
        self.entry_b = tk.Entry(self.root)
        self.entry_b.grid(row=0, column=4, padx=5, pady=5)

        tk.Button(self.root, text="=", command=self.calculate).grid(row=0, column=5, padx=5, pady=5)
        self.result_var = tk.StringVar()
        tk.Label(self.root, textvariable=self.result_var).grid(row=0, column=6, padx=5, pady=5)

    def calculate(self):
        try:
            a = float(self.entry_a.get())
            b = float(self.entry_b.get())
            op = self.op_var.get()
            result = calculate(a, op, b)
        except Exception as e:
            self.result_var.set(f"Error: {e}")
        else:
            self.result_var.set(str(result))

    def run(self):
        self.root.mainloop()

def main(args):
    if len(args) == 3:
        a = float(args[0])
        op = args[1]
        b = float(args[2])
        try:
            result = calculate(a, op, b)
        except Exception as e:
            print(f"Error: {e}")
            return 1
        print(result)
        return 0
    else:
        gui = CalculatorGUI()
        gui.run()
        return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
