from contextlib import nullcontext as does_not_raise

import pytest
from pydantic import ValidationError


from src.models import OrderRL


@pytest.mark.parametrize("arg", [800, "800", "1234", "12.34"])
def test_RLOrder_price_valid_values(arg):
    with does_not_raise():
        OrderRL(location="MAL", fund_code="foo", price=arg)


@pytest.mark.parametrize("arg", ["", None, "foo"])
def test_RLOrder_price_invalid(arg):
    with pytest.raises(ValidationError):
        OrderRL(location="MAL", fund_code="foo", price=arg)
