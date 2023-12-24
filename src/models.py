from decimal import *
from typing import Literal

from pydantic import BaseModel, field_validator, Field
from pydantic import ValidationError


class Order(BaseModel):
    location: str
    fund_code: str
    price: str = Field(pattern=r"^\d{3,}$")


class OrderRL(Order):
    location: Literal["MAL", "MAP"]


class Item(BaseModel):
    location: str
    price: str = Field(pattern=r"\d{1,}\.\d{2}$")


class ItemRL(BaseModel):
    callno_tag: Literal["8528"]
    callno: str = Field(pattern=r"^ReCAP 23-\d{6}$")
