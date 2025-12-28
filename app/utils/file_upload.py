# app/utils/file_upload.py

import os
import shutil
from uuid import uuid4
from fastapi import UploadFile, HTTPException

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_DIR = os.path.join(BASE_DIR, "..", "uploads")  
os.makedirs(UPLOAD_DIR, exist_ok=True)

# def save_file(file: UploadFile, folder: str) -> str:
def save_file(
    file: UploadFile,
    folder: str,
    allowed_types: list[str]
) -> str:
    
    if file.content_type not in allowed_types:
        raise HTTPException(status_code=400, detail="Invalid file type")
    ext = file.filename.split(".")[-1]
    filename = f"{uuid4()}.{ext}"   # remove file overwritten
    folder_path = os.path.join(UPLOAD_DIR, folder)

    os.makedirs(folder_path, exist_ok=True)

    file_path = os.path.join(folder_path, filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return file_path
