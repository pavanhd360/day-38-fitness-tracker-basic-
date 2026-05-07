
from ctypes import HRESULT
import os
import requests
from datetime import datetime
GENDER = "male"
WEIGHT_KG = 70
HEIGHT_CM = 175
AGE = 19
USERNAME = os.environ.get("own_username")
PASSWORD =  os.environ.get("own_password")
TOKEN = os.environ.get("own_token")

APP_ID = os.environ.get("own_app_id")
API_KEY = os.environ.get("own_api_key")
exercise_endpoint = "https://app.100daysofpython.dev/v1/nutrition/natural/exercise"
sheet_endpoint = os.environ.get("own_sheet_endpoint")
exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(result)

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    exercise_name = exercise["name"].lower()

    # --- THIS IS THE LOGIC TO CHANGE DURATION ---
    if "run" in exercise_name or "cardio" in exercise_name:
        final_duration = 30
    elif "gym" in exercise_name or "lift" in exercise_name or "exercise" in exercise_name:
        final_duration = 90  # This forces 1.5 hours for 'gym'
    else:
        final_duration = exercise["duration_min"]

    # --- SCALE CALORIES FOR THE NEW DURATION ---
    # (Optional but recommended so your stats stay accurate)
    final_calories = round((exercise["nf_calories"] / exercise["duration_min"]) * final_duration)

    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise_name.title(),
            "duration": final_duration,  # <-- WE USE THE NEW VARIABLE HERE
            "calories": final_calories
        }
    }

    # 3. Send to Sheety (Use only ONE of these)
    bearer_headers = {"Authorization": f"Bearer {TOKEN}"}
    sheet_response = requests.post(
        sheet_endpoint,
        json=sheet_inputs,
        headers=bearer_headers
    )

    print(sheet_response.text)
