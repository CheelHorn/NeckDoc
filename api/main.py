from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from features.authentication.routes import auth
from features.exercise.routes import exercise, exercise_image
from features.therapy.routes import patient, therapist, therapy
from features.training_plan.routes import training_plan, exercise_duration, exercise_interval, training_plan_exercise, exercise_execution, video_stream

app = FastAPI()
app.mount("/assets", StaticFiles(directory="assets"), name="assets")

origins = [
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router)
app.include_router(patient.router)
app.include_router(therapist.router)
app.include_router(therapy.router)
app.include_router(exercise.router)
app.include_router(exercise_image.router)
app.include_router(training_plan.router)
app.include_router(exercise_duration.router)
app.include_router(exercise_interval.router)
app.include_router(training_plan_exercise.router)
app.include_router(exercise_execution.router)
app.include_router(video_stream.router)
