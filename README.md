##Doctor-Patient API

A simple REST API built with Django and Django REST Framework (DRF) to manage doctors, patients, and their medical records.

Doctors can:
View patient information
See patient medical problems and medications
Add new patient records via POST requests

##Features

✅ Doctor Login / Authentication
✅ GET all patients
✅ POST new patient records
✅ Uses Django REST Framework for API endpoints
✅ Simple, extendable models: Doctor, Patient, Record

##Installation

#Clone the repository:
git clone git@github.com:Adeline0111/doctor-patient-api.git
cd doctor-patient-api

##Create a virtual environment:
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

##Install dependencies:
pip install -r requirements.txt

##Apply migrations:
python manage.py makemigrations
python manage.py migrate

##Create a superuser (doctor):
python manage.py createsuperuser

##Run the server:
python manage.py runserver

| Method | Endpoint         | Description              |
| ------ | ---------------- | ------------------------ |
| GET    | `/api/patients/` | List all patients        |
| POST   | `/api/patients/` | Add a new patient record |

##Example Request
POST /api/patients/

{
  "name": "John Doe",
  "age": 35,
  "problem": "Flu",
  "medications": "Paracetamol, Vitamin C"
}

##License
MIT License – feel free to use and extend.


