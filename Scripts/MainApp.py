import math
import tkinter as tk

firstNumber=secondNumber=sign=None


def GetDigit(digit):
    print(digit)
    current = screen["text"]
    new = current + str(digit)
    screen.config(text=new)

def performAction(x):
    global firstNumber, sign
    firstNumber = int(screen["text"])
    sign = x
    screen.config(text="")

def Clear():
    screen.config(text="")

def Sqrt():
    global firstNumber
    firstNumber = int(screen["text"])
    result = math.sqrt(firstNumber)
    result = float(result)
    screen.config(text=result)

def Equal():
    global firstNumber, secondNumber, sign
    secondNumber = int(screen["text"])

    if sign == "+":
        result = firstNumber + secondNumber
        screen.config(text=result)
    elif sign == "-":
        result = firstNumber - secondNumber
        screen.config(text=result)
    elif sign == "*":
        result = firstNumber * secondNumber
        screen.config(text=result)
    elif sign == "/":
        result = firstNumber / secondNumber
        result = float(result)
        screen.config(text=result)
    elif sign == "pow":
        result = math.pow(firstNumber,secondNumber) 
        result = int(result)
        screen.config(text=result)
    
#Creating the GUI
r = tk.Tk()
r.configure(bg="black")
r.title("Calculator")

screen = tk.Label(r, width=20, height=3, text="", fg="white", bg="black", font=("Helvetica", 12, "bold italic"))
r.resizable(False,False)

one = tk.Button(r, text="1", width=10, height=3, bg="black", fg="white", font=("Helvetica", 12, "bold italic"),command=lambda :GetDigit(1))
two = tk.Button(r, text="2", width=10, height=3, bg="black", fg="white", font=("Helvetica", 12, "bold italic"),command=lambda :GetDigit(2))
three = tk.Button(r, text="3", width=10, height=3, bg="black", fg="white", font=("Helvetica", 12, "bold italic"),command=lambda :GetDigit(3))
four = tk.Button(r, text="4", width=10, height=3, bg="black", fg="white", font=("Helvetica", 12, "bold italic"),command=lambda :GetDigit(4))
five = tk.Button(r, text="5", width=10, height=3, bg="black", fg="white", font=("Helvetica", 12, "bold italic"),command=lambda :GetDigit(5))
six = tk.Button(r, text="6", width=10, height=3, bg="black", fg="white", font=("Helvetica", 12, "bold italic"),command=lambda :GetDigit(6))
seven = tk.Button(r, text="7", width=10, height=3, bg="black", fg="white", font=("Helvetica", 12, "bold italic"),command=lambda :GetDigit(7))
eight = tk.Button(r, text="8", width=10, height=3, bg="black", fg="white", font=("Helvetica", 12, "bold italic"),command=lambda :GetDigit(8))
nine = tk.Button(r, text="9", width=10, height=3, bg="black", fg="white", font=("Helvetica", 12, "bold italic"),command=lambda :GetDigit(9))

addButton = tk.Button(r, text="+", width=10, height=3, bg="black", fg="white", font=("Helvetica", 12, "bold italic"),command=lambda :performAction("+"))
subtractButton = tk.Button(r, text="-", width=10, height=3, bg="black", fg="white", font=("Helvetica", 12, "bold italic"),command=lambda :performAction("-"))
multButton = tk.Button(r, text="*", width=10, height=3, bg="black", fg="white", font=("Helvetica", 12, "bold italic"),command=lambda :performAction("*"))
divButton = tk.Button(r, text="/", width=10, height=3, bg="black", fg="white", font=("Helvetica", 12, "bold italic"),command=lambda :performAction("/"))
powButton = tk.Button(r, text="^x", width=10, height=3, bg="black", fg="white", font=("Helvetica", 12, "bold italic"),command=lambda :performAction("pow"))
sqrtButton = tk.Button(r, text="sqrt", width=10, height=3, bg="black", fg="white", font=("Helvetica", 12, "bold italic"),command=lambda :Sqrt())
equalButton = tk.Button(r, text="=", width=20, height=3, bg="black", fg="white", font=("Helvetica", 12, "bold italic"),command=lambda :Equal())
clearButton = tk.Button(r, text="C", width=10, height=3, bg="black", fg="white", font=("Helvetica", 12, "bold italic"),command=lambda :Clear())
quitButton = tk.Button(r, text="QUIT", width=20, height=3, bg="black", fg="white", font=("Helvetica", 12, "bold italic"),command=r.destroy)

#Grid placement
screen.grid(row=0, column=0, columnspan=2)
one.grid(row=1, column=0)
two.grid(row=1, column=1)
three.grid(row=1, column=2)
four.grid(row=2, column=0)
five.grid(row=2, column=1)
six.grid(row=2, column=2)
seven.grid(row=3, column=0)
eight.grid(row=3, column=1)
nine.grid(row=3, column=2)


addButton.grid(row=1, column=3, columnspan=1)
subtractButton.grid(row=2, column=3, columnspan=1)
multButton.grid(row=1, column=4, columnspan=1)
divButton.grid(row=2, column=4, columnspan=1)
sqrtButton.grid(row=3, column=3, columnspan=1)
powButton.grid(row=3, column=4, columnspan=1)
equalButton.grid(row=4, column=3, columnspan=2, sticky="ew")
clearButton.grid(row=4, column=0, columnspan=1)
quitButton.grid(row=4, column=1, columnspan=2, sticky="ew")
r.mainloop()
