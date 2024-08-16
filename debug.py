
import time
from plyer import notification
from email import message
from socket import timeout
import schedule

def aviso_sono():

    notification.notify(
        title = "ATENÇÃO, HORA DE BEBER ÁGUA!!",
        message = "BEBA 2 COPOS DE ÁGUA!!",
        #app_icon = "Icon_ico",
        timeout = 10
     )
    time.sleep(10)

schedule.every().day.at("19:49").do(aviso_sono)

while True:
    schedule.run_pending()