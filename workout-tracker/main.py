import requests
from datetime import datetime
import os

#Make the request to nutritionix API
APP_ID = os.environ["APP_ID"]
API_KEY = os.environ["API_KEY"]
exercise_headers = {
    "Content-Type": "application/json",
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}
body = {
     "query": "I Ran 1K and cycled for 10 minutes",
     "gender": "male",
     "weight_kg": 65,
     "height_cm": 165,
     "age": 30
}
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
response = requests.post(exercise_endpoint, json=body, headers=exercise_headers)
result = response.json()

#Organize response in sheets
SHEETY_TOKEN = os.environ["SHEETY_TOKEN"]
sheety_endpoint = "https://api.sheety.co/e2a2a8c2c5a4ef42ce82913818b2b87a/copiaDiMyWorkouts/workouts"
sheety_headers = {
    "Authorization": f"Bearer {SHEETY_TOKEN}"
}


today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheety_endpoint, json=sheet_inputs, headers=sheety_headers)


