from tkinter import *

window=Tk()

def kgs_conversion():
    grams=float(e1_value.get())*1000
    pounds=float(e1_value.get())*2.204
    ounces=float(e1_value.get())*35.274
    t1_g.delete("1.0", END)
    t1_g.insert(END, grams)
    t1_p.delete("1.0", END)
    t1_p.insert(END, pounds)
    t1_o.delete("1.0", END)
    t1_o.insert(END, ounces)

e2=Label(window, text="Kg")
e2.grid(row=0,column=0)

b1=Button(window, text="Convert", command=kgs_conversion)
b1.grid(row=0,column=2)

e1_value= StringVar()
e1=Entry(window, textvariable=e1_value)
e1.grid(row=0,column=1)

t1_g=Text(window, height=1, width=20)
t1_g.grid(row=1,column=0)

t1_p=Text(window, height=1, width=20)
t1_p.grid(row=1,column=1)

t1_o=Text(window, height=1, width=20)
t1_o.grid(row=1,column=2)

window.mainloop()
