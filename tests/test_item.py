from contextlib import nullcontext as does_not_raise

import pytest
from pydantic import ValidationError


from src.models import Item, ItemRL


@pytest.mark.parametrize("arg", ["9.99", "0.00"])
def test_Item_price_valid(arg):
    with does_not_raise():
        Item(location="sna0l", price=arg)


@pytest.mark.parametrize("arg", ["999", "0", "9.999", 999, 0.99, 0, "", None])
def test_Item_price_invalid(arg):
    with pytest.raises(ValidationError):
        Item(location="sna0l", price=arg)


def test_ItemRL_callno_tag_valid():
    with does_not_raise():
        ItemRL(
            callno_tag="8528",
            callno="ReCAP 23-108092",
            price="9.99",
            location="rcmb2",
            subs_combinations=("rcmb2", "2", "43"),
        )


@pytest.mark.parametrize("arg", [None, "", "foo"])
def test_ItemRL_callno_tag_invalid(arg):
    with pytest.raises(ValidationError):
        ItemRL(
            callno_tag=arg,
            callno="ReCAP 23-108092",
            price="9.99",
            location="rcmb2",
            subs_combinations=("rcmb2", "2", "43"),
        )


@pytest.mark.parametrize("arg", ["ReCAP 23-108092", "ReCAP 23-108093"])
def test_item_callno_valid(arg):
    with does_not_raise():
        ItemRL(
            callno_tag="8528",
            callno=arg,
            price="9.99",
            location="rcmb2",
            subs_combinations=("rcmb2", "2", "43"),
        )


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
def test_ItemRL_callno_valid(arg):
    with pytest.raises(ValidationError):
        ItemRL(
            callno_tag="8528",
            callno=arg,
            price="9.99",
            location="rcmb2",
            subs_combinations=("rcmb2", "2", "43"),
        )


def test_ItemRL_subs_combination_rcmb2_invalid_item_type():
    with pytest.raises(ValidationError) as exc:
        ItemRL(
            callno_tag="8528",
            callno="ReCAP 23-108092",
            price="9.99",
            location="rc2ma",
            subs_combinations=("rcmb2", "55", "43"),
        )
    assert "Input should be ('rcmb2', '2', '43')" in (str(exc))


def test_ItemRL_subs_combination_rcmf2_valid():
    with does_not_raise():
        ItemRL(
            callno_tag="8528",
            callno="ReCAP 23-108092",
            price="9.99",
            location="rcmf2",
            subs_combinations=("rcmf2", "55", "43"),
        )
