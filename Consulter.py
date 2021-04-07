from pydantic import BaseModel, Field
from datetime import date
from typing import List, Optional


class ConsulterOut(BaseModel):
    id_res: int = Field(None)
    id_user: int = Field(None)
    favorite: bool = Field(None)
    start_date: date = Field(None, alias='ressource commencée le ')
    end_date: date = Field(None, alias='ressource finie le ')
    note_user: int = Field(None, alias='nombre d\'étoile')

    class Config:
        orm_mode = True
        allow_population_by_field_name = True


class FavoriteCreate(BaseModel):
    id_res: int
    id_user: int
    favorite: bool
    note_user: int
