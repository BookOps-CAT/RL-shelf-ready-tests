from enum import Enum
from typing import Literal

from pydantic import BaseModel, Field


class MarcOrderEncoding(Enum):
    location = "$t"
    fund_code = "$u"
    price = "$s"


class MarcItemEncoding(Enum):
    location = "$l"
    price = "$p"
    callno_tag = "$z"
    callno = "$a"


class Order(BaseModel):
    location: str
    fund_code: str
    price: str = Field(pattern=r"^\d{3,}$")


class OrderRL(Order):
    location: Literal["MAL", "MAP"]


class Item(BaseModel):
    location: str
    price: str = Field(pattern=r"\d{1,}\.\d{2}$")


class ItemRL(Item):
    callno_tag: Literal["8528"]
    callno: str = Field(pattern=r"^ReCAP 23-\d{6}$")
    subs_combinations: Literal[("rcmb2", "2", "43"), ("rcmf2", "55", "43")]
