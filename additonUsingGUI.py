from tkinter import *
root=Tk()

root.title("Addition of numbers")
root.geometry("400x350")

def add():
    res = int(n1.get()) + int(n2.get())
    result.set(res)


Label(root, text="First Number: ").grid(row=0, sticky=W)
Label(root, text="Second Number: ").grid(row=1, sticky=W)
Label(root, text="Result: ").grid(row=2, sticky=W)

n1=StringVar()
n2=StringVar()
result=StringVar()
Entry(root, textvariable=n1).grid(row=0, column=1, sticky=W)
Entry(root, textvariable=n2).grid(row=1, column=1, sticky=W)

Entry(root, textvariable=result).grid(row=2, column=1, sticky=W)
Button(root, text="Calculate", command=add).grid(row=0, column=2, columnspan=2, rowspan=2, padx=5, pady=5)

mainloop()

