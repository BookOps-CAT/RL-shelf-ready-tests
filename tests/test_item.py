from contextlib import nullcontext as does_not_raise

import pytest
from pydantic import ValidationError


from src.models import ItemRL


def test_item_callno_tag_correct():
    with does_not_raise():
        ItemRL(callno_tag="8528", callno="ReCAP 23-108092")


@pytest.mark.parametrize("arg", [None, "", "foo"])
def test_item_callno_tag_invalid(arg):
    with pytest.raises(ValidationError):
        ItemRL(callno_tag=arg, callno="ReCAP 23-108092")
