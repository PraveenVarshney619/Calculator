from tkinter import *
from tkinter.tix import *
 
expression = ""
colorScheme = ["#bdd8f1"]
fontScheme = ["Arial", 20]

def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)

def equalpress(): 
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)

        expression = ""
    except: 
        equation.set(" error ")
        expression = ""

def BalloonEditions(element, message):
    MyObj = Balloon()
    MyObj.bind_widget(element, balloonmsg=message)

def hover(element):
    def function_on(event):
        element['bg'] = '#82a6cb'
    def function_off(event):
        element['bg'] = colorScheme

    element.bind("<Enter>", function_on)
    element.bind("<Leave>", function_off)

 
def clear():
    global expression
    expression = ""
    equation.set("Enter Your Expression")


if __name__ == "__main__":
   
    gui = Tk()
    gui.resizable(FALSE, FALSE)
    gui.configure(background=colorScheme)
    gui.title("Simple Calculator")


    equation = StringVar()
    expression_field = Entry(gui, textvariable=equation, borderwidth=6, font=['Calibri', 20])
    expression_field.grid(columnspan=4, ipadx=70, ipady=7)

    equation.set('Enter Your Expression')


    button1 = Button(gui, text=' 1 ', fg='black', bg=colorScheme, font=fontScheme, command=lambda: press(1), height=1, width=6)
    button1.grid(row=2, column=0)
    hover(button1)

    button2 = Button(gui, text=' 2 ', fg='black', bg=colorScheme, font=fontScheme, command=lambda: press(2), height=1, width=6)
    button2.grid(row=2, column=1)
    hover(button2)

    button3 = Button(gui, text=' 3 ', fg='black', bg=colorScheme, font=fontScheme, command=lambda: press(3), height=1, width=6)
    button3.grid(row=2, column=2)
    hover(button3)

    button4 = Button(gui, text=' 4 ', fg='black', bg=colorScheme, font=fontScheme, command=lambda: press(4), height=1, width=6)
    button4.grid(row=3, column=0)
    hover(button4)

    button5 = Button(gui, text=' 5 ', fg='black', bg=colorScheme, font=fontScheme, command=lambda: press(5), height=1, width=6)
    button5.grid(row=3, column=1)
    hover(button5)

    button6 = Button(gui, text=' 6 ', fg='black', bg=colorScheme, font=fontScheme, command=lambda: press(6), height=1, width=6)
    button6.grid(row=3, column=2)
    hover(button6)

    button7 = Button(gui, text=' 7 ', fg='black', bg=colorScheme, font=fontScheme, command=lambda: press(7), height=1, width=6)
    button7.grid(row=4, column=0)
    hover(button7)

    button8 = Button(gui, text=' 8 ', fg='black', bg=colorScheme, font=fontScheme, command=lambda: press(8), height=1, width=6)
    button8.grid(row=4, column=1)
    hover(button8)

    button9 = Button(gui, text=' 9 ', fg='black', bg=colorScheme, font=fontScheme, command=lambda: press(9), height=1, width=6)
    button9.grid(row=4, column=2)
    hover(button9)

    button0 = Button(gui, text=' 0 ', fg='black', bg=colorScheme, font=fontScheme, command=lambda: press(0), height=1, width=6)
    button0.grid(row=5, column=0)
    hover(button0)

    plus = Button(gui, text=' + ', fg='black', bg=colorScheme, font=fontScheme, command=lambda: press("+"), height=1, width=6)
    plus.grid(row=2, column=3)
    hover(plus)
    BalloonEditions(plus, 'Addition (+)\nAdds the Numbers')

    minus = Button(gui, text=' - ', fg='black', bg=colorScheme, font=fontScheme,command=lambda: press("-"), height=1, width=6)
    minus.grid(row=3, column=3)
    hover(minus)
    BalloonEditions(minus, 'Subtraction (-)\nSubtracts the Numbers')

    multiply = Button(gui, text=' × ', fg='black', bg=colorScheme, font=fontScheme,   command=lambda: press("*"), height=1, width=6)
    multiply.grid(row=4, column=3)
    hover(multiply)
    BalloonEditions(multiply, 'Multiplication (×)\nMultiplies the Numbers')

    divide = Button(gui, text=' ÷ ', fg='black', bg=colorScheme, font=fontScheme, command=lambda: press("/"), height=1, width=6)
    divide.grid(row=5, column=3)
    hover(divide)
    BalloonEditions(divide, 'Division (÷)\nDivides the Numbers')

    modulo = Button(gui, text=' % ', fg='black', bg=colorScheme, font=fontScheme, command=lambda: press("%"), height=1, width=6)
    modulo.grid(row=5, column=2)
    hover(modulo)
    BalloonEditions(modulo, 'Modulo (%)\nGives The Modulo of the Numbers')


    Decimal= Button(gui, text='.', fg='black', bg=colorScheme, font=fontScheme, command=lambda: press('.'), height=1, width=6)
    Decimal.grid(row=5, column=1)
    hover(Decimal)
    BalloonEditions(Decimal, 'Decimal Point (.)\nAdds a Decimal Point')

    equal = Button(gui, text=' = ', fg='black', bg=colorScheme, font=fontScheme,command=equalpress, height=1, width=13)
    equal.grid(row=6, column=0, columnspan=2)
    hover(equal)
    BalloonEditions(equal, 'Equal (=)\nSign to Perform Operation')

    clear = Button(gui, text='Clear', fg='black', bg=colorScheme, font=fontScheme,command=clear, height=1, width=13)
    clear.grid(row=6, column=2, columnspan=2)
    hover(clear)
    BalloonEditions(clear, 'Clear\nClears All')

    gui.mainloop()