from pydantic import BaseModel, Field
from typing import Optional

class RelationOut(BaseModel):
    # id_rel: int = Field(None, alias='id')
    label_rel: str = Field(..., alias='label')

    class Config:
        orm_mode = True
        allow_population_by_field_name = True

class Valable(BaseModel):
    #id_res: int = None
    #id_rel: int = None
    relation: Optional[RelationOut]

    class Config:
        orm_mode = True
        allow_population_by_field_name = True


