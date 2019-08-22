from tkinter import *
import math
import unicodedata

expression= ""
PI = unicodedata.lookup("GREEK CAPITAL LETTER PI")
def btn_clear():
    global expression
    expression = ""
    display.set("0")

def btn_clicked(num):
    global expression
    expression = expression + str(num)
    display.set(expression)


def result():
    global expression

    try:
        res = eval(expression, {"sin": math.sin}, {"cos":math.cos})             #here is th e[place i want to edit
        res =round(res,13)
        display.set(str(res))
        expression = str(res)
    except ZeroDivisionError:
        display.set("Invalid")




root = Tk()
root.geometry("500x400+120+120")
root.resizable(0,0)
root.title("SCIENTIFIC CALCULATOR")

display = StringVar()

frame1 = Frame(root)
frame1.pack(expand= True, fill="both")
frame2 = Frame(root)
frame2.pack(expand= True, fill="both")
frame3 = Frame(root)
frame3.pack(expand= True, fill="both")
frame4 = Frame(root)
frame4.pack(expand= True, fill="both")
frame5 = Frame(root)
frame5.pack(expand= True, fill="both")
frame6 = Frame(root)
frame6.pack(expand= True, fill="both")



entry_box = Entry(frame1, justify =RIGHT, font="Verdana 20", textvariable = display, bg="WHITE").pack(expand = True, fill="both")


btn7 = Button(frame2, text="7", font="Verdana 22", bd=0, relief=GROOVE, command=lambda :btn_clicked(7)).pack(side=LEFT, expand=True, fill="both")
btn8 = Button(frame2, text="8", font="Verdana 22", bd=0, relief=GROOVE, command=lambda :btn_clicked(8)).pack(side=LEFT, expand=True, fill="both")
btn9 = Button(frame2, text="9", font="Verdana 22", bd=0, relief=GROOVE, command=lambda :btn_clicked(9)).pack(side=LEFT, expand=True, fill="both")
btn_mul = Button(frame2, text="*", font="Verdana 22", bd=0, relief=GROOVE, command=lambda :btn_clicked('*')).pack(side=LEFT, expand=True, fill="both")
btn_sin = Button(frame2, text="sin", font="Verdana 22", bd=0, relief=GROOVE, command=lambda :btn_clicked('sin(')).pack(side=LEFT, expand=True, fill="both")
btn_log = Button(frame2, text="log", font="Verdana 22", bd=0, relief=GROOVE, command=lambda :btn_clicked('log(')).pack(side=LEFT, expand=True, fill="both")




btn4 = Button(frame3, text="4", font="Verdana 22", bd=0, relief=GROOVE, command=lambda :btn_clicked(4)).pack(side=LEFT, expand=True, fill="both")
btn5 = Button(frame3, text="5", font="Verdana 22", bd=0, relief=GROOVE, command=lambda :btn_clicked(5)).pack(side=LEFT, expand=True, fill="both")
btn6 = Button(frame3, text="6", font="Verdana 22", bd=0, relief=GROOVE, command=lambda :btn_clicked(6)).pack(side=LEFT, expand=True, fill="both")
btn_sub = Button(frame3, text="-", font="Verdana 22", bd=0, relief=GROOVE, command=lambda :btn_clicked('-')).pack(side=LEFT, expand=True, fill="both")
btn_cos = Button(frame3, text="cos", font="Verdana 22", bd=0, relief=GROOVE, command=lambda :btn_clicked('cos(')).pack(side=LEFT, expand=True, fill="both")
btn_ln = Button(frame3, text="ln", font="Verdana 22", bd=0, relief=GROOVE, command=lambda : btn_clicked('ln(')).pack(side=LEFT, expand=True, fill="both")


btn1 = Button(frame4, text="1", font="Verdana 22", bd=0, relief=GROOVE,  command=lambda :btn_clicked(1)).pack(side=LEFT, expand=True, fill="both")
btn2 = Button(frame4, text="2", font="Verdana 22", bd=0, relief=GROOVE, command=lambda :btn_clicked(2)).pack(side=LEFT, expand=True, fill="both")
btn3 = Button(frame4, text="3", font="Verdana 22", bd=0, relief=GROOVE, command=lambda :btn_clicked(3)).pack(side=LEFT, expand=True, fill="both")
btn_divide = Button(frame4, text="/", font="Verdana 22", bd=0, relief=GROOVE, command=lambda : btn_clicked('/')).pack(side=LEFT, expand=True, fill="both")
btn_tan = Button(frame4, text="tan", font="Verdana 22", bd=0, relief=GROOVE, command=lambda : btn_clicked('tan(')).pack(side=LEFT, expand=True, fill="both")
btn_pow = Button(frame4, text="^", font="Verdana 22", bd=0, relief=GROOVE, command=lambda :btn_clicked('**')).pack(side=LEFT, expand=True, fill="both")


btn_decimal = Button(frame5, text=".", font="Verdana 22", bd=0, relief=GROOVE, command=lambda :btn_clicked('.')).pack(side=LEFT, expand=True, fill="both")
btn0 = Button(frame5, text="0", font="Verdana 22", bd=0, relief=GROOVE, command=lambda :btn_clicked(0)).pack(side=LEFT, expand=True, fill="both")
btn_clear = Button(frame5, text="C",font="Verdana 22", bd=0, relief=GROOVE,command=btn_clear).pack(side=LEFT,expand=True,fill="both")
btn_add = Button(frame5, text="+", font="Verdana 22", bd=0, relief=GROOVE, command=lambda :btn_clicked('+')).pack(side=LEFT, expand=True, fill="both")
btn_square =  Button(frame5, text='x\u00b2', font="Verdana 22", bd=0, relief=GROOVE, command=lambda :btn_clicked('**2')).pack(side=LEFT, expand=True, fill="both")
btn_root =  Button(frame5, text='\u221A', font="Verdana 22", bd=0, relief=GROOVE, command=lambda :btn_clicked('\u221A')).pack(side=LEFT, expand=True, fill="both")

btn_pi = Button(frame6, text=PI, font="Verdana 22", bd=0, relief=GROOVE, command=lambda :btn_clicked(math.pi)).pack(side=LEFT, expand=True, fill="both")
btn_open_bracket = Button(frame6, text="(", font="Verdana 22", bd=0, relief=GROOVE, command=lambda :btn_clicked('(')).pack(side=LEFT, expand=True, fill="both")
btn_closed_bracket = Button(frame6, text=")", font="Verdana 22", bd=0, relief=GROOVE, command=lambda :btn_clicked(')')).pack(side=LEFT, expand=True, fill="both")
btn_e = Button(frame6, text="e", font="Verdana 22", bd=0, relief=GROOVE, command=lambda :btn_clicked(math.e)).pack(side=LEFT, expand=True, fill="both")
btn_fact = Button(frame6, text="x!", font="Verdana 22", bd=0, relief=GROOVE, command=lambda :btn_clicked('!')).pack(side=LEFT, expand=True, fill="both")
btn_equal = Button(frame6, text= "=", font="Verdana 22", bd=0, relief=GROOVE, command=result).pack(side=LEFT, expand=True, fill="both")


root.mainloop()
