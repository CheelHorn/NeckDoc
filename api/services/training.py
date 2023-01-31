from typing import Any, Optional

from sqlalchemy.orm import Session
from fastapi import HTTPException, UploadFile

from db.models import Training, User, Exercise
from schemas.training import TrainingCreate, TrainingUpdate

from .base import BaseService

from utils.file_handling import save_video_file
from utils.config import TRAINING_VIDEOS_PATH

class TrainingService(BaseService[Training, TrainingCreate, TrainingUpdate]):
    def __init__(self, db_session: Session):
        super(TrainingService, self).__init__(Training, db_session)

    def create(self, obj: TrainingCreate, db_session: Session) -> Training:
        user = db_session.query(User).get(obj.user_id)
        exercise = self.db_session.query(Exercise).get(obj.exercise_id)

        if user is None:
            raise HTTPException(
                status_code=400,
                detail=f"User with userId = {obj.user_id} not found.",
            )

        if exercise is None:
            raise HTTPException(
                status_code=400,
                detail=f"Exercise with exerciseId = {obj.exercise_id} not found.",
            )

        return super(TrainingService, self).create(obj)

    def update_video(self, training_id: Any, image_file: UploadFile, db_session: Session) -> Optional[Training]:
        exercise: Optional[Training] = self.get(training_id, db_session)
        file_path = save_video_file(image_file, TRAINING_VIDEOS_PATH)
        exercise.image_path = file_path
        return self.update(training_id, TrainingUpdate.from_orm(exercise), db_session)
        