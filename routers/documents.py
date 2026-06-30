from fastapi import APIRouter, UploadFile, File, BackgroundTasks, HTTPException
from fastapi.responses import JSONResponse
import os
import shutil

from services.rag_service import process_document

router = APIRouter()

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/upload")
async def upload_document(
    file: UploadFile = File(...),
    background_tasks: BackgroundTasks = BackgroundTasks()
):

    if not file.filename.lower().endswith(
        ('.pdf', '.txt', '.md')
    ):
        raise HTTPException(
            status_code=400,
            detail="Only PDF, TXT and MD files are allowed"
        )

    file_path = os.path.join(
        UPLOAD_DIR,
        file.filename
    )

    with open(file_path, "wb") as buffer:

        shutil.copyfileobj(
            file.file,
            buffer
        )

    background_tasks.add_task(
        process_document,
        file_path,
        file.filename
    )

    return {
        "message":
        f"{file.filename} uploaded successfully"
    }