from fastapi import FastAPI, HTTPException
from app.models import Inquiry, Appointment
from app.ai import get_response
from app.db import save_appointment
from app.email_utils import send_email
from app.voice_utils import listen_to_user, speak_response

app = FastAPI()

@app.post("/inquiry/")
async def inquire(inquiry: Inquiry):
    response = get_response(inquiry.question)
    return {"response": response}

@app.get("/voice-inquiry/")
async def voice_interaction():
    user_input = listen_to_user()
    if user_input:
        response = get_response(user_input)
        speak_response(response)
        return {"response": response}
    else:
        raise HTTPException(status_code=400, detail="Could not process voice input.")

@app.post("/book-appointment/")
async def book_appointment(appointment: Appointment):
    print("::Booking appointment request received::")
    appointment_dict = appointment.model_dump()
    save_appointment(appointment_dict)
    print("::Appointment saved successfully::")
    print(f"::Sending appointment booking confirmation to: {appointment.client_name} ::")
    send_email(appointment.email, appointment_dict)
    print(f"::Appointment booking confirmation email sent to: {appointment.client_name} successfully ::")
    return {"message": "Appointment booked successfully!"}