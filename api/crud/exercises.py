from typing import Any, Optional

from sqlalchemy.orm import Session
from fastapi import HTTPException, UploadFile

from db.models import Exercise
from schemas.exercises import ExerciseCreate, ExerciseUpdate

from .base import BaseService

from utils.file_handling import save_image_file
from utils.config import EXERCISE_IMAGES_PATH

class ExcerciseService(BaseService[Exercise, ExerciseCreate, ExerciseUpdate]):
    def __init__(self, db_session: Session):
        super(ExcerciseService, self).__init__(Exercise, db_session)

    def get_image_path(self, exercise_id: Any) -> Any:
        exercise: Optional[Exercise] = self.get(exercise_id)

        return exercise.image_path

    def update_image(self, exercise_id: Any, image_file: UploadFile) -> Optional[Exercise]:
        exercise: Optional[Exercise] = self.get(exercise_id)
        file_path = save_image_file(image_file, EXERCISE_IMAGES_PATH)
        exercise.image_path = file_path
        return self.update(exercise_id, ExerciseUpdate.from_orm(exercise))