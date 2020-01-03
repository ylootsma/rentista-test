from models.base_model import BaseModel
import peewee as pw


class Email(BaseModel):
    email = pw.CharField(unique=True, default="default")
    landingpage = pw.CharField(unique=False, default="default")
