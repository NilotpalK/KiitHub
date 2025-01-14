from pydantic import BaseModel, EmailStr
from datetime import datetime

class User(BaseModel):
    name: str
    email: EmailStr
    password: str
    phone: str = None
    created_at: datetime = datetime.now()

class UserInDB(User):
    id: str