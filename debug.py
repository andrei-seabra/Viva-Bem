from schedule import every, run_pending
from plyer import notification

from tkinter import *
from tkinter import ttk

window = Tk()

def snoozerNotification():
    """
        Notifies the user to sleep and turn off the computer.
    """
    
    # References
    icon = "Assets/Images/Icon.ico"
    cooldown = 3600 # 1h

    # Notification system
    notification.notify(title = "Viva Bem", message = "Hora de dormir, desligue o seu computador.", app_icon = icon, timeout = 30)



def snoozerNotificationsStarter(window: Tk, hour: str = "22:00"):
    every().day.at(hour).do(snoozerNotification)

    def scheduleChecker():
        run_pending()
        window.after(1000, scheduleChecker)

    scheduleChecker()

snoozerNotificationsStarter(window=window, hour="13:16")

window.mainloop()