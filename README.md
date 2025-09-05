# documetro-ai
Document Intelligence System for SIH - OCR ,NLP, Search &amp; Notifications 
## FastAPI Backend (App Layer)

### Endpoints
- POST /upload/ → Uploads a file to the `uploads/` folder
- POST /search/ → Accepts a query (currently stub)
- POST /notify/ → Accepts a message (currently stub)
- GET / → Health check

### How to Run
uvicorn main:app --reload

### Notes
- Files are stored in `uploads/`
- SQLite DB (`test.db`) + SQLAlchemy setup included for extension
