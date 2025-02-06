from pydantic import BaseModel, EmailStr
from datetime import datetime

class EmailResponse(BaseModel):
    email: EmailStr
    sent_at: datetime
