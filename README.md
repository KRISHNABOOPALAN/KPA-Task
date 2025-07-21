# KPA Assignment - Backend API (Django)

## Tech Stack
- Python 3.12
- Django REST Framework
- PostgreSQL
- Postman for API Testing

## APIs Implemented
1. `POST /api/forms/bogie-checksheet`  
   - Saves a bogie inspection form with nested JSON fields.

2. `GET /api/forms/wheel-specifications`  
   - Fetches wheel specification forms using optional filters.

## Setup Instructions
1. Clone the project or unzip the folder.
2. Create a virtual environment:

python -m venv env
source env/bin/activate

3. Install dependencies:

pip install -r requirements.txt

4. Create a `.env` file with DB credentials:

DB_NAME=kpa
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432

5. Run migrations:

python manage.py makemigrations
python manage.py migrate

6. Run server:

python manage.py runserver


## How to Test
- Use Postman and import the provided collection.
- Test both POST and GET APIs.
- Data is stored in PostgreSQL.

## Assumptions / Limitations
- Auth not implemented (not required).
- Validation is minimal and based on field presence.

