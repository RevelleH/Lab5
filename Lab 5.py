import tkinter as tk
from tkinter import *

top = Tk()
top.geometry("500x600")
top.title("Calculator")

answer = Text(top, width=25, height=2, font=("Arial", 14))
answer.place(x=50, y=50)

def show(x):
    try:
        if x == "=":
            final_answer = eval(answer.get(1.0, "end-1c"))
            answer.delete(1.0, END)
            answer.insert(tk.INSERT, final_answer)
        elif x == "C":
            answer.delete(1.0, END)
        else:
            answer.insert(END, x)
    except Exception:
        answer.delete(1.0, END)
        answer.insert(tk.INSERT, "Error")

B1 = Button(top, text="1", width=10, height=5, command=lambda: show("1"))
B1.place(x=50, y=150)
B2 = Button(top, text="2", width=10, height=5, command=lambda: show("2"))
B2.place(x=150, y=150)
B3 = Button(top, text="3", width=10, height=5, command=lambda: show("3"))
B3.place(x=250, y=150)
B4 = Button(top, text="4", width=10, height=5, command=lambda: show("4"))
B4.place(x=50, y=250)
B5 = Button(top, text="5", width=10, height=5, command=lambda: show("5"))
B5.place(x=150, y=250)
B6 = Button(top, text="6", width=10, height=5, command=lambda: show("6"))
B6.place(x=250, y=250)
B7 = Button(top, text="7", width=10, height=5, command=lambda: show("7"))
B7.place(x=50, y=350)
B8 = Button(top, text="8", width=10, height=5, command=lambda: show("8"))
B8.place(x=150, y=350)
B9 = Button(top, text="9", width=10, height=5, command=lambda: show("9"))
B9.place(x=250, y=350)
B0 = Button(top, text="0", width=10, height=5, command=lambda: show("0"))
B0.place(x=150, y=450)

B_add = Button(top, text="+", width=10, height=5, command=lambda: show("+"))
B_add.place(x=350, y=150)
B_sub = Button(top, text="-", width=10, height=5, command=lambda: show("-"))
B_sub.place(x=350, y=250)
B_mul = Button(top, text="*", width=10, height=5, command=lambda: show("*"))
B_mul.place(x=350, y=350)
B_div = Button(top, text="/", width=10, height=5, command=lambda: show("/"))
B_div.place(x=350, y=450)
B_eq = Button(top, text="=", width=10, height=5, command=lambda: show("="))
B_eq.place(x=250, y=450)
B_clear = Button(top, text="C", width=10, height=5, command=lambda: show("C"))
B_clear.place(x=50, y=450)
B_neg = Button(top, text="(-)", width=10, height=5, command=lambda: show("-"))
B_neg.place(x=350, y=50)

top.mainloop()
