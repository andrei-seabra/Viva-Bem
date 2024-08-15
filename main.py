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
page = Canvas(window, width="405", height="655", bg="#F8F8F8")
page.pack()

# Bottom bar canvas
bottomBar = Canvas(window, width="405", height="65", bg="#DCDCDC")
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

    button = Button(bottomBar, image=buttonIcon, bd=0, anchor="center")
    button.grid(row=0, column=i, ipadx="3", ipady="3")

    button.image = buttonIcon # Avoids problems with iteration

    buttons.append(button)

bmiCalculator(page)

# Runs the window
window.mainloop()