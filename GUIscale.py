from tkinter import *

def select():
    val = "Value = " + str(v.get())
    ans.set(val)


root= Tk()
root.title("Scale Demo")
root.geometry("200x100")
v=DoubleVar()
ans=StringVar()
Scale(root, variable=v, from_ = 1, to = 50, orient=HORIZONTAL).pack(anchor=CENTER)
Button(root, text="Value", command=select).pack(anchor=CENTER)
l1=Label(root,textvariable=ans).pack()

mainloop()

