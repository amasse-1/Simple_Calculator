# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 19:32:07 2020
@author: Anthony
"""

import tkinter as tk

#button press function
def press(num):
    global expression    
    
    expression = expression +str(num)
    
    equation.set(expression)

#equals function
def equal():
    try:
        global expression
        
        total = str(eval(expression))
        
        equation.set(total)
        
        expression = str(total)
        
    except:
        equation.set("error")
        expression = ""
        
#clear function
def clear():
    global expression
    expression = ""
    equation.set("")
    
if __name__ == "__main__":
    calc = tk.Tk()

    expression = ""

    calc.configure(background = "black")

    calc.title("Calculator")

    calc.geometry("300x200")

    equation = tk.StringVar()

    field = tk.Entry(calc, textvariable = equation, bg = "#dbddde") # a light grey
    field.grid(columnspan=4, ipadx = 80)
    
    #the buttons
    nine = tk.Button(calc, text = "9", fg="white", bg = "gray",
                     command=lambda: press(9), height=2, width=7)
    eight = tk.Button(calc, text = "8", fg="white", bg = "gray",
                     command=lambda: clear(8), height=2, width=7)
    seven = tk.Button(calc, text = "7", fg="white", bg = "gray",
                     command=lambda: press(7), height=2, width=7)
    six = tk.Button(calc, text = "6", fg="white", bg = "gray",
                     command=lambda: press(6), height=2, width=7)
    five = tk.Button(calc, text = "5", fg="white", bg = "gray",
                     command=lambda: press(5), height=2, width=7)
    four = tk.Button(calc, text = "4", fg="white", bg = "gray",
                     command=lambda: press(4), height=2, width=7)
    three = tk.Button(calc, text = "3", fg="white", bg = "gray",
                     command=lambda: press(3), height=2, width=7)
    two = tk.Button(calc, text = "2", fg="white", bg = "gray",
                     command=lambda: press(2), height=2, width=7)
    one = tk.Button(calc, text = "1", fg="white", bg = "gray",
                     command=lambda: press(1), height=2, width=7)
    zero = tk.Button(calc, text = "0", fg="white", bg = "gray",
                     command=lambda: press(0), height=2, width=7)
    add= tk.Button(calc, text = "+", fg="white", bg = "gray",
                     command=lambda: press("+"), height=2, width=7)
    subtract= tk.Button(calc, text = "-", fg="white", bg = "gray",
                     command=lambda: press("-"), height=2, width=7)
    multiply = tk.Button(calc, text = "*", fg="white", bg = "gray",
                    command=lambda: press("*"), height=2, width=7)
    divide = tk.Button(calc, text = "/", fg="white", bg = "gray",
                     command=lambda: press("/"), height=2, width=7)
    clears = tk.Button(calc, text = "C", fg="white", bg = "gray",
                     command=lambda: clear, height=2, width=7)
    equals = tk.Button(calc, text = "=", fg="white", bg = "gray",
                     command=lambda: equal(), height=2, width=7)
    
    #grid of buttons
    nine.grid(row=2, column=0)
    eight.grid(row=2, column = 1)
    seven.grid(row=2, column = 2)
    add.grid(row=2, column=3)
    six.grid(row = 3, column = 0)
    five.grid(row=3, column=1)
    four.grid(row=3, column = 2)
    subtract.grid(row=3, column = 3)
    three.grid(row=4, column = 0)
    two.grid(row=4, column = 1)
    one.grid(row=4, column = 2)
    multiply.grid(row=4, column = 3)
    zero.grid(row = 5, column = 0)
    clears.grid(row = 5, column = 1)
    equals.grid(row=5, column = 2)
    divide.grid(row=5, column = 3)
    
    calc.mainloop()