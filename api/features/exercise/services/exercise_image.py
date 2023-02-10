from typing import Any, Optional

from sqlalchemy.orm import Session
from fastapi import Depends, UploadFile

# Pydantic schemas
from features.exercise.schemas.exercise_image import ExerciseImageCreate, ExerciseImageUpdate

# SqlAlchemy models
from db.models import ExerciseImage
from db.session import get_db

from shared.base import BaseService

from shared.file_handling import save_image_file
from shared.config import EXERCISE_IMAGE_PATH

class ExerciseImageService(BaseService[ExerciseImage, ExerciseImageCreate, ExerciseImageUpdate]):
    def __init__(self, db_session: Session):
        super(ExerciseImageService, self).__init__(ExerciseImage, db_session)

    def upload_image(self, exercise_image_id: Any, image_file: UploadFile) -> Optional[ExerciseImage]:
        exercise_image: Optional[ExerciseImage] = self.get(exercise_image_id)
        file_url = save_image_file(image_file, EXERCISE_IMAGE_PATH)
        exercise_image.image_url = file_url
        return self.update(exercise_image_id, ExerciseImageUpdate.from_orm(exercise_image))


def get_exercise_image_service(db_session: Session = Depends(get_db)) -> ExerciseImageService:
    return ExerciseImageService(db_session)