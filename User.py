from pydantic import BaseModel, Field
from datetime import date, datetime
from typing import List, Optional
from .Role import Role
from .Csp import Csp


class UserOut(BaseModel):
    id_user: int = Field(None, alias='id')
    pseudo_user: str = Field(None, alias='pseudo')
    firstname: str = Field(None)
    lastname: str = Field(None)
    zip_code_user: str = Field(None, alias='zip_code')
    mail_user: str = Field(None, alias='mail')
    birthdate_user: date = Field(None, alias='birthdate')
    created_at_user: date = Field(None, alias='created')
    updated_at_user: date = Field(None, alias='updated')
    role: Role = Field(None)
    csp: Csp = Field(None)


    class Config:
        orm_mode = True
        allow_population_by_field_name = True


class UserCreate(BaseModel):
    pseudo: str
    firstname: str
    lastname: str
    password: str
    mail: str
    birthdate: date
    zip_code: str
    csp: int
    role: str

