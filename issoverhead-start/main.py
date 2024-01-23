import requests
from datetime import datetime
import smtplib
import time
#
MY_LAT = 51.507351 # Your latitude
MY_LONG = -0.127758 # Your longitude

MY_EMAIL = "**********"
PASSWD = "***********"

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now().hour
    if time_now in range(sunset, sunrise):
        return True

def iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    if iss_longitude+5 == MY_LONG or iss_longitude-5 == MY_LONG and iss_latitude+5 == MY_LAT or iss_latitude-5 == MY_LAT:
        return True

while True:
    time.sleep(60)
    if iss_overhead() and is_night():
        with smtplib.SMTP("smtp-mail.") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs="***********",
                                msg=f"Subject:ISS ABOVE YOU \n\nLook at the sky. The ISS is now above you"
                                )


