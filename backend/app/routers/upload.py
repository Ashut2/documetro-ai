from fastapi import APIRouter , UploadFile , File

# created router object (so it can be included in main.py later )
router = APIRouter()

# Example route for uploading a file 
@router.post("/")
async def upload_file(file:UploadFile = File(...)):
    #    Upload a file to the system (right now just returns the filename).
    # Later we will connect this to OCR + NLP pipeline.
    return {
        "filename": file.filename
    }
