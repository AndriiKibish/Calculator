frfrom tkinter import *
from math import pow, sqrt, sin, cos, tan, log

def dan():
    num1_int = int(num1.get())
    num2_int = int(num2.get())
    return num1_int, num2_int


def one_c():
    num1_int = int(num1.get())
    return num1_int


def sum_result():
    num1_int, num2_int = dan()
    result = num1_int + num2_int
    label.config(text=f'{result}')


def diff_result():
    num1_int, num2_int = dan()
    result = num1_int - num2_int
    label.config(text=f'{result}')


def div_result():
    num1_int, num2_int = dan()
    try:
        result = num1_int / num2_int
        label.config(text=f'{result}')
    except:
        num2_int = 0
        print("division by zero")
        label.config(text='Division by zero not possible')


def mult_result():
    num1_int, num2_int = dan()
    result = num1_int * num2_int
    label.config(text=f'{result}')


win = Tk()
win.geometry('300x400')
Label(win, text='Number1', font=('Calibri 17')).pack()
num1 = Entry(win, width=20)
num1.pack()
Label(win, text='Number2', font=('Calibri 17')).pack()
num2 = Entry(win, width=20)
num2.pack()
Button(win, font=('Calibri 17'), text='+', command=sum_result).pack()
Button(win, font=('Calibri 17'), text='-', command=diff_result).pack()
Button(win, font=('Calibri 17'), text='/', command=div_result).pack()
Button(win, font=('Calibri 17'), text='*', command=mult_result).pack()
label = Label(win, text='Result:', font=('Calibri 17'))
label.pack(pady=20)

win.mainloop()
