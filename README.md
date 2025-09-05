# documetro-ai
Document Intelligence System for SIH - OCR ,NLP, Search &amp; Notifications 
## FastAPI Backend (App Layer)

### Endpoints
- POST /upload/ → Uploads a file to the `uploads/` folder
- POST /search/ → Accepts a query (currently stub)
- POST /notify/ → Accepts a message (currently stub)
- GET / → Health check

### How to Run
python -m uvicorn main:app --reload

### Notes
- Files are stored in `uploads/`
- SQLite DB (`test.db`) + SQLAlchemy setup included for extension


### 1. How to Run the Project

## Clone the repo:

git clone <your-repo-url>
cd backend


## Create and activate a virtual environment (if not already):

python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate # Linux/Mac


## Install dependencies:

pip install -r requirements.txt


## Run the FastAPI server:

uvicorn app.main:app --reload

### 2. Database Rules

Don’t manually delete or move test.db.

Always use the API endpoints (like /upload/ and /upload/list) to interact with the database.

If they really need to reset the DB, ask them to delete test.db and restart the server → it will auto-create a fresh one.

### 3. Code Editing Rules

Don’t touch database.py (that’s our core setup).

If you need new endpoints :

Create them in a new router file (e.g., routers/analyze.py)

Import and include the router inside main.py.

Don’t duplicate get_db or Document imports → always import from app.database.

### 4. Git Workflow

Always pull latest before pushing:

git pull origin main


When adding new features, create a new branch:

git checkout -b feature-branch-name


Push the branch and open a Pull Request → this way, your main branch stays safe.

### 5. Testing

After running the server, they can test in:

Swagger Docs → http://127.0.0.1:8000/docs

Upload a file in /upload/ → confirm it appears in uploads/ folder.

Check test.db → confirm the row is saved in the documents table.

👉 Basically: “Don’t touch the database setup. Don’t push directly to main. Always test your endpoints in Swagger before committing.”
