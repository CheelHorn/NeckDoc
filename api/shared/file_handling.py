import os
import uuid
import shutil
import mimetypes

from fastapi import UploadFile, HTTPException

image_whitelist = ['image/jpeg', 'image/png']
video_whitelist = ['video/mp4']

def save_file(file: UploadFile, file_path: str, file_name: str, file_extension: str) -> str:
    file_location = file_path + file_name + file_extension
    try:
        with open(os.getcwd()+file_location, 'wb') as f:
            shutil.copyfileobj(file.file, f)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        file.file.close()

    return file_location

def save_image_file(file: UploadFile, file_path: str, file_name: str) -> str:
    file_extension = mimetypes.guess_extension(file.content_type)

    #TODO: Check for image mimetype
    if 1==1:
        return save_file(file, file_path, file_name, file_extension)
    else:
        raise HTTPException(status_code=500) 


def save_video_file(file: UploadFile, file_path: str, file_name: str) -> str:
    file_extension = mimetypes.guess_extension(file.content_type)

    #TODO: Check for video mimetype
    if 1==1:
        return save_file(file, file_path, file_name, file_extension)
    else:
        raise HTTPException(status_code=500) 