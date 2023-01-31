

from services.user import UserService
from db.models import Patient
from schemas.user import PatientUpdate, UserCreate

class PatientService(UserService[Patient, PatientUpdate, UserCreate]):
    def __init__(self, db_session):
        super(PatientService, self).__init__(Patient, db_session)
