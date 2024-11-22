# Leenk Health Context API

A FastAPI-based mock API that generates health context data for elderly care monitoring scenarios. Built for hackathon demonstration purposes.

## Sample Response

```json
{
    "vital_signs": {
        "blood_pressure": {
            "reading": "155/90",
            "time": "10:00 AM",
            "status": "High"
        }
    },
    "calendar": {
        "event": "Cardiology appointment",
        "datetime": "02:30 PM",
        "location": "SGH Cardiology, Level 3"
    },
    "medical_logs": {
        "medication_adherence": "Missed medication 2x this week"
    }
}
```

## Quick Start

### Installation

1. Clone the repository
```bash
git clone [your-repo-url]
cd leenk-api
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

### Running the API

Start the FastAPI server:
```bash
python main.py
```

The API will be available at `http://localhost:8000`

## API Usage

### Health Context Endpoint

**Endpoint:** `/health-context`
**Method:** GET

#### cURL Example
```bash
curl http://localhost:8000/health-context
```

#### Python Request Example
```python
import requests

response = requests.get('http://localhost:8000/health-context')
print(response.json())
```

## Features

- Randomized but realistic blood pressure readings
- Dynamic appointment scheduling information
- Medication adherence tracking
- CORS enabled for frontend integration

## API Documentation

Once the server is running, visit:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`
