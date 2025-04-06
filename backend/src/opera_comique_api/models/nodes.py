from datetime import date

from pydantic import BaseModel


class Work(BaseModel):
    charlton_id: str
    title: str


class Performance(BaseModel):
    date: date
    location: str
