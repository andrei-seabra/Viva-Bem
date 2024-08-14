import time
from plyer import notification
from email import message
from socket import timeout

while True:
    notification.notify(
        title = "ATENÇÃO, HORA DE BEBER ÁGUA!!",
        message = "BEBA 2 COPOS DE ÁGUA!!",
        #app_icon = "Icon_ico",
        timeout = 10
     )
    time.sleep(10)