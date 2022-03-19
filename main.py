from fastapi import FastAPI
from fastapi.responses import JSONResponse
from decouple import config
from fastapi_mail import FastMail, MessageSchema,ConnectionConfig
from pydantic import BaseModel


app = FastAPI(title="Shop")

conf = ConnectionConfig(
    MAIL_USERNAME = config('MAIL_USERNAME'),
    MAIL_PASSWORD = config("MAIL_PASSWORD"),
    MAIL_FROM =config("MAIL_FROM"),
    MAIL_PORT = 587,
    MAIL_SERVER = "smtp.gmail.com",
    MAIL_TLS = True,
    MAIL_SSL = False,
    USE_CREDENTIALS = True,
    VALIDATE_CERTS = True
)


class Message(BaseModel):
    name:str
    email:str
    year_experience:str
    phone:str

@app.post("/email")
async def simple_send(message_in:Message) -> JSONResponse:

    body_message = f"""
Name: {message_in.name}
Email: {message_in.email}
Year of experience: {message_in.year_experience}
phone: {message_in.phone}
"""
    print(1)
    message = MessageSchema(
        subject="Fastapi-Mail module",
        recipients=['hamzasharit@gmail.com',],
        body=body_message,
        )
    fm = FastMail(conf)
    await fm.send_message(message)
    return JSONResponse(status_code=200, content={"message": "email has been sent"})     