from fastapi import FastAPI
from datetime import datetime, timedelta
import random
from typing import Dict
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def generate_blood_pressure():
    # Generate random but realistic blood pressure values
    systolic = random.randint(140, 170)
    diastolic = random.randint(85, 100)
    return f"{systolic}/{diastolic}"

def get_bp_status(bp_reading: str):
    systolic = int(bp_reading.split('/')[0])
    if systolic >= 160:
        return "Critical"
    elif systolic >= 150:
        return "High"
    else:
        return "Elevated"

def generate_appointment_time():
    # Generate a random time for tomorrow
    tomorrow = datetime.now() + timedelta(days=1)
    hour = random.randint(9, 16)  # Between 9 AM and 4 PM
    minute = random.choice([0, 15, 30, 45])
    return tomorrow.replace(hour=hour, minute=minute)

def format_appointment_time(dt: datetime):
    return dt.strftime("%I:%M %p")

def generate_appointment_location():
    locations = [
        "SGH Cardiology, Level 3",
        "SGH Heart Centre, Block 4",
        "SGH Medical Centre, Level 2",
        "SGH Specialist Clinic, Level 4"
    ]
    return random.choice(locations)

def generate_missed_meds():
    times = random.randint(1, 4)
    return f"Missed medication {times}x this week"

@app.get("/health-context")
async def get_health_context() -> Dict:
    bp_reading = generate_blood_pressure()
    appointment_time = generate_appointment_time()
    
    return {
        "vital_signs": {
            "blood_pressure": {
                "reading": bp_reading,
                "time": "10:00 AM",
                "status": get_bp_status(bp_reading)
            }
        },
        "calendar": {
            "event": "Cardiology appointment",
            "datetime": format_appointment_time(appointment_time),
            "location": generate_appointment_location()
        },
        "medical_logs": {
            "medication_adherence": generate_missed_meds()
        }
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
