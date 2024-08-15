from tkinter import *

# Interface

# Methods

def cleanCanvas(canvas: Canvas):
    """
        Deletes all the widgets of a given canvas.
    """

    widgets = canvas.find_all()

    for widget in widgets:
        canvas.delete(widget)

# Guis

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



def kcalCalculatorPage(canvas: Canvas = "page"):
    """
        Inserts the kcal calculator to the page canvas.
    """

    cleanCanvas(canvas)

    # References
    timer = PhotoImage(file="Assets/Images/Timer.png")
    symbol = PhotoImage(file="Assets/Images/BurnedCalories.png")
    playButton = PhotoImage(file="Assets/Images/PlayButton.png")
    pauseButton = PhotoImage(file="Assets/Images/PauseButton.png")

    sportsIcons = [
        "Assets/Images/WalkingButton.png",
        "Assets/Images/CyclingButton.png",
        "Assets/Images/RunningButton.png"
    ]

    # Sports canvas
    canvasSports = Canvas(canvas, width=303, height=75, bg="#F8F8F8")
    canvasSports.place(x=51, y=66)

    # Sports buttons
    buttons = []

    for i, icon in enumerate(sportsIcons):
        buttonIcon = PhotoImage(file=icon)

        button = Button(canvasSports, image=buttonIcon, bd=0, anchor="center")
        button.grid(row=0, column=i, ipadx=15)

        button.image = buttonIcon # Avoids problems with iteration

        buttons.append(button)

    # Timer display
    canvas.create_image(90, 235, anchor="nw", image=timer)
    canvas.timer = timer # Avoids calling function problems

    canvas.create_text(140, 250, anchor="nw", font=("Inter", 36), text="00:00") # Timer

    # Toogler buttton
    tooglerButton = Button(canvas, image=playButton, bd=0, anchor="nw")
    tooglerButton.place(x=158, y=417)
    canvas.playButton = playButton # Avoids calling function problems

    # Burned Kcal counter
    canvas.create_image(72, 543, anchor="nw", image=symbol)
    canvas.symbol = symbol # Avoids calling function problems

    canvas.create_text(134, 555, anchor="nw", font=("Inter", 28, "bold"), text="1.600 cal")



def bmiCalculatorPage(canvas: Canvas = "page"):
    """
        Inserts the bmi calculator to the page canvas.
    """
    
    cleanCanvas(canvas)

    # References
    entryImg = PhotoImage(file="Assets/Images/Entry.png") # Entry background
    buttonImg = PhotoImage(file="Assets/Images/CalculateButton.png") # Calculate button

    canvas.create_text(48, 100, anchor="nw", font=("Inter", 25, "bold"), text="Calculadora de IMC") # Title

    # Weight's and Height's entry
    entries = []

    entriesDict = {
        "Peso (kg)": [208, 235, 237.5],
        "Altura (m)": [315, 342, 344.5]
    }

    # Entry stuff
    for entry in entriesDict:
        canvas.create_text(88, entriesDict[entry][0], anchor="nw", font=("Inter", 16, "bold"), text=entry) # Entry title
    
        canvas.create_image(78, entriesDict[entry][1], anchor="nw", image=entryImg) # Entry image
        canvas.entryImg = entryImg # Avoids calling function problems

        guiEntry = Entry(canvas, bd=0, fg="black", font=("Inter", 20), highlightbackground="#DCDCDC", background="#DCDCDC")
        canvas.create_window(85, entriesDict[entry][2], anchor="nw", width=235, height=45, window=guiEntry) # Entry

        entries.append(guiEntry)

    # Button stuff
    calculateButton = Button(canvas, image=buttonImg, bd=0)
    canvas.create_window(121, 415, anchor="nw", width=165, height=55, window=calculateButton) # Calculate Button
    canvas.buttonImg = buttonImg # Avoids calling function problems



def goalPage(canvas: Canvas = "page"):
    """
        Inserts the goals to the page canvas.
    """

    cleanCanvas(canvas)

    # References
