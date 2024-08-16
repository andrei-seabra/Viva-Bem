# Libries used in myapp library
from tkinter import *
from tkinter import ttk

# Back-end


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

def homePage(canvas: Canvas):
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



def kcalCalculatorPage(canvas: Canvas):
    """
        Inserts the kcal calculator to the page canvas.
    """

    cleanCanvas(canvas)

    # References
    timer = PhotoImage(file="Assets/Images/Timer.png")
    symbol = PhotoImage(file="Assets/Images/BurnedCalories.png")
    playButton = PhotoImage(file="Assets/Images/PlayButton.png")
    pauseButton = PhotoImage(file="Assets/Images/PauseButton.png")

    # Sports canvas
    canvasSports = Canvas(canvas, width=303, height=77, bg="#F8F8F8")
    canvas.create_window(51, 66, anchor="nw", width=303, height=77, window=canvasSports)

    # Sports buttons
    buttons = []

    sportsIcons = [
        "Assets/Images/WalkingButton.png",
        "Assets/Images/CyclingButton.png",
        "Assets/Images/RunningButton.png"
    ]

    # The adition of the sports buttons
    for i, icon in enumerate(sportsIcons):
        buttonIcon = PhotoImage(file=icon)

        button = Button(canvasSports, anchor="center", bd=0, bg="#F8F8F8", image=buttonIcon)
        button.grid(row=0, column=i, ipadx=13)

        button.image = buttonIcon # Avoids problems with iteration

        buttons.append(button)

    # Timer display
    canvas.create_image(90, 235, anchor="nw", image=timer)
    canvas.timer = timer # Avoids calling function problems

    canvas.create_text(140, 250, anchor="nw", font=("Inter", 36), text="00:00") # Timer

    # Toogler buttton
    tooglerButton = Button(canvas, anchor="nw", bd=0, bg="#F8F8F8", image=playButton)
    canvas.create_window(158, 417, anchor="nw", width=90, height=90, window=tooglerButton)
    canvas.playButton = playButton # Avoids calling function problems

    # Burned Kcal counter
    canvas.create_image(72, 543, anchor="nw", image=symbol)
    canvas.symbol = symbol # Avoids calling function problems

    canvas.create_text(134, 555, anchor="nw", font=("Inter", 28, "bold"), text="1.600 cal")



def bmiCalculatorPage(canvas: Canvas):
    """
        Inserts the bmi calculator to the page canvas.
    """
    
    cleanCanvas(canvas)

    # References
    entryImg = PhotoImage(file="Assets/Images/Entry.png") # Entry background
    buttonImg = PhotoImage(file="Assets/Images/CalculateButton.png") # Calculate button

    # Title
    canvas.create_text(48, 100, anchor="nw", font=("Inter", 25, "bold"), text="Calculadora de IMC")

    # Weight's and height's entry
    entries = []

    entriesDict = {
        "Peso (kg)": [208, 235, 237.5],
        "Altura (m)": [315, 342, 344.5]
    }

    # The adition of the weight/height entries
    for entry in entriesDict:
        canvas.create_text(88, entriesDict[entry][0], anchor="nw", font=("Inter", 16, "bold"), text=entry) # Entry title
    
        canvas.create_image(78, entriesDict[entry][1], anchor="nw", image=entryImg) # Entry image
        canvas.entryImg = entryImg # Avoids calling function problems

        guiEntry = Entry(canvas, bd=0, fg="black", font=("Inter", 20), highlightbackground="#DCDCDC", background="#DCDCDC")
        canvas.create_window(85, entriesDict[entry][2], anchor="nw", width=235, height=45, window=guiEntry) # Entry

        entries.append(guiEntry)

    # Calculate button
    calculateButton = Button(canvas, bd=0, image=buttonImg)
    canvas.create_window(121, 415, anchor="nw", width=165, height=55, window=calculateButton) # Calculate Button
    canvas.buttonImg = buttonImg # Avoids calling function problems



def goalPage(canvas: Canvas):
    """
        Inserts the goals to the page canvas.
    """

    cleanCanvas(canvas)

    # References
    flag = PhotoImage(file="Assets/Images/Flag.png")
    add = PhotoImage(file="Assets/Images/AddButton.png")

    # Title
    canvas.create_text(145, 137, anchor="nw", font=("Inter", 40, "bold"), text="Meta")

    # Flag image
    canvas.create_image(75, 309, anchor="nw", image=flag)
    canvas.flag = flag # Avoids calling function problems

    # Results text
    canvas.create_text(171, 325, anchor="nw", font=("Inter", 36, "bold"), text="100%") # Percentage display
    canvas.create_text(110, 376, anchor="nw", font=("Inter", 24, "bold"), text="10.000 / 10.000") # Total display

    # Add new goal button
    button = Button(canvas, bd=0, image=add, bg="#F8F8F8")
    canvas.create_window(158, 505, anchor="nw", width=90, height=90, window=button) # New goal button
    canvas.add = add # Avoids calling function problems



def recipesPage(canvas: Canvas):
    """
        Inserts the recipes to the page canvas.
    """
    ...
    cleanCanvas(canvas)

    # References
    reloadIcon = PhotoImage(file="Assets/Images/ReloadButton.png")

    # Title
    canvas.create_text(128, 125, anchor="nw", font=("Inter", 28, "bold"), text="Receitas")

    # Meal button canvas
    canvasMeals = Canvas(canvas, width=246, height=75, bg="#F8F8F8")
    canvas.create_window(45, 182, anchor="nw", window=canvasMeals)

    # Meal buttons
    buttons = []

    mealIcons = [
        "Assets/Images/BreakfastButton.png",
        "Assets/Images/LunchButton.png"
    ]

    # The adition of the meal buttons
    for i, icon in enumerate(mealIcons):
        buttonIcon = PhotoImage(file=icon)

        button = Button(canvasMeals, anchor="center", bd=0, bg="#F8F8F8", image=buttonIcon)
        button.grid(row=0, column=i, ipadx=42.5)

        button.image = buttonIcon # Avoids problems with iteration

        buttons.append(button)

    # Recipe text
    canvas.create_text(43, 308, anchor="nw", font=("Inter", 18, "bold"), text="Omele: \n - 2 ovos \n - 2 fatias de queijo \n - 1 fio de óleo") # Recipe

    # Reload meal button
    reloadButton = Button(canvas, bd=0, bg="#F8F8F8", image=reloadIcon)
    canvas.create_window(173, 562, anchor="nw", width=60, height=60, window=reloadButton)
    canvas.reloadIcon = reloadIcon


def snoozerPage(canvas: Canvas):
    """
        Inserts the snoozer to the page canvas.
    """

    cleanCanvas(canvas)

    # References
    timer = PhotoImage(file="Assets/Images/Timer.png")
    snooze = PhotoImage(file="Assets/Images/SnoozeButton.png")

    # Title
    canvas.create_text(40, 122, anchor="nw", font=("Inter", 27, "bold"), text="Regulador de sono")

    # Timer display
    canvas.create_text(140, 235, anchor="nw", font=("Inter", 16, "bold"), text="Alarme atual") # Timer title

    canvas.create_image(90, 260, anchor="nw", image=timer)
    canvas.timer = timer # Avoids calling function problems

    canvas.create_text(140, 275, anchor="nw", font=("Inter", 36), text="22:00") # Timer

    # New alarm button
    button = Button(canvas, bd=0, image=snooze, bg="#F8F8F8")
    canvas.create_window(53, 459, anchor="nw", width=75, height=75, window=button)
    canvas.snooze = snooze # Avoids calling function problems
    
    # Alarm options
    options = ttk.Combobox(canvas, state="readonly", background="#666666", font=("Inter", 10, "bold"), justify="center")
    canvas.create_window(140, 470, anchor="nw", width=225, height=50, window=options)