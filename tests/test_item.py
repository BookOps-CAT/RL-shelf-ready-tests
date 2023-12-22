from contextlib import nullcontext as does_not_raise

import pytest
from pydantic import ValidationError


from src.models import ItemRL


def test_item_callno_tag_valid():
    with does_not_raise():
        ItemRL(callno_tag="8528", callno="ReCAP 23-108092")


@pytest.mark.parametrize("arg", [None, "", "foo"])
def test_item_callno_tag_invalid(arg):
    with pytest.raises(ValidationError):
        ItemRL(callno_tag=arg, callno="ReCAP 23-108092")


@pytest.mark.parametrize("arg", ["ReCAP 23-108092", "ReCAP 23-108093"])
def test_item_callno_valid(arg):
    with does_not_raise():
        ItemRL(callno_tag="8528", callno=arg)


@pytest.mark.parametrize(
    "arg",
    [
        "ReCAP23-108092",
        "Rcap 23-108093",
        "ReCAP 23108093",
        "ReCAP 22-108092",
        "ReCAP 23-10809",
        "ReCAP 23-108092 ",
        " ReCAP 23-108092",
        "ReCAP  23-108092" "",
        None,
    ],
)
def test_item_callno_valid(arg):
    with pytest.raises(ValidationError):
        ItemRL(callno_tag="8528", callno=arg)
