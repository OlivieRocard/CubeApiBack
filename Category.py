from pydantic import BaseModel, Field
from typing import Optional


class CategoryOut(BaseModel):
    #id_cat: int = Field(None, alias='id')
    label_cat: str = Field(..., alias='label')


    class Config:
        orm_mode = True
        allow_population_by_field_name = True


class Caracterise(BaseModel):
    #id_res: int = None
    #id_cat: int = None
    categorie: Optional[CategoryOut]

    class Config:
        orm_mode = True
        allow_population_by_field_name = True


