import tkinter as tk
from tkinter import *
from tkinter import messagebox
window = tk.Tk()

# setting title of a window
window.title("GUI")
# window.geometry('350x200')

# lbl = tkinter.Label(window,text="Hi i am Musharruf").pack()
# l1 = tkinter.Label(window,text="Musharruf",font=("Arial Bold",50)).pack()
# l1.grid(column=0,row=0)

# # sizing a window
#
# # creating a button
# bt = tk.Button(window,text="Enter")
# bt.grid(column=1,row=0)
#
# # change color and background color of a button
# bt1 = tk.Button(window,text="submit",bg="orange",fg="red")
# bt1.grid(column=1,row=1)
#
# # function to print after clicking button
# def clicked():
#     bt2.configure(text="Button was clicked !!")
# bt2 = tk.Button(window,text="print",command=clicked)
# bt2.grid(column=1,row=2)
#
# # creating a entry widgets
# txt = tk.Entry(window,width=10)
# txt.grid(column=1,row=3)
# def clicked1():
#     res = "welcome to "+txt.get()
#     l2.configure(text=res)
# btn3 = tk.Button(window,text="enter", command=clicked1).grid(column=2,row=3)
#
# # comboBox widget(drop-down)
# n = tk.StringVar()
# combo = tkk.Combobox(window, width=27,textvariable = n)
# combo['values']=(1,2,3,4,5,'text')
# combo.current(3)
# combo.grid(column=5,row=0)
#
# # CheckButton widget
# chk_state = BooleanVar()
# chk_state.set(True)
# chk = Checkbutton(window,text="select",var=chk_state)
# chk.grid(column=6,row=0)
#
# # radio button
# rad1 = Radiobutton(window,text='python',value=1)
# rad2 = Radiobutton(window,text='java',value=2)
# rad3 = Radiobutton(window,text='django',value=3)
# rad1.grid(column=7,row=0)
# rad2.grid(column=8,row=0)
# rad3.grid(column=9,row=0)
#
# # scrolledtext widget {from tkinter import scrolledtext}
# scrl = scrolledtext.ScrolledText(window,width=30,height=10)
#
# # messagebox widget {from tkinter import messagebox} with example
# # functions in messagebox:
# # showinfo(), showwarning(), showerror(), askquestion(), askokcancel(),askyesno(), askretrycancel()
# def clicked2():
#     messagebox.showinfo("Message title","message content")
# btn4 = tk.Button(window,text="enter",command=clicked2).pack()


# spinbox widget
# spin = Spinbox(window,from_=0, to=100, width=15).pack()

# Geomentry management-pack(), grid(), place()
# # organizing layout and widgets
# # frame - it is used to create the division in the window, you can aligh the frames as you like with the side parameter of pack() method
# top_frame = tk.Frame(window).pack()
# bottom_frame = tk.Frame(window).pack(side="bottom")

# b1 = tk.Button(top_frame, text="Button1", fg="red").pack()
# b2 = tk.Button(top_frame, text="Button2", fg="green").pack()
# b3 = tk.Button(bottom_frame, text="Button3", fg="purple").pack(side="left")
# b4 = tk.Button(bottom_frame, text="Button4", fg="blue").pack(side="left")

# tk.Label(window, text="Suf. width", fg="white",bg="purple").pack()
# tk.Label(window, text="taking all available x width", fg="white",bg="green").pack(fill="x")
# tk.Label(window, text="taking all available y height", fg="white",bg="orange").pack(side="left",fill="y")

# tk.Label(window, text="UserName").grid(row=0)
# tk.Entry(window).grid(row=0,column=1)

# tk.Label(window, text="password").grid(row=1)
# tk.Entry(window).grid(row=1,column=1)

# tk.Checkbutton(window, text="keep me login").grid(row=2, columnspan=2)

# def hi():
#     tk.Label(window,text="hi i am musharruf").pack()

# tk.Button(window, text="click Me", command=hi).pack()

# # event binding
# def say1(event):
#     tk.Label(window,text="this is left button").pack()
# def say2(event):
#     tk.Label(window,text="this is middle button").pack()
# def say3(event):
#     tk.Label(window,text="this is right button").pack()

# btn5 = tk.Button(window, text="click me")
# btn5.bind("<Button-1>",say1)
# btn5.pack()
# btn6 = tk.Button(window, text="click me")
# btn6.bind("<Button-1>",say2)
# btn6.pack()
# btn7 = tk.Button(window, text="click me")
# btn7.bind("<Button-1>",say3)
# btn7.pack()

# def left_click(event):
#     tk.Label(window, text="left click").pack()
# def middle_click(event):
#     tk.Label(window, text="middle click").pack()
# def right_click(event):
#     tk.Label(window, text="right click").pack()

# window.bind("<Button-1>",left_click)
# window.bind("<Button-2>",middle_click)
# window.bind("<Button-3>",right_click)

# images in tkinter
# icon = tk.PhotoImage(file="videos\shapess.png")
# label = tk.Label(window,image=icon).pack()

window.mainloop()


















# widgets in tkinter
# Label, Button, Entry, ComboBox, CheckBox, CheckButton, Radio, ScrollText, # #SpinBox, Menu Bar, Notebook