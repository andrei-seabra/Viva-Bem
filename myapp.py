from tkinter import *

# Interface methods

def cleanCanvas(canvas: Canvas):
    """
        Deletes all the widgets of a given canvas.
    """

    widgets = canvas.find_all()

    for widget in widgets:
        canvas.delete(widget)

def homePage(canvas: Canvas = "page"):
    """
        Inserts the home page to the page canvas.
    """

    cleanCanvas(canvas)

    icon = PhotoImage(file="Assets/Images/Icon.png")
    canvas.create_image(250, 107, anchor="nw", image=icon) # App icon
    canvas.icon = icon # Avoids calling function problems

    canvas.create_text(32, 147, anchor="nw", font=("Inter", 30, "bold"), text="Viva Bem") # App name
    canvas.create_text(24, 233, anchor="nw", font=("Inter", 18), text="Seja bem-vindo(a), ") # App title
    canvas.create_text(24, 270, anchor="nw", font=("Inter", 15), text="ao aplicativo que te mantém em forma!") # App title

def kcalCalculatorPage():
    ...

def bmiCalculator(canvas: Canvas = "page"):
    """
        Inserts the bmi calculator to the page canvas.
    """
    
    cleanCanvas(canvas)

    # references
    entryImg = PhotoImage(file="Assets/Images/Entry.png") # Entry background
    buttonImg = PhotoImage(file="Assets/Images/CalculateButton.png") # Calculate button

    canvas.create_text(48, 100, anchor="nw", font=("Inter", 25, "bold"), text="Calculadora de IMC") # Title

    # Weight stuff
    canvas.create_text(88, 208, anchor="nw", font=("Inter", 16, "bold"), text="Peso (kg)") # Weight's entry title
    
    canvas.create_image(78, 235, anchor="nw", image=entryImg) # Weight's entry image
    canvas.entryImg = entryImg # Avoids calling function problems

    weightEntry = Entry(canvas, border=8, bd=0, fg="black", font=("Inter", 20), highlightbackground="#DCDCDC", background="#DCDCDC")
    canvas.create_window(85, 237.5, anchor="nw", width=235, height=45, window=weightEntry) # Weight's entry

    # Height stuff
    canvas.create_text(88, 315, anchor="nw", font=("Inter", 16, "bold"), text="Altura (m)") # Height's entry title

    canvas.create_image(78, 342, anchor="nw", image=entryImg) # Weight's entry image
    canvas.entryImg = entryImg # Avoids calling function problems

    heightEntry = Entry(canvas, border=8, bd=0, fg="black", font=("Inter", 20), highlightbackground="#DCDCDC", background="#DCDCDC")
    canvas.create_window(85, 344.5, anchor="nw", width=235, height=45, window=heightEntry) # Height's entry

    # Button stuff
    calculateButton = Button(canvas, image=buttonImg, bd=0)
    canvas.create_window(121, 415, anchor="nw", width=165, height=55, window=calculateButton) # Calculate Button
    canvas.buttonImg = buttonImg # Avoids calling function problems