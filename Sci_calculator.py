from tkinter import *
import math
from tkinter import messagebox
import unicodedata

expression= ""


def btn_clear():
    global expression
    expression = ""
    display.set("0")

def btnAC():
    global expression
    expression = expression[:-1]
    display.set(expression)

def btn_clicked(num):
    global expression
    expression = expression + str(num)
    display.set(expression)

def angular_conversion():
    global expression
    expression = round(math.degrees(float(expression)),6)
    display.set(expression)


def result():
    global expression

    try:

        res = eval(expression,{'sin':math.sin, 'cos':math.cos,'tan':math.tan, 'sqrt':math.sqrt, 'log':math.log10, 'exp':math.exp,
                               'ln':math.log, 'asin':math.asin, 'deg':math.radians })
        res = round(res, 15)
        display.set(str(res))
        expression = str(res)

    except ZeroDivisionError:
        display.set("Invalid")

    except ValueError:
        display.set("Invalid")

    except SyntaxError:
        messagebox.showerror("ERROR", "Syntax Error")

    except TypeError:
        messagebox.showerror("ERROR", "Syntax Error")


root = Tk()
root.geometry("900x450+120+120")
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
frame7 = Frame(root)
frame7.pack(expand= True, fill="both")


entry_box = Label(frame1, anchor='ne', font="Dina 20", textvariable = display, bg="AntiqueWhite1").pack(expand = True, fill="both")

note = Label(frame7, anchor='sw', font="Dina 10", text='NOTE: [cDeg=Convert number to degree] [Trigo functions take and give answers in Radians as default]', bg="PeachPuff3").pack(expand=True,fill="both")


btn7 = Button(frame2, text="7 ", font="Dina 22", bd=0, relief=GROOVE, command=lambda :btn_clicked(7), activebackground="PeachPuff3",bg="PeachPuff2").pack(side=LEFT, expand=True, fill="both")
btn8 = Button(frame2, text=" 8 ", font="Dina 22", bd=0, relief=GROOVE, command=lambda :btn_clicked(8), activebackground="PeachPuff3",bg="PeachPuff2").pack(side=LEFT, expand=True, fill="both")
btn9 = Button(frame2, text="9 ", font="Dina 22", bd=0, relief=GROOVE, command=lambda :btn_clicked(9), activebackground="PeachPuff3",bg="PeachPuff2").pack(side=LEFT, expand=True, fill="both")
btn_mul = Button(frame2, text="*", font="Dina 22", bd=0, relief=GROOVE, command=lambda :btn_clicked('*'), activebackground="PeachPuff3",bg="PeachPuff2").pack(side=LEFT, expand=True, fill="both")
btn_sin = Button(frame2, text="sin", font="Dina 22", bd=0, relief=GROOVE, command=lambda :btn_clicked('sin('), activebackground="PeachPuff3",bg="PeachPuff2").pack(side=LEFT, expand=True, fill="both")
btn_asin = Button(frame2, text='asin', font="Dina 22", bd=0, relief=GROOVE, command=lambda :btn_clicked('asin('), activebackground="PeachPuff3",bg="PeachPuff2").pack(side=LEFT, expand=True, fill="both")
btn_log = Button(frame2, text="log ", font="Dina 22", bd=0, relief=GROOVE, command=lambda :btn_clicked('log('), activebackground="PeachPuff3",bg="PeachPuff2").pack(side=LEFT, expand=True, fill="both")

btn4 = Button(frame3, text="4 ", font="Dina 22", bd=0, relief=GROOVE, command=lambda :btn_clicked(4), activebackground="PeachPuff3",bg="PeachPuff2").pack(side=LEFT, expand=True, fill="both")
btn5 = Button(frame3, text="  5", font="Dina 22", bd=0, relief=GROOVE, command=lambda :btn_clicked(5), activebackground="PeachPuff3",bg="PeachPuff2").pack(side=LEFT, expand=True, fill="both")
btn6 = Button(frame3, text="  6", font="Dina 22", bd=0, relief=GROOVE, command=lambda :btn_clicked(6), activebackground="PeachPuff3",bg="PeachPuff2").pack(side=LEFT, expand=True, fill="both")
btn_sub = Button(frame3, text="  -", font="Dina 22", bd=0, relief=GROOVE, command=lambda :btn_clicked('-'), activebackground="PeachPuff3",bg="PeachPuff2").pack(side=LEFT, expand=True, fill="both")
btn_cos = Button(frame3, text=" cos", font="Dina 22", bd=0, relief=GROOVE, command=lambda :btn_clicked('cos('), activebackground="PeachPuff3",bg="PeachPuff2").pack(side=LEFT, expand=True, fill="both")
btn_acos = Button(frame3, text="acos", font="Dina 22", bd=0, relief=GROOVE, command=lambda :btn_clicked('acos('), activebackground="PeachPuff3",bg="PeachPuff2").pack(side=LEFT, expand=True, fill="both")
btn_ln = Button(frame3, text=" ln  ", font="Dina 22", bd=0, relief=GROOVE, command=lambda : btn_clicked('ln('), activebackground="PeachPuff3",bg="PeachPuff2").pack(side=LEFT, expand=True, fill="both")

btn1 = Button(frame4, text="1 ", font="Dina 22", bd=0, relief=GROOVE,  command=lambda :btn_clicked(1),activebackground="PeachPuff3",bg="PeachPuff2").pack(side=LEFT, expand=True, fill="both")
btn2 = Button(frame4, text="2", font="Dina 22", bd=0, relief=GROOVE, command=lambda :btn_clicked(2), activebackground="PeachPuff3",bg="PeachPuff2").pack(side=LEFT, expand=True, fill="both")
btn3 = Button(frame4, text="  3 ", font="Dina 22", bd=0, relief=GROOVE, command=lambda :btn_clicked(3), activebackground="PeachPuff3",bg="PeachPuff2").pack(side=LEFT, expand=True, fill="both")
btn_divide = Button(frame4, text="/", font="Dina 22", bd=0, relief=GROOVE, command=lambda : btn_clicked('/'), activebackground="PeachPuff3",bg="PeachPuff2").pack(side=LEFT, expand=True, fill="both")
btn_tan = Button(frame4, text="tan", font="Dina 22", bd=0, relief=GROOVE, command=lambda : btn_clicked('tan('), activebackground="PeachPuff3",bg="PeachPuff2").pack(side=LEFT, expand=True, fill="both")
btn_atan = Button(frame4, text="atan", font="Dina 22", bd=0, relief=GROOVE, command=lambda :btn_clicked('atan('), activebackground="PeachPuff3",bg="PeachPuff2").pack(side=LEFT, expand=True, fill="both")
btn_pow = Button(frame4, text=" ^  ", font="Dina 22", bd=0, relief=GROOVE, command=lambda :btn_clicked('**'),activebackground="PeachPuff3",bg="PeachPuff2").pack(side=LEFT, expand=True, fill="both")

btn_one_clear = Button(frame5, text="CE", font="Dina 18", bd=0, relief=GROOVE, command=btnAC, activebackground="PeachPuff3",bg="PeachPuff2").pack(side=LEFT, expand=True, fill="both")
btn0 = Button(frame5, text="0", font="Dina 22", bd=0, relief=GROOVE, command=lambda :btn_clicked(0), activebackground="PeachPuff3",bg="PeachPuff2").pack(side=LEFT, expand=True, fill="both")
btn_clear = Button(frame5, text="AC",font="Dina 18", bd=0, relief=GROOVE,command=btn_clear, activebackground="PeachPuff3",bg="PeachPuff2").pack(side=LEFT,expand=True,fill="both")
btn_add = Button(frame5, text="+  " , font="Dina 22", bd=0, relief=GROOVE, command=lambda :btn_clicked('+'),activebackground="PeachPuff3",bg="PeachPuff2").pack(side=LEFT, expand=True, fill="both")
btn_square = Button(frame5, text='x\N{SUPERSCRIPT TWO} ', font="Dina 22", bd=0, relief=GROOVE, command=lambda :btn_clicked('**2'), activebackground="PeachPuff3",bg="PeachPuff2").pack(side=LEFT, expand=True, fill="both")
btn_root = Button(frame5, text=' \u221A  ', font="Dina 22", bd=0, relief=GROOVE, command=lambda :btn_clicked('sqrt('), activebackground="PeachPuff3",bg="PeachPuff2").pack(side=LEFT, expand=True, fill="both")
btn_pi = Button(frame5, text='  \N{GREEK SMALL LETTER PI} ', font="Dina 22", bd=0, relief=GROOVE, command=lambda :btn_clicked(math.pi), activebackground="PeachPuff3",bg="PeachPuff2").pack(side=LEFT, expand=True, fill="both")


btn_decimal = Button(frame6, text= "  .", font="Dina 22", bd=0, relief=GROOVE, command=lambda :btn_clicked('.'), activebackground="PeachPuff3",bg="PeachPuff2").pack(side=LEFT, expand=True, fill="both")
btn_open_bracket = Button(frame6, text="    ( ", font="Dina 22", bd=0, relief=GROOVE, command=lambda :btn_clicked('('),activebackground="PeachPuff3",bg="PeachPuff2").pack(side=LEFT, expand=True, fill="both")
btn_closed_bracket = Button(frame6, text="    )  ", font="Dina 22", bd=0, relief=GROOVE, command=lambda :btn_clicked(')'), activebackground="PeachPuff3",bg="PeachPuff2").pack(side=LEFT, expand=True, fill="both")
btn_equal = Button(frame6, text= "  =", font="Dina 22", bd=0, relief=GROOVE, command=result, activebackground="PeachPuff3",bg="PeachPuff2").pack(side=LEFT, expand=True, fill="both")
btn_exp = Button(frame6, text="   exp", font="Dina 22", bd=0, relief=GROOVE, command=lambda :btn_clicked('exp('), activebackground="PeachPuff3",bg="PeachPuff2").pack(side=LEFT, expand=True, fill="both")
btn_deg = Button(frame6, text="  deg", font="Dina 22", bd=0, relief=GROOVE, command=lambda :btn_clicked('deg('), activebackground="PeachPuff3",bg="PeachPuff2").pack(side=LEFT, expand=True, fill="both")
btn_convert_deg = Button(frame6, text="cDeg", font="Dina 22", bd=0, relief=GROOVE, command=angular_conversion, activebackground="PeachPuff3",bg="PeachPuff2").pack(side=LEFT, expand=True, fill="both")


root.mainloop()
