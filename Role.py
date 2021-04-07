from pydantic import BaseModel, Field


class Role(BaseModel):
    label_role: str = Field(..., alias='role')

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
