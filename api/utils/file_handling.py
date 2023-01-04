import os
import uuid
import shutil
import mimetypes

from fastapi import UploadFile, HTTPException


image_whitelist = ['image/jpeg', 'image/png']


def save_image_file(file: UploadFile, path: str) -> str:
    file_location = os.getcwd() + path + str(uuid.uuid4()) + mimetypes.guess_extension(file.content_type)
    try:
        with open(file_location, 'wb') as f:
            shutil.copyfileobj(file.file, f)
    except Exception:
        raise HTTPException(status_code=500)
    finally:
        file.file.close()

    return file_location