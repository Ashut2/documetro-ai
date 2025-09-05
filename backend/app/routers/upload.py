from fastapi import APIRouter , UploadFile , File , Depends
from sqlalchemy.orm import Session
from app.database import get_db , Document
import os
# import DB Stuff
from ..database import SessionLocal,Document
# created router object (so it can be included in main.py later )
router = APIRouter()

UPLOAD_DIR = "uploads" # folder where files go
os.makedirs(UPLOAD_DIR, exist_ok=True) # create folder if it doesn’t exist

#  route for uploading a file 
@router.post("/")
async def upload_file(file:UploadFile = File(...) , db:Session=Depends(get_db)):
    #    Upload a file to the system (right now just returns the filename).
    # Later we will connect this to OCR + NLP pipeline.
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as f:
        f.write(await file.read())

    db_file = Document(filename=file.filename,filepath=file_path)
    db.add(db_file)
    db.commit()
    db.refresh(db_file)

    return {
                "message": f"File '{file.filename}' uploaded successfully!",
        "id": db_file.id,
        "filename": db_file.filename,
        "filepath": db_file.filepath

    }

@router.get("/list")
def list_files(db: Session = Depends(get_db)):
    # fetch all uploaded files stored in DB

    files = db.query(Document).all()
    return files
