Workout Tracking via Nutritionix & Sheety
This Python application uses Natural Language Processing (NLP) to track workouts. It allows you to enter your exercise in plain English (e.g., "I ran 5km and walked for 20 minutes") and automatically logs the date, time, duration, and calories burned to a connected Google Sheet.

Features
Natural Language Input: Uses the Nutritionix API to understand conversational text.

Automatic Google Sheets Logging: Uses the Sheety API to append data to your spreadsheet.

Smart Duration Logic: Automatically standardizes gym sessions to 90 minutes and cardio to 30 minutes for consistent tracking.

Dynamic Calorie Scaling: Recalculates calories burned based on the adjusted durations to ensure data accuracy.

Secure Authentication: Utilizes environment variables to keep API keys and tokens private.

Prerequisites
Nutritionix API Key: Get your APP_ID and API_KEY from the Nutritionix Developer Portal.

Sheety Account: Connect your Google Sheet at Sheety.co. Ensure your sheet has these headers: Date, Time, Exercise, Duration, Calories.

Python 3.x

Requests Library: pip install requests

Setup and Environment Variables
Set the following environment variables on your system before running the script:

own_app_id: Your Nutritionix App ID.

own_api_key: Your Nutritionix API Key.

own_token: Your Sheety Bearer Token.

own_sheet_endpoint: Your Sheety Project API URL.

own_username: Your Sheety username (if required).

own_password: Your Sheety password (if required).
