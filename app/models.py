from pydantic import BaseModel

class Inquiry(BaseModel):
    question: str

class Appointment(BaseModel):
    client_name: str
    date_time: str
    case_description: str
    email: str
    lawyer_name: str
    lawyer_phone: str
    lawyer_email: str
