import tkinter as tk
from tkinter import messagebox

def button_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)

def button_clear():
    global expression
    expression = ""
    input_text.set("")

def button_equal():
    global expression
    try:
        total = str(eval(expression))
        input_text.set(total)
        expression = total
    except:
        messagebox.showinfo("Hiba", "Hibás bemenet")
        input_text.set("")
        expression = ""

expression = ""


app = tk.Tk()
app.geometry("300x400")
app.title("Calculator")


input_text = tk.StringVar()
input_frame = tk.Frame(app, width=312, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=1)
input_frame.pack(side=tk.TOP)

label = tk.Label(app, text="Általános számológép", font=('arial', 18, 'bold'))
label.pack()
input_field = tk.Entry(input_frame, font=('arial', 18, 'bold'), textvariable=input_text, width=50, bg="#eee", bd=0, justify=tk.RIGHT)
input_field.grid(row=0, column=0)
input_field.pack(ipady=10)


button_frame = tk.Frame(app, width=312, height=272.5, bg="grey")
button_frame.pack()


button_percent = tk.Button(button_frame, text="%", padx=36, pady=20, command=lambda: button_click('%'))
button_CE = tk.Button(button_frame, text="CE", padx=30, pady=20, command=lambda: button_clear())
button_C = tk.Button(button_frame, text="C", padx=34, pady=20, command=lambda: button_clear())
button_back = tk.Button(button_frame, text="⌫", padx=30, pady=20, command=lambda: button_click(''))
button7 = tk.Button(button_frame, text='7', padx=40, pady=20, command=lambda: button_click(7))
button8 = tk.Button(button_frame, text='8', padx=40, pady=20, command=lambda: button_click(8))
button9 = tk.Button(button_frame, text='9', padx=40, pady=20, command=lambda: button_click(9))
button_divide = tk.Button(button_frame, text='÷', padx=39, pady=20, command=lambda: button_click('/'))
button4 = tk.Button(button_frame, text='4', padx=40, pady=20, command=lambda: button_click(4))
button5 = tk.Button(button_frame, text='5', padx=40, pady=20, command=lambda: button_click(5))
button6 = tk.Button(button_frame, text='6', padx=40, pady=20, command=lambda: button_click(6))
button_multiply = tk.Button(button_frame, text='×', padx=39, pady=20, command=lambda: button_click('*'))
button1 = tk.Button(button_frame, text='1', padx=40, pady=20, command=lambda: button_click(1))
button2 = tk.Button(button_frame, text='2', padx=40, pady=20, command=lambda: button_click(2))
button3 = tk.Button(button_frame, text='3', padx=40, pady=20, command=lambda: button_click(3))
button_subtract = tk.Button(button_frame, text='-', padx=41, pady=20, command=lambda: button_click('-'))
button_plus_minus = tk.Button(button_frame, text='+/-', padx=33, pady=20, command=lambda: button_click('-'))
button0 = tk.Button(button_frame, text='0', padx=40, pady=20, command=lambda: button_click(0))
button_dot = tk.Button(button_frame, text='.', padx=42, pady=20, command=lambda: button_click('.'))
button_add = tk.Button(button_frame, text='+', padx=39, pady=20, command=lambda: button_click('+'))
button_equal = tk.Button(button_frame, text='=', padx=39, pady=20, command=button_equal)


button_percent.grid(row=1, column=0)
button_CE.grid(row=1, column=1)
button_C.grid(row=1, column=2)
button_back.grid(row=1, column=3)
button7.grid(row=2, column=0)
button8.grid(row=2, column=1)
button9.grid(row=2, column=2)
button_divide.grid(row=2, column=3)
button4.grid(row=3, column=0)
button5.grid(row=3, column=1)
button6.grid(row=3, column=2)
button_multiply.grid(row=3, column=3)
button1.grid(row=4, column=0)
button2.grid(row=4, column=1)
button3.grid(row=4, column=2)
button_subtract.grid(row=4, column=3)
button_plus_minus.grid(row=5, column=0)
button0.grid(row=5, column=1)
button_dot.grid(row=5, column=2)
button_add.grid(row=5, column=3)
button_equal.grid(row=6, column=2)
comma_button = tk.Button(button_frame, text=",", padx=40, pady=20, command=lambda: button_click('.'))
comma_button.grid(row=6, column=1)


app.mainloop()
