from tkinter import *
root = Tk()
root.geometry("300x400+300+300")
root.resizable(0,0)
root.title("SCI CALCULATOR")

row1= Frame(root).pack(expand=True, fill="both",)
row2= Frame(root).pack(expand=True, fill="both",)
row3= Frame(root).pack(expand=True, fill="both",)
row4= Frame(root).pack(expand=True, fill="both",)

btn1 = Button(row1, text="1", font="Verdana 22" ).pack(side=LEFT,expand=True,fill="both")


root.mainloop()