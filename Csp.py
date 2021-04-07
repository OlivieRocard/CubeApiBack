from pydantic import BaseModel, Field


class Csp(BaseModel):
    label_csp: str = Field(..., alias='csp')

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
