from fastapi import Depends, FastAPI, HTTPException, File, UploadFile
from fastapi.security import OAuth2PasswordRequestForm

from sqlalchemy.orm import Session

from routes import auth, users

from utils.auth import authenticate_user, create_access_token
from utils.dependencies import get_db

from models import users as user_model
from db.session import engine

#user_model.Base.metadata.drop_all(bind=engine)
#user_model.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth.router)
app.include_router(users.router)


# Only for swagger authorize demonstration
@app.post("/token")
def login_user(db: Session = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(email=form_data.username, password=form_data.password, db=db)

    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    return {
        "access_token": create_access_token(sub=user.email),
        "token_type": "bearer",
    }
