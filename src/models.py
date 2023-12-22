from pydantic import BaseModel, field_validator, Field

from typing import Literal


class OrderRL(BaseModel):
    location: str
    fund_code: str
    price: int

    @field_validator("price", mode="wrap")
    def fix_price(cls, value, hadler):
        return int(str(value).replace(".", ""))


class ItemRL(BaseModel):
    callno_tag: Literal["8528"]
    callno: str = Field(pattern=r"^ReCAP 23-\d{6}$")
