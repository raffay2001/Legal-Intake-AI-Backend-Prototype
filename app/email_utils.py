import smtplib
from email.mime.text import MIMEText
from .config import EMAIL_SENDER, SMTP_SERVER_HOST, SMTP_SERVER_PORT, SMTP_SERVER_PASSWORD, SMTP_SERVER_LOGIN

def send_email(to_email, appointment):
    """Send an email confirmation for an appointment."""
    
    try:
        subject = "Appointment Confirmation From Raffay Legal Services"
        body = f"""
        Dear {appointment['client_name']},

        Your Appointment Is Confirmed For {appointment['date_time']}.

        Your Lawyer's Details Are Given Below: 

        1. Lawyer's Name: {appointment['lawyer_name']}
        2. Lawyer's Email: {appointment['lawyer_email']}
        3. Lawyer's Phone Number: {appointment['lawyer_phone']}

        Your Case Description Is: {appointment['case_description']}.

        Best Regards,
        Raffay Legal Services Team.
        """
        receiver_email = to_email
       
        message = MIMEText(body, "plain")
        message["Subject"] = subject
        message["From"] = EMAIL_SENDER
        message["To"] = to_email

        # Dispatching the email
        with smtplib.SMTP(SMTP_SERVER_HOST, SMTP_SERVER_PORT) as server:
            server.starttls()  
            server.login(SMTP_SERVER_LOGIN, SMTP_SERVER_PASSWORD)
            server.sendmail(EMAIL_SENDER, receiver_email, message.as_string())

    except Exception as e:
        print(f"Error sending email: {e}")