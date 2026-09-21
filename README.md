
# Support Desk CRM System

A lightweight, high-performance Support Desk & CRM web application built with **FastAPI**, **SQLAlchemy**, and a clean **vanilla JavaScript/HTML/CSS** dashboard. It allows teams to manage customer support tickets, track SLAs, update ticket statuses, and process incoming support requests in real time.

---

## -- Features

- **Ticket Dashboard:** Track ticket IDs, customer info, subjects, creation dates, and priority status.
- **SLA & Priority Calculation:** Dynamic SLA tracking based on ticket age and status.
- **Timezone Awareness:** Automatic UTC-to-Local timezone parsing for accurate timestamp rendering.
- **Modal View & Editing:** View full ticket details, updates, and activity logs in responsive modal overlays.
- **RESTful API Backend:** Fast, asynchronous FastAPI endpoints built with structured Pydantic schemas.
- **Railway Ready:** Pre-configured with a `Procfile` and environment-aware start commands for zero-friction cloud deployment.

---

## ------ Tech Stack

- **Backend:** Python 3.10+, FastAPI, Uvicorn, SQLAlchemy, Pydantic
- **Frontend:** HTML5, Tailwind CSS / Custom CSS, Modern Vanilla JavaScript (Fetch API)
- **Database:** SQLite (Development) / PostgreSQL (Production)
- **Deployment:** Railway

---

## 📁 Project Structure

```text
crm-system/
├── app/
│   ├── __init__.py
│   ├── main.py          # FastAPI application routes & setup
│   ├── models.py        # SQLAlchemy database models
│   ├── schemas.py       # Pydantic models for validation
│   └── database.py      # Database engine & session configuration
├── static/
│   └── index.html       # Single-page application frontend dashboard
├── Procfile             # Railway start command configuration
├── requirements.txt     # Python dependencies
└── README.md

Local Setup & Installation
1. Clone the Repository
git clone [https://github.com/Mohitkumar874/crm-system.git](https://github.com/Mohitkumar874/crm-system.git)
cd crm-system

2. Set Up Virtual Environment
# Windows
python -m venv .venv
.venv\Scripts\activate

# macOS / Linux
python3 -m venv .venv
source .venv/bin/activate

3. Install Dependencies
pip install -r requirements.txt

4. Run the Application

uvicorn app.main:app --reload
Open your browser and navigate to http://127.0.0.1:8000 to access the dashboard.

Swagger API documentation is automatically available at http://127.0.0.1:8000/docs


-----Deployment (Railway)
-This repository is optimized for quick deployment on Railway.

-Connect your GitHub repository to Railway.

-Ensure the Start Command is configured as:

-Bash
-uvicorn app.main:app --host 0.0.0.0 --port $PORT

