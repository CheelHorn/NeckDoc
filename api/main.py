from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


from routes import auth, patient, therapist, exercise, training, therapy


app = FastAPI()

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
app.include_router(exercise.router)
app.include_router(training.router)
app.include_router(therapy.router)
