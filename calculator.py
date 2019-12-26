# 计算器GUI

import tkinter as tk
import tkinter.messagebox as mb

number = 0
number_list = list()
calculate_number = list()
method = []

root = tk.Tk() # 窗口

# 建立GUI的名称
root.title("计算器")

# 设定GUI的大小
root.geometry("800x600")

# 建立frame
frame_display = tk.Frame() # 显示区域frame
frame_display.pack()

frame_number_row1 = tk.Frame() # 数字区域frame
frame_number_row1.pack()
frame_number_row2 = tk.Frame() # 数字区域frame
frame_number_row2.pack()
frame_number_row3 = tk.Frame() # 数字区域frame
frame_number_row3.pack()

frame = tk.Frame(root) # 计算区域Frame
frame.pack()

# 数字按键函数
def zero():
    global number
    number = 0
    number_list.append(number)
    reverse_number_list = list(reversed(number_list))
    multi = 1
    display_number = 0
    for i in reverse_number_list:
        display_number = multi * i + display_number
        multi = multi*10
    v.set(display_number)

def one():
    global number
    number = 1
    number_list.append(number)
    reverse_number_list = list(reversed(number_list))
    multi = 1
    display_number = 0
    for i in reverse_number_list:
        display_number = multi * i + display_number
        multi = multi*10
    v.set(display_number)

def two():
    global number
    number = 2
    number_list.append(number)
    reverse_number_list = list(reversed(number_list))
    multi = 1
    display_number = 0
    for i in reverse_number_list:
        display_number = multi * i + display_number
        multi = multi*10
    v.set(display_number)

def three():
    global number
    number = 3
    number_list.append(number)
    reverse_number_list = list(reversed(number_list))
    multi = 1
    display_number = 0
    for i in reverse_number_list:
        display_number = multi * i + display_number
        multi = multi*10
    v.set(display_number)

def four():
    global number
    number = 4
    number_list.append(number)
    reverse_number_list = list(reversed(number_list))
    multi = 1
    display_number = 0
    for i in reverse_number_list:
        display_number = multi * i + display_number
        multi = multi*10
    v.set(display_number)

def five():
    global number
    number = 5
    number_list.append(number)
    reverse_number_list = list(reversed(number_list))
    multi = 1
    display_number = 0
    for i in reverse_number_list:
        display_number = multi * i + display_number
        multi = multi*10
    v.set(display_number)

def six():
    global number
    number = 6
    number_list.append(number)
    reverse_number_list = list(reversed(number_list))
    multi = 1
    display_number = 0
    for i in reverse_number_list:
        display_number = multi * i + display_number
        multi = multi*10
    v.set(display_number)

def seven():
    global number
    number = 7
    number_list.append(number)
    reverse_number_list = list(reversed(number_list))
    multi = 1
    display_number = 0
    for i in reverse_number_list:
        display_number = multi * i + display_number
        multi = multi*10
    v.set(display_number)

def eight():
    global number
    number = 8
    number_list.append(number)
    reverse_number_list = list(reversed(number_list))
    multi = 1
    display_number = 0
    for i in reverse_number_list:
        display_number = multi * i + display_number
        multi = multi*10
    v.set(display_number)

def nine():
    global number
    number = 9
    number_list.append(number)
    reverse_number_list = list(reversed(number_list))
    multi = 1
    display_number = 0
    for i in reverse_number_list:
        display_number = multi * i + display_number
        multi = multi*10
    v.set(display_number)

# 运算函数
def mul():
    # global calculate_number
    calculate_number.clear()
    calculate_number.append(number)
    method.clear()
    method.append("mul")

def div():
    calculate_number.clear()
    calculate_number.append(number)
    method.clear()
    method.append("div")

def sub():
    calculate_number.clear()
    calculate_number.append(number)
    method.clear()
    method.append("sub")

def add():
    calculate_number.clear()
    calculate_number.append(number)
    method.clear()
    method.append("add")

# 计算按键函数
def calculate():
    # mb.showinfo(title="消息", message="请查看结果")
    if method[0] == "mul":
        result = calculate_number[0] * number
    if method[0] == "sub":
        result = calculate_number[0] - number
    if method[0] == "add":
        result = calculate_number[0] + number
    if method[0] == "div":
        result = calculate_number[0] / number
        result = format(result, ".4f") # 保留4位小数
    v.set(result)

# 清零函数
def clear():
    # mb.showinfo(title="消息", message="已经清空")
    global number
    number = 0
    v.set(number)
    number_list.clear()
    calculate_number.clear()
    method.clear()

# 在display_frame中设定Label
v = tk.StringVar()
label = tk.Label(frame_display, width=15, height=3, bg="gray", textvariable=v).pack(side="right")
v.set(number)

# 数字按键
button_seven = tk.Button(frame_number_row1, width=3, height=2, text="7", command=seven).pack(side="left")
button_eight = tk.Button(frame_number_row1, width=3, height=2, text="8", command=eight).pack(side="left")
button_nine = tk.Button(frame_number_row1, width=3, height=2, text="9", command=nine).pack(side="left")
button_four = tk.Button(frame_number_row2, width=3, height=2, text="4", command=four).pack(side="left")
button_five = tk.Button(frame_number_row2, width=3, height=2, text="5", command=five).pack(side="left")
button_six = tk.Button(frame_number_row2, width=3, height=2, text="6", command=six).pack(side="left")
button_one = tk.Button(frame_number_row3, width=3, height=2, text="1", command=one).pack(side="left")
button_two = tk.Button(frame_number_row3, width=3, height=2, text="2", command=two).pack(side="left")
button_three = tk.Button(frame_number_row3, width=3, height=2, text="3", command=three).pack(side="left")
button_zero = tk.Button(frame, width=3, height=2, text="0", command=zero).pack(side="left")

# 运算按键
button_mul = tk.Button(frame_number_row1, width=3, height=2, text="x", command=mul)
button_mul.pack()
button_mul = tk.Button(frame_number_row2, width=3, height=2, text="-", command=sub)
button_mul.pack()
button_mul = tk.Button(frame_number_row3, width=3, height=2, text="+", command=add)
button_mul.pack()
button_mul = tk.Button(frame, width=3, height=2, text="➗", command=div)
button_mul.pack(side="right")
# 清零，计算按键
button_left = tk.Button(frame, width=3, height=2, text="C", command=clear)
button_left.pack(side="left")

button_right = tk.Button(frame, width=3, height=2, text="=", command=calculate)
button_right.pack(side="left")


# 主窗口循环显示
root.mainloop()
