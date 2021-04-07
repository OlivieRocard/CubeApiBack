from pydantic import BaseModel, Field
from datetime import date
from typing import List
from .Category import Caracterise
from.Relation import Valable


class RessourceOut(BaseModel):
    id_res: int = Field(None, alias='id')
    title_res: str = Field(None, alias='title')
    status_res: str = Field(None, alias='status')
    acces_res: bool = Field(None, alias='acces')
    content_res: str = Field(None, alias='content')
    source_res: str = Field(None, alias='source')
    diificulty: str = Field(None)
    created_at_res: date = Field(None, alias='created')
    updated_at_res: date = Field(None, alias='updated')
    valable: List[Valable] = Field(..., alias='Relation')
    caracterise: List[Caracterise] = Field(..., alias='Categorie')


    class Config:
        orm_mode = True
        allow_population_by_field_name = True


class RessourceCreate(BaseModel):

    title_res: str
    acces_res: str
    content_res: str
    source_res: str
    type_ressource: str
    category_res: str
    relation_res: str
    difficulty: str
    user: int

