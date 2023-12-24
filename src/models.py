from typing import Literal

from pydantic import BaseModel, field_validator, Field
from pydantic import ValidationError


class Order(BaseModel):
    location: str
    fund_code: str
    price: int

    @field_validator("price", mode="wrap")
    def fix_price(cls, value, handler):
        return int(str(value).replace(".", ""))


class OrderRL(Order):
    location: Literal["MAL", "MAP"]


class Item(BaseModel):
    location: str
    price: float


class ItemRL(BaseModel):
    callno_tag: Literal["8528"]
    callno: str = Field(pattern=r"^ReCAP 23-\d{6}$")
