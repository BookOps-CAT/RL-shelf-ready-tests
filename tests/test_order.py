from contextlib import nullcontext as does_not_raise

import pytest
from pydantic import ValidationError


from src.models import Order, OrderRL


@pytest.mark.parametrize("arg", [800, "800", "1234", "12.34"])
def test_Order_price_valid_values(arg):
    with does_not_raise():
        Order(location="MAL", fund_code="foo", price=arg)


@pytest.mark.parametrize("arg", ["", None, "foo"])
def test_Order_price_invalid(arg):
    with pytest.raises(ValidationError):
        Order(location="MAL", fund_code="foo", price=arg)


@pytest.mark.parametrize("arg", ["MAL", "MAP"])
def test_OrderRL_location_valid(arg):
    with does_not_raise():
        OrderRL(location=arg, fund_code="foo", price="999")


@pytest.mark.parametrize("arg", ["foo", "", None, 5, []])
def test_OrderRL_location_invalid(arg):
    with pytest.raises(ValidationError):
        OrderRL(location=arg, fund_code="foo", price="999")
