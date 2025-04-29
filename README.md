# Django Complaint Management System with Auto-Tagging

## Project Description
This is a Django web application where users can submit complaints.  
The system automatically tags complaints as "Urgent" if keywords like fire, accident, or violence are found otherwise the complaint is tagged as "Normal".

## Features
- Complaint Submission Form
- Auto-Tagging based on keywords
- Admin Panel to view and manage complaints
- Bootstrap Frontend
- (Bonus) Download complaints as CSV

## Technologies Used
- Python
- Django
- SQLite3 (Default Database)
- Bootstrap 5 (Frontend)

## Setup Instructions

1. "Clone the Repository".
   
   ```bash
   git clone <your-github-repo-link>

--------------------------------------------------------------------------------------------------------------------------
2. "OR Download zip and extract it".

- cd complaint_management
- python -m venv env source env/bin/activate # On window: env\Scripts\activate
- pip install -r requirements.txt
- python manage.py migrate
- python manage.py createsuperuser
- python manage.py runserver

# now you can access it in web browser

- http://127.0.0.1:8000/ -> for access project
- http://127.0.0.1:8000/admin/ -> for admin page