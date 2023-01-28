from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Extra, Field, PositiveInt

from app.constants import MAX_LIMIT, MIN_LIMIT


class CharityProjectBase(BaseModel):
    name: Optional[str] = Field(None, min_length=MIN_LIMIT, max_length=MAX_LIMIT)
    description: Optional[str] = Field(None, max_length=MAX_LIMIT)
    full_amount: Optional[PositiveInt]


class CharityProjectCreate(CharityProjectBase):
    name: str = Field(..., min_length=MIN_LIMIT, max_length=MAX_LIMIT)
    description: str = Field(..., min_length=MIN_LIMIT)
    full_amount: PositiveInt


class CharityProjectUpdate(CharityProjectBase):

    class Config:
        extra = Extra.forbid


class CharityProjectDB(CharityProjectBase):
    id: int
    invested_amount: Optional[int]
    fully_invested: Optional[bool]
    create_date: Optional[datetime]
    close_date: Optional[datetime]

    class Config:
        orm_mode = True
