# Libraries used in the project
from tkinter import *
from myapp import *

# Creates the window's app
window = Tk()

# Window format
window.title("Viva Bem")
window.iconbitmap("Assets/Images/Icon.ico")
window.geometry("405x720")

# Page canvas
page = Canvas(window, width=405, height=655, bg="#F8F8F8")
page.pack()

# Bottom bar canvas
bottomBar = Canvas(window, width=405, height=65, bg="#DCDCDC")
bottomBar.pack()

# Bottom Bar Buttons
buttons = []

icons = [
    "Assets/Images/Home.png",
    "Assets/Images/Calories.png",
    "Assets/Images/Calculator.png",
    "Assets/Images/Goal.png",
    "Assets/Images/Recipes.png",
    "Assets/Images/Clock.png"
]

# The adition of the bottom bar buttons
for i, icon in enumerate(icons):
    buttonIcon = PhotoImage(file=icon)

    button = Button(bottomBar, anchor="center", bd=0, image=buttonIcon)
    button.grid(row=0, column=i, ipadx=3, ipady=3)

    button.image = buttonIcon # Avoids problems with iteration

    buttons.append(button)

# Bottom bar buttons configuration
buttons[0].configure(command=lambda canvas=page: homePage(canvas)) # Home page button
buttons[1].configure(command=lambda canvas=page: kcalCalculatorPage(canvas)) # Kcal calculator button
buttons[2].configure(command=lambda canvas=page: bmiCalculatorPage(canvas)) # Bmi calculator button
buttons[3].configure(command=lambda canvas=page: goalPage(canvas)) # Goal page button
buttons[4].configure(command=lambda canvas=page: recipesPage(canvas)) # Recipes button
buttons[5].configure(command=lambda canvas=page: snoozerPage(canvas)) # Snoozer page button

# Initializations

# Home page
homePage(page)

# Water notifications
waterNotification(window)

# Sleep notifications
snoozerNotificationsStarter(window=window, hour="13:18")

# Runs the window
window.mainloop()