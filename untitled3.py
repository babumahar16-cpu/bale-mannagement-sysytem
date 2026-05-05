-
"""Untitled3.ipynb



!pip install -q -U google-generativeai

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "AI Controller Running"}

@app.get("/predict")
def predict(value: float):
    result = value * 2  # yahan apna AI logic/model lagao
    return {"output": result}




print("FastAPI server started on http://0.0.0.0:8000")


print(public_url)

import google.generativeai as genai
from google.colab import userdata

# Get the API key securely from Colab's user data secretshttp://localhost:8000/
api_key = userdata.get('google-api-key')

# Verify the API key
print(f"API Key retrieved: {api_key}")

# Configure the genai library with the API key
genai.configure(api_key=api_key)

model = genai.GenerativeModel('gemini-2.5-flash')






print(f"AI Decision: {response.text}")



import google.generativeai as genai

# Define the functions that the AI can call
def check_system_temperature():
    """Checks the current system temperature."""
    # In a real scenario, this would interact with system sensors
    print("Checking system temperature...")
    return {"temperature": 75, "unit": "Fahrenheit"}

def turn_on_active_cooling(percentage: int):
    """Turns on active cooling to a specified percentage.

    print(f"Turning on active cooling to {percentage}%...")
    # In a real scenario, this would interact with system cooling hardware
    return {"status": "Cooling activated", "percentage": percentage}


}
