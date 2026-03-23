from tkinter import *


def button_click(number):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(current) + str(number))


def button_clear():
    entry.delete(0, END)


def button_backspace():
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, current[:-1])


def button_add():
    global first_num, math_op
    first_num = float(entry.get() or 0)
    math_op = "add"
    entry.delete(0, END)


def button_subtract():
    global first_num, math_op
    first_num = float(entry.get() or 0)
    math_op = "subtract"
    entry.delete(0, END)


def button_multiply():
    global first_num, math_op
    first_num = float(entry.get() or 0)
    math_op = "multiply"
    entry.delete(0, END)


def button_divide():
    global first_num, math_op
    first_num = float(entry.get() or 0)
    math_op = "divide"
    entry.delete(0, END)


def button_equals():
    try:
        second_num = float(entry.get())
    except ValueError:
        entry.delete(0, END)
        entry.insert(0, "Error")
        return

    entry.delete(0, END)

    if math_op == "add":
        entry.insert(0, first_num + second_num)
    elif math_op == "subtract":
        entry.insert(0, first_num - second_num)
    elif math_op == "multiply":
        entry.insert(0, first_num * second_num)
    elif math_op == "divide":
        if second_num != 0:
            entry.insert(0, first_num / second_num)
        else:
            entry.insert(0, "Error")


def button_plus_minus():
    current = entry.get()
    if not current:
        return
    if current.startswith("-"):
        entry.delete(0, END)
        entry.insert(0, current[1:])
    else:
        entry.delete(0, END)
        entry.insert(0, "-" + current)


def button_action(action):
    if action == "C":
        button_clear()
    elif action == "<-":
        button_backspace()
    elif action == "±":
        button_plus_minus()
    elif action == "=":
        button_equals()
    elif action == "+":
        button_add()
    elif action == "-":
        button_subtract()
    elif action == "*":
        button_multiply()
    elif action == "/":
        button_divide()


root = Tk()
root.title("Adhiraj's Calculator - MIT-WPU Demo")
root.geometry("300x400")
root.resizable(False, False)

entry = Entry(root, width=16, font=("Arial", 16), bd=5, justify=RIGHT)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = [
    ("C", 1, 0), ("±", 1, 1), ("<-", 1, 2), ("/", 1, 3),
    ("7", 2, 0), ("8", 2, 1), ("9", 2, 2), ("*", 2, 3),
    ("4", 3, 0), ("5", 3, 1), ("6", 3, 2), ("-", 3, 3),
    ("1", 4, 0), ("2", 4, 1), ("3", 4, 2), ("+", 4, 3),
    ("0", 5, 0), (".", 5, 1), ("=", 5, 2, 2),
]

for item in buttons:
    text = item[0]
    row = item[1]
    col = item[2]
    colspan = item[3] if len(item) > 3 else 1

    if text in ["C", "<-", "±", "/", "*", "-", "+", "="]:
        btn = Button(
            root,
            text=text,
            width=11 if colspan > 1 else 5,
            height=2,
            font=("Arial", 14),
            bd=5,
            bg="orange" if text == "=" else "lightgray",
            command=lambda t=text: button_action(t),
        )
    else:
        btn = Button(
            root,
            text=text,
            width=5,
            height=2,
            font=("Arial", 14),
            bd=5,
            command=lambda t=text: button_click(t),
        )

    btn.grid(row=row, column=col, columnspan=colspan, padx=3, pady=3)

root.mainloop()
