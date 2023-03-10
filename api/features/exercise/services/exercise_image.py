from typing import Any, Optional

from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, UploadFile

# Pydantic schemas
from features.exercise.schemas.exercise_image import ExerciseImageCreate, ExerciseImageUpdate
from pydantic.types import UUID4

# SqlAlchemy models
from db.models import ExerciseImage, Exercise
from db.session import get_db

from shared.base import BaseService

from shared.file_handling import save_image_file
from shared.config import EXERCISE_IMAGE_PATH

class ExerciseImageService(BaseService[ExerciseImage, ExerciseImageCreate, ExerciseImageUpdate]):
    def __init__(self, db_session: Session):
        super(ExerciseImageService, self).__init__(ExerciseImage, db_session)

    def create(self, exercise_image: ExerciseImageCreate) -> Optional[ExerciseImage]:
        exercise = self.db_session.query(Exercise).get(exercise_image.exercise_id)
        if exercise is None:

            raise HTTPException(
                status_code=400,
                detail=f"Exercise with exerciseId = {exercise_image.exercise_id} not found.",
            )
        
        return super(ExerciseImageService, self).create(exercise_image)

    def upload_image(self, exercise_image_id: UUID4, image_file: UploadFile) -> Optional[ExerciseImage]:
        exercise_image: Optional[ExerciseImage] = self.get(exercise_image_id)
        print(exercise_image_id)
        print(str(exercise_image_id))

        file_url = save_image_file(image_file, EXERCISE_IMAGE_PATH, str(exercise_image_id))
        exercise_image.image_url = file_url
        return super(ExerciseImageService, self).update(exercise_image_id, ExerciseImageUpdate.from_orm(exercise_image))


def get_exercise_image_service(db_session: Session = Depends(get_db)) -> ExerciseImageService:
    return ExerciseImageService(db_session)