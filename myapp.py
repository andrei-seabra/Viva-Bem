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
    canvas.create_image(250, 32, anchor="nw", image=icon) # App icon
    canvas.icon = icon # Avoids calling function problems

    logo = PhotoImage(file="Assets/Images/Logo.png")
    canvas.create_image(78, 291, anchor="nw", image=logo) # App logo
    canvas.logo = logo # Avoids calling function problems

    canvas.create_text(32, 72, anchor="nw", font=("Inter", 30, "bold"), text="Viva Bem") # App name
    canvas.create_text(24, 160, anchor="nw", font=("Inter", 18), text="Seja bem-vindo(a), ") # App title
    canvas.create_text(24, 195, anchor="nw", font=("Inter", 15), text="ao aplicativo que te mantém em forma!") # App title