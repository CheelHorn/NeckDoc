from typing import Any, Optional

from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, UploadFile

# Pydantic schemas
from features.training_plan.schemas.exercise_execution import ExerciseExecutionCreate, ExerciseExecutionUpdate

# SQLAlchemy models
from db.models import ExerciseExecution, TrainingPlanExercise
from db.session import get_db

from shared.base import BaseService

from shared.file_handling import save_video_file
from shared.config import EXERCISE_EXECUTION_VIDEO_PATH

class ExerciseExecutionService(BaseService[ExerciseExecution, ExerciseExecutionCreate, ExerciseExecutionUpdate]):
    def __init__(self, db_session: Session):
        super(ExerciseExecutionService, self).__init__(ExerciseExecution, db_session)

    def create(self, obj: ExerciseExecutionCreate) -> ExerciseExecution:
        training_plan_exercise = self.db_session.query(TrainingPlanExercise).get(obj.training_plan_exercise_id)

        if training_plan_exercise is None:
            raise HTTPException(
                status_code=400,
                detail=f"TrainingPlan with trainingPlanId = {obj.training_plan_exercise_id} not found.",
            )
        return super(ExerciseExecutionService, self).create(obj)
    
    def upload_video(self, exercise_execution_id: Any, video_file: UploadFile) -> Any:
        exercise_execution: Optional[ExerciseExecution] = self.get(exercise_execution_id)
        file_url = save_video_file(video_file, EXERCISE_EXECUTION_VIDEO_PATH)
        exercise_execution.video_url = file_url

        return self.update(exercise_execution_id, ExerciseExecutionUpdate.from_orm(exercise_execution))

def get_exercise_execution_service(db_session: Session = Depends(get_db)) -> ExerciseExecutionService:
    return ExerciseExecutionService(db_session)