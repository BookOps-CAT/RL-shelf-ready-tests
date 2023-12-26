from pydantic import ValidationError
from rich import print

from src.models import OrderRL, ItemRL, MarcOrderEncoding, MarcItemEncoding


def format_errors(e, model):
    if model == "order":
        return (
            f"{MarcOrderEncoding[e['loc'][0]].value} ({e['loc'][0]}): "
            f"{e['msg']} | input: {e['input']}"
        )
    elif model == "item":
        return (
            f"{MarcItemEncoding[e['loc'][0]].value} ({e['loc'][0]}): "
            f"{e['msg']} | input: {e['input']}"
        )


def simulate():
    try:
        OrderRL(
            location="myn",
            fund_code="foo",
            price="9.99",
        )
    except ValidationError as exc:
        for e in exc.errors():
            formatted_e = format_errors(e, "order")
            print(f"[italic red]960 field (order):[/italic red] {formatted_e}")

    try:
        ItemRL(location="rc2ma", price="999", callno_tag="8528", callno="23-123456")
    except ValidationError as exc:
        for e in exc.errors():
            formatted_e = format_errors(e, "item")
            print(f"[italic red]949 field (item):[/italic red] {formatted_e}")


if __name__ == "__main__":
    simulate()
