from fastapi import FastAPI, Request
from pydantic import BaseModel, EmailStr, constr
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pydantic import validator
import bleach
import os
# from fastapi.middleware.cors import CORSMiddleware

# # CORS Configuration
# origins = [
#     "https://zambelli.group"
# ]

smtp_server = os.getenv("SMTP_SERVER")
smtp_port = os.getenv("SMTP_PORT")
sender_email = os.getenv("SENDER_EMAIL")
receiver_email = os.getenv("RECEIVER_EMAIL")
smtp_username = os.getenv("SMTP_USERNAME")
smtp_password = os.getenv("SMTP_PASSWORD")

app = FastAPI()

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["POST"],
#     allow_headers=["Content-Type"],
# )

class ContactForm(BaseModel):
    name: constr(max_length=100)
    email: EmailStr
    subject: constr(max_length=100)
    message: constr(max_length=500)

    @validator('name', 'subject')
    def sanitize_text(cls, value):
        return bleach.clean(value, strip=True)


class FormAPI:
    @app.post("/api/submit-form")
    async def submit_form(self, request: Request, form_data: ContactForm):
        # Perform any extra necessary form validation and processing here
        # You can access the form data using `form_data.name`, `form_data.email`, etc.
        # For example, you can send an email notification using an email service or store the data in a database

        # Create the email message
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = receiver_email
        message["Subject"] = "Contact Form from zambelli.group"

        # Construct the email body
        email_body = f"""
        Name: {form_data.name}
        Email: {form_data.email}
        Subject: {form_data.subject}
        Message: {form_data.message}
        """
        message.attach(MIMEText(email_body, "plain"))

        try:
            # Connect to the SMTP server
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()

            # Login to your Gmail account
            server.login(smtp_username, smtp_password)

            # Send the email
            server.sendmail(sender_email, receiver_email, message.as_string())

            # Disconnect from the server
            server.quit()

            # Return a response indicating the success of form submission
            return {"message": "Form submitted successfully!"}
        except Exception as e:
            # Handle any errors that occur during email sending
            return {"message": f"Failed to submit form. Error: {str(e)}"}