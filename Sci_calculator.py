from tkinter import *
import math
import unicodedata

expression= ""

PI = unicodedata.lookup("GREEK CAPITAL LETTER PI")
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

def result():
    global expression

    try:
        if "sin(" in expression:

            i = expression.find("sin(")
            pos_start = i+4                                  #line from 25 to 27 is for obtaing number between brackets
            pos_end  = expression.find(")",pos_start)
            short_expression = expression[pos_start:pos_end]
            final_result = round(math.sin(math.radians(float(eval(short_expression)))), 6)
            short_expression = 'sin(' + short_expression + ')'
            expression = expression.replace(short_expression,str(final_result) )    #29,30 line to replace value of sin() in exprssion

        if "tan(" in expression:

            i = expression.find("tan(")
            pos_start = i+4                                  #line from 25 to 27 is for obtaing number between brackets
            pos_end  = expression.find(")",pos_start)
            short_expression = expression[pos_start:pos_end]
            final_result = round(math.tan(math.radians(float(eval(short_expression)))), 6)
            length = len(short_expression)
            print(length)
            short_expression = 'tan(' + short_expression + ')'
            expression = expression.replace(short_expression,str(final_result))

        if "cos(" in expression:

            i = expression.find("cos(")
            pos_start = i+4                                  #line from 25 to 27 is for obtaing number between brackets
            pos_end  = expression.find(")",pos_start)
            short_expression = expression[pos_start:pos_end]
            final_result = round(math.cos(math.radians(float(eval(short_expression)))), 6)
            short_expression = 'cos(' + short_expression + ')'
            expression = expression.replace(short_expression,str(final_result) )

        if "log(" in expression:
            i = expression.find("log(")
            pos_start = i + 4  # line from 25 to 27 is for obtaing number between brackets
            pos_end = expression.find(")", pos_start)
            short_expression = expression[pos_start:pos_end]
            final_result = round(math.log10(float(eval(short_expression))), 6)
            short_expression = 'log(' + short_expression + ')'
            expression = expression.replace(short_expression, str(final_result))

        if "ln(" in expression:
            i = expression.find("ln(")
            pos_start = i + 3  # line from 25 to 27 is for obtaing number between brackets
            pos_end = expression.find(")", pos_start)
            short_expression = expression[pos_start:pos_end]
            final_result = round(math.log(float(eval(short_expression)),math.e), 6)
            short_expression = 'ln(' + short_expression + ')'
            expression = expression.replace(short_expression, str(final_result))

        if "\u221A(" in expression:
                i = expression.find("\u221A(")
                pos_start = i + 2                         # line from 25 to 27 is for obtaing number between brackets
                pos_end = expression.find(")", pos_start)
                short_expression = expression[pos_start:pos_end]
                final_result = round(math.sqrt(float(eval(short_expression))), 6)
                short_expression = '\u221A(' + short_expression + ')'
                expression = expression.replace(short_expression, str(final_result))

        if "exp(" in expression:
            i = expression.find("exp(")
            pos_start = i + 4  # line from 25 to 27 is for obtaing number between brackets
            pos_end = expression.find(")", pos_start)
            short_expression = expression[pos_start:pos_end]
            final_result = round(math.exp(float(eval(short_expression))), 6)
            short_expression = 'exp(' + short_expression + ')'
            expression = expression.replace(short_expression, str(final_result))


        res = eval(expression)  # here is th e[place i want to edit
        res = round(res, 13)
        display.set(str(res))
        expression = str(res)

    except ZeroDivisionError:
        display.set("Invalid")

    except ValueError:
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


entry_box = Label(frame1, anchor='ne', font="Verdana 20", textvariable = display, bg="AntiqueWhite1").pack(expand = True, fill="both")

btn7 = Button(frame2, text="7", font="Dina 22", bd=0, relief=GROOVE, command=lambda :btn_clicked(7), activebackground="PeachPuff3",bg="PeachPuff2").pack(side=LEFT, expand=True, fill="both")
btn8 = Button(frame2, text="8", font="Dina 22", bd=0, relief=GROOVE, command=lambda :btn_clicked(8), activebackground="PeachPuff3",bg="PeachPuff2").pack(side=LEFT, expand=True, fill="both")
btn9 = Button(frame2, text="9", font="Dina 22", bd=0, relief=GROOVE, command=lambda :btn_clicked(9), activebackground="PeachPuff3",bg="PeachPuff2").pack(side=LEFT, expand=True, fill="both")
btn_mul = Button(frame2, text="*", font="Dina 22", bd=0, relief=GROOVE, command=lambda :btn_clicked('*'), activebackground="PeachPuff3",bg="PeachPuff2").pack(side=LEFT, expand=True, fill="both")
btn_sin = Button(frame2, text="sin", font="Dina 22", bd=0, relief=GROOVE, command=lambda :btn_clicked('sin('), activebackground="PeachPuff3",bg="PeachPuff2").pack(side=LEFT, expand=True, fill="both")
btn_log = Button(frame2, text="log", font="Dina 22", bd=0, relief=GROOVE, command=lambda :btn_clicked('log('), activebackground="PeachPuff3",bg="PeachPuff2").pack(side=LEFT, expand=True, fill="both")

btn4 = Button(frame3, text="4", font="Dina 22", bd=0, relief=GROOVE, command=lambda :btn_clicked(4), activebackground="PeachPuff3",bg="PeachPuff2").pack(side=LEFT, expand=True, fill="both")
btn5 = Button(frame3, text="5", font="Dina 22", bd=0, relief=GROOVE, command=lambda :btn_clicked(5), activebackground="PeachPuff3",bg="PeachPuff2").pack(side=LEFT, expand=True, fill="both")
btn6 = Button(frame3, text="6", font="Dina 22", bd=0, relief=GROOVE, command=lambda :btn_clicked(6), activebackground="PeachPuff3",bg="PeachPuff2").pack(side=LEFT, expand=True, fill="both")
btn_sub = Button(frame3, text="-", font="Dina 22", bd=0, relief=GROOVE, command=lambda :btn_clicked('-'), activebackground="PeachPuff3",bg="PeachPuff2").pack(side=LEFT, expand=True, fill="both")
btn_cos = Button(frame3, text="cos", font="Dina 22", bd=0, relief=GROOVE, command=lambda :btn_clicked('cos('), activebackground="PeachPuff3",bg="PeachPuff2").pack(side=LEFT, expand=True, fill="both")
btn_ln = Button(frame3, text="ln ", font="Dina 22", bd=0, relief=GROOVE, command=lambda : btn_clicked('ln('), activebackground="PeachPuff3",bg="PeachPuff2").pack(side=LEFT, expand=True, fill="both")

btn1 = Button(frame4, text="1", font="Dina 22", bd=0, relief=GROOVE,  command=lambda :btn_clicked(1),activebackground="PeachPuff3",bg="PeachPuff2").pack(side=LEFT, expand=True, fill="both")
btn2 = Button(frame4, text="2", font="Dina 22", bd=0, relief=GROOVE, command=lambda :btn_clicked(2), activebackground="PeachPuff3",bg="PeachPuff2").pack(side=LEFT, expand=True, fill="both")
btn3 = Button(frame4, text="3 ", font="Dina 22", bd=0, relief=GROOVE, command=lambda :btn_clicked(3), activebackground="PeachPuff3",bg="PeachPuff2").pack(side=LEFT, expand=True, fill="both")
btn_divide = Button(frame4, text="/", font="Dina 22", bd=0, relief=GROOVE, command=lambda : btn_clicked('/'), activebackground="PeachPuff3",bg="PeachPuff2").pack(side=LEFT, expand=True, fill="both")
btn_tan = Button(frame4, text="tan", font="Dina 22", bd=0, relief=GROOVE, command=lambda : btn_clicked('tan('), activebackground="PeachPuff3",bg="PeachPuff2").pack(side=LEFT, expand=True, fill="both")
btn_pow = Button(frame4, text=" ^ ", font="Dina 22", bd=0, relief=GROOVE, command=lambda :btn_clicked('**'),activebackground="PeachPuff3",bg="PeachPuff2").pack(side=LEFT, expand=True, fill="both")

btn_decimal = Button(frame5, text=".", font="Dina 22", bd=0, relief=GROOVE, command=lambda :btn_clicked('.'), activebackground="PeachPuff3",bg="PeachPuff2").pack(side=LEFT, expand=True, fill="both")
btn0 = Button(frame5, text="0", font="Dina 22", bd=0, relief=GROOVE, command=lambda :btn_clicked(0), activebackground="PeachPuff3",bg="PeachPuff2").pack(side=LEFT, expand=True, fill="both")
btn_clear = Button(frame5, text="AC",font="Dina 20", bd=0, relief=GROOVE,command=btn_clear, activebackground="PeachPuff3",bg="PeachPuff2").pack(side=LEFT,expand=True,fill="both")
btn_add = Button(frame5, text="+   " , font="Dina 22", bd=0, relief=GROOVE, command=lambda :btn_clicked('+'),activebackground="PeachPuff3",bg="PeachPuff2").pack(side=LEFT, expand=True, fill="both")
btn_square =  Button(frame5, text='x\u00b2 ', font="Dina 22", bd=0, relief=GROOVE, command=lambda :btn_clicked('**2'), activebackground="PeachPuff3",bg="PeachPuff2").pack(side=LEFT, expand=True, fill="both")
btn_root =  Button(frame5, text='\u221A ', font="Dina 22", bd=0, relief=GROOVE, command=lambda :btn_clicked('\u221A('), activebackground="PeachPuff3",bg="PeachPuff2").pack(side=LEFT, expand=True, fill="both")

btn_pi = Button(frame6, text=PI, font="Dina 22", bd=0, relief=GROOVE, command=lambda :btn_clicked(math.pi), activebackground="PeachPuff3",bg="PeachPuff2").pack(side=LEFT, expand=True, fill="both")
btn_open_bracket = Button(frame6, text="(", font="Dina 22", bd=0, relief=GROOVE, command=lambda :btn_clicked('('),activebackground="PeachPuff3",bg="PeachPuff2").pack(side=LEFT, expand=True, fill="both")
btn_closed_bracket = Button(frame6, text=")", font="Dina 22", bd=0, relief=GROOVE, command=lambda :btn_clicked(')'), activebackground="PeachPuff3",bg="PeachPuff2").pack(side=LEFT, expand=True, fill="both")
btn_one_clear = Button(frame6, text="CE", font="Dina 20", bd=0, relief=GROOVE, command=btnAC, activebackground="PeachPuff3",bg="PeachPuff2").pack(side=LEFT, expand=True, fill="both")
btn_exp = Button(frame6, text="exp", font="Dina 22", bd=0, relief=GROOVE, command=lambda :btn_clicked('exp('), activebackground="PeachPuff3",bg="PeachPuff2").pack(side=LEFT, expand=True, fill="both")
btn_equal = Button(frame6, text= "=", font="Dina 22", bd=0, relief=GROOVE, command=result, activebackground="PeachPuff3",bg="PeachPuff2").pack(side=LEFT, expand=True, fill="both")


root.mainloop()
