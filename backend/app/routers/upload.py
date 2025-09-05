from fastapi import APIRouter , UploadFile , File
import os
# created router object (so it can be included in main.py later )
router = APIRouter()

UPLOAD_DIR = "uploads" # folder where files go
os.makedirs(UPLOAD_DIR, exist_ok=True) # create folder if it doesn’t exist

# Example route for uploading a file 
@router.post("/")
async def upload_file(file:UploadFile = File(...)):
    #    Upload a file to the system (right now just returns the filename).
    # Later we will connect this to OCR + NLP pipeline.
    file_path = os.path.join(UPLOAD_DIR, file.filename)

    with open(file_path, "wb") as f:
        f.write(await file.read())

    return {
        "message": f"File '{file.filename}' uploaded successfully!", "path": file_path
    }
