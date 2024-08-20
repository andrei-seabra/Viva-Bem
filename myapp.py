# Libries used in myapp library
from schedule import every, run_pending
from plyer import notification

from random import choice

from tkinter import *
from tkinter import ttk

# Back-end

# Calculations

def bmiCalculator(weight: str, height: str, canvas: Canvas, resultDisplay: Canvas.create_text):
    """
        Calculates the bmi of the user based on their information.
    """

    # References
    formatedMagnitudes = []
    
    acceptableCharacters = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ",", "."]
    magnitudes = [weight, height]

    # Avoids other characters in magnitudes which aren't related to numbers or blank spaces
    for magnitude in magnitudes:
        if magnitude == "":
            canvas.itemconfig(resultDisplay, text="Os dados são inválidos.")
            return
        else:
            for char in magnitude:
                if not char  in acceptableCharacters:
                    canvas.itemconfig(resultDisplay, text="Os dados são inválidos.")
                    return
            
    # Treat the information
    for magnitude in magnitudes:
        if "," in magnitude:
            formatedMagnitude = float(magnitude.replace(",","."))
            formatedMagnitudes.append(formatedMagnitude)
        else:
            formatedMagnitude = float(magnitude)
            formatedMagnitudes.append(formatedMagnitude)

    # Calculation
    bmi = formatedMagnitudes[0] / formatedMagnitudes[1] ** 2
    
    result = ""

    if bmi < 18.5:
        result = " Você está abaixo \n   do peso ideal."
    elif bmi < 25:
        result = "Você está no peso ideal."
    elif bmi < 30:
        result = "Você está sobrepeso."
    elif bmi < 40:
        result = "Você está com obesidade."
    else:
        result = "   Você está com \nobesidade mórbida."
    
    canvas.itemconfig(resultDisplay, text=result)



# Timer

# References
time = 0
isRunning = False

def timerHandler(canvas: Canvas, timerDisplay: Canvas.create_text, window: Tk):
    global time, isRunning

    if isRunning:
        # Displays the time
        canvas.itemconfig(timerDisplay, text=f"{(time // 60):02}:{(time % 60):02}")

        time += 1
        
        window.after(1000, timerHandler, canvas, timerDisplay, window)

def timerStarter(canvas: Canvas, timerDisplay: Canvas.create_text, button: Button, pauseIcon: PhotoImage, playIcon: PhotoImage, window: Tk, kcalCounter: Canvas.create_text):
    """
        Runs/stops the timer.
    """
        
    global time, isRunning, currentTime

    if isRunning:
        kcalCalculator(canvas, kcalCounter)

        # Changes the button image
        button.config(image=playIcon)

        # Control variable
        isRunning = False

        # Inicializes the timer
        timerHandler(canvas, timerDisplay, window)

    else:
        # Resets the timer
        time = 0

        # Changes the button image
        button.config(image=pauseIcon)

        # Control variable
        isRunning = True

        # Inicializes the timer
        timerHandler(canvas, timerDisplay, window)

# Sports Chooser

# References
currentSport = "walking"

def sportHandler(sport):
    global currentSport
    
    currentSport = sport

def setBurnedKcal(burnedKcal: str):
    # References
    kcal = 0
    total = 0

    # Reads the data
    with open("Assets/Data/kcalData.txt", "r") as file:
        kcal = int(file.read())

    # Writes the data
    with open("Assets/Data/kcalData.txt", "w") as file:
        total = kcal + int(burnedKcal)

        file.write(str(total))


def kcalCalculator(canvas: Canvas, kcalCounter: Canvas.create_text):
    """
        Calculates the kcal burned by the user based on their information.
    """
    global time

    # Control variable
    kcalBurnedPerMin = 0

    # Checks which sport the user is practicing
    if currentSport == "cycling":
        kcalBurnedPerMin = 4
    elif currentSport == "walking":
        kcalBurnedPerMin = 6
    else:
        kcalBurnedPerMin = 10

    # Calculation
    minutes = time / 60
    
    kcalBurned = minutes * kcalBurnedPerMin
    
    setBurnedKcal(str(round(kcalBurned)))

    canvas.itemconfig(kcalCounter, text=f"{round(kcalBurned)} cal")



# Goal handlers

def setGoal(goal: str, canvas: Canvas, window: Tk):
    acceptableCharacters = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    # Avoids other characters in goal which aren't related to numbers or blank spaces
    if goal == "" or goal == "0":
        alert = canvas.create_text(85, 410, anchor="nw", font=("Inter", 16, "bold"), text="Os dados são inválidos.")
        window.after(2000, lambda: canvas.delete(alert))
        return
    else:
        for char in goal:
            if not char  in acceptableCharacters:
                alert = canvas.create_text(85, 410, anchor="nw", font=("Inter", 16, "bold"), text="Os dados são inválidos.")
                window.after(2000, lambda: canvas.delete(alert))
                return

    # Writes the data
    with open("Assets/Data/goalData.txt", "w") as file:
        file.write(goal)

    goalPage(canvas, window) # Returns to the main page

def getGoal():
    # References
    goal = ""

    # Read of the data
    with open("Assets/Data/goalData.txt", "r") as file:
        goal = file.read()
    
    return goal

def getBurnedKcal():
    burnedKcal = ""
    # Read of the data
    with open("Assets/Data/kcalData.txt", "r") as file:
        burnedKcal = file.read()
    
    return burnedKcal

# Percent
def percentHandler(burnedKcal: str, goal: str):
    # Avoids division by zero
    if goal == "0":
        return "0%"
    
    return f"{round((int(burnedKcal) / int(goal)) * 100)}%"



# Meal selector

def getRandomMeal(canvas: Canvas, recipeText: Canvas.create_text, meal: str):
    """
        Gets a random meal based on the meal time.
    """

    # References
    breakfast = [
        "Smoothie Verde:\n- Banana\n- Espinafre\n- Iorgute natural\n- Leite\n- Mel",
        "Omelete:\n- 2 ovo\n- Espinafre\n- Tomate",
        "Mingau de aveia:\n- Mingau\n- Aveia",
        "Brownie de banana:\n- Banana\n- Pasta de amendoim\n- Aveia",
        "Shake de banana:\n- Iorgute natural\n- Banana\n- Aveia"
    ]

    lunchDinner = [
        "Escondidinho de frango:\n- Peito de frango\n- Cebola\n- 2 dentes de alho\n- Tomate\n- Pimetão\n- Milho",
        "Tacos de feijão:\n- Feijão preto\n- Milho\n- Tomate\n- Cebola\n- 4 tortilhas integrais",
        "Espaguete de abobrinha:\n- 2 abobrinhas\n- Molho de tomate\n- 1 dente de alho",
        "Nhoque de abobrinha:\n- 2 abobrinhas\n- Farinha de trigo\n- Ovo\n- Queijo\n- 1 dente de alho",
        "Salmão:\n- Filé de salmão\n- Espinafre",
        "Ratatouille de legumes:\n- Berinjela\n- Abobrinha\n- Pimentão\n- Tomate\n- Cebola\n- 2 dentes de alho",
        "Frango grelhado:\n- Peito de frango\n- Brocólis",
        "Sopa de lentilha:\n- Lentilha\n- Cenoura\n- Cebola\n- 1 dente de alho",
        "Salada de atum:\n- Lata de atum\n- Milho\n- Tomate\n- Cebola roxa",
        "Salada de grão-de-bico:\n- Grão-de-bico\n- Tomate\n- Pepino\n- Cebola roxa"
    ]

    # The meal presented in the screen
    randomMeal = ""

    # Checks which meal time was selected
    if meal == "breakfast":
        randomMeal = choice(breakfast)
    else:
        randomMeal = choice(lunchDinner)

    # Displays it
    canvas.itemconfig(recipeText, text=randomMeal)

# Notifications

def waterNotification(window: Tk):
    """
        Notifies the user to drink water.
    """

    # References
    icon = "Assets/Images/Icon.ico"
    cooldown = 3600 # 1h

    # Notification system
    notification.notify(title = "Viva Bem", message = "Beba 2 copos de água.", app_icon = icon, timeout = 10)

    window.after(cooldown * 1000, waterNotification) # Runs it in a loop



def snoozerNotification():
    """
        Notifies the user to sleep and turn off the computer.
    """
    
    # References
    icon = "Assets/Images/Icon.ico"

    # Notification system
    notification.notify(title = "Viva Bem", message = "Hora de dormir, desligue o seu computador.", app_icon = icon, timeout = 30)

def snoozerNotificationsStarter(window: Tk, hour: str):
    every().day.at(hour).do(snoozerNotification)

    def scheduleChecker():
        run_pending()
        window.after(1000, scheduleChecker)

    scheduleChecker()



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



def kcalCalculatorPage(canvas: Canvas, window: Tk):
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
    sportsCanvas = Canvas(canvas, width=303, height=77, bg="#F8F8F8")
    canvas.create_window(51, 66, anchor="nw", width=303, height=77, window=sportsCanvas)

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

        button = Button(sportsCanvas, anchor="center", bd=0, bg="#F8F8F8", image=buttonIcon)
        button.grid(row=0, column=i, ipadx=13)

        button.image = buttonIcon # Avoids problems with iteration

        buttons.append(button)

    # Buttons configuration
    buttons[0].configure(command=lambda: sportHandler("walking"))
    buttons[1].configure(command=lambda: sportHandler("cycling"))
    buttons[2].configure(command=lambda: sportHandler("running"))

    # Timer display
    canvas.create_image(90, 235, anchor="nw", image=timer)
    canvas.timer = timer # Avoids calling function problems

    timerDisplay = canvas.create_text(140, 250, anchor="nw", font=("Inter", 36), text="00:00") # Timer

    # Kcal counter
    kcalCounter = canvas.create_text(134, 555, anchor="nw", font=("Inter", 28, "bold"), text="0 cal")

    # Toogler buttton
    tooglerButton = Button(canvas, anchor="nw", bd=0, bg="#F8F8F8", image=playButton, command=lambda: timerStarter(canvas, timerDisplay, tooglerButton, pauseButton, playButton, window, kcalCounter))
    canvas.create_window(158, 417, anchor="nw", width=90, height=90, window=tooglerButton)
    canvas.playButton = playButton # Avoids calling function problems

    # Burned Kcal counter
    canvas.create_image(72, 543, anchor="nw", image=symbol)
    canvas.symbol = symbol # Avoids calling function problems



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

    # Result display
    resultDisplay = canvas.create_text(79, 551, anchor="nw", font=("Inter", 17), text="")

    # Calculate button
    calculateButton = Button(canvas, bd=0, image=buttonImg, command=lambda: bmiCalculator(entries[0].get(), entries[1].get(), canvas, resultDisplay))
    canvas.create_window(121, 415, anchor="nw", width=165, height=55, window=calculateButton) # Calculate Button
    canvas.buttonImg = buttonImg # Avoids calling function problems



# Goal configuration

def setGoalPage(canvas: Canvas, window: Tk):
    """
        Inserts the page to set the user's goal.
    """

    cleanCanvas(canvas)

    # References
    background = PhotoImage(file="Assets/Images/Entry.png")
    setButton = PhotoImage(file="Assets/Images/SetButton.png")

    # Title
    canvas.create_text(125, 113, anchor="nw", font=("Inter", 24, "bold"), text="Nova meta")

    # Entry
    canvas.create_text(100, 312, anchor="nw", font=("Inter", 12, "bold"), text="Meta de queima de calorias") # Title

    canvas.create_image(78, 342, anchor="nw", image=background) # Background image
    canvas.background = background # Avoids calling function problems

    entry = Entry(canvas, bd=0, fg="black", font=("Inter", 20), highlightbackground="#D9D9D9", background="#D9D9D9")
    canvas.create_window(78, 342, anchor="nw", width=250, height=55, window=entry) # Entry

    button = Button(canvas, bd=0, image=setButton, bg="#F8F8F8", command=lambda: setGoal(entry.get(), canvas, window))
    canvas.create_window(114, 525, anchor="nw", width=165, height=55, window=button)

    canvas.setButton = setButton # Avoids calling function problems

def goalPage(canvas: Canvas, window:Tk):
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
    canvas.create_text(171, 325, anchor="nw", font=("Inter", 36, "bold"), text=f"{percentHandler(getBurnedKcal(), getGoal())}") # Percentage display
    canvas.create_text(110, 376, anchor="nw", font=("Inter", 24, "bold"), text=(f"{int(getBurnedKcal()):,.0f} / {int(getGoal()):,.0f}").replace(",", ".")) # Total display

    # Add new goal button
    button = Button(canvas, bd=0, image=add, bg="#F8F8F8", command=lambda: setGoalPage(canvas, window))
    canvas.create_window(158, 505, anchor="nw", width=90, height=90, window=button) # New goal button
    canvas.add = add # Avoids calling function problems



def recipesPage(canvas: Canvas):
    """
        Inserts the recipes to the page canvas.
    """
    
    cleanCanvas(canvas)

    # Title
    canvas.create_text(128, 125, anchor="nw", font=("Inter", 28, "bold"), text="Receitas")

    # Meal button canvas
    canvasMeals = Canvas(canvas, width=246, height=75, bg="#F8F8F8")
    canvas.create_window(45, 250, anchor="nw", window=canvasMeals)

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
    recipeText = canvas.create_text(43, 376, anchor="nw", font=("Inter", 18)) # Recipe
    
    # Buttons configuration
    buttons[0].config(command=lambda: getRandomMeal(canvas, recipeText, "breakfast"))
    buttons[1].config(command=lambda: getRandomMeal(canvas, recipeText, "lunchDinner"))


def snoozerPage(canvas: Canvas, window: Tk):
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

    timerDisplay = canvas.create_text(140, 275, anchor="nw", font=("Inter", 36), text="22:00") # Timer

    # New alarm button
    button = Button(canvas, bd=0, image=snooze, bg="#F8F8F8", command=lambda: setHour(options, canvas, timerDisplay, window))
    canvas.create_window(53, 459, anchor="nw", width=75, height=75, window=button)
    canvas.snooze = snooze # Avoids calling function problems
    
    # Alarm options
    hours = [
        "18:00",
        "19:00",
        "20:00",
        "21:00",
        "22:00",
        "23:00"
    ]
    
    # Combobox
    options = ttk.Combobox(canvas, state="readonly", background="#666666", font=("Inter", 20, "bold"), justify="center", values=hours)
    canvas.create_window(140, 470, anchor="nw", width=225, height=50, window=options)

# Snoozer configuration

# References
currentHour = ""

def setHour(comboBox: ttk.Combobox, canvas: Canvas, timerDisplay: Canvas.create_text, window: Tk):
    """
        Sets the hour of the snoozer.
    """
    global currentHour

    currentHour = comboBox.get()

    canvas.itemconfig(timerDisplay, text=currentHour)
    snoozerNotificationsStarter(window, currentHour)