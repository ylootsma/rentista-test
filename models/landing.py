from models.base_model import BaseModel
import peewee as pw


class Landing(BaseModel):
    size = pw.CharField(unique=False, default="default")
    email = pw.CharField(unique=True, default="default")
    subscription = pw.CharField(unique=False, default="default")
    name = pw.CharField(unique=False, default="default")
    landingpage = pw.CharField(unique=False, default="default")
    payment = pw.CharField(unique=False, default="default")
