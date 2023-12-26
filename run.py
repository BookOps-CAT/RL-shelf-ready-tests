from pydantic import ValidationError
from rich import print

from src.models import OrderRL, ItemRL


def parse_errors(e):
    return f"{e['loc'][0]}: {e['msg']} | input: {e['input']}"


def simulate():
    try:
        OrderRL(
            location="myn",
            fund_code="foo",
            price="9.99",
        )
    except ValidationError as exc:
        for e in exc.errors():
            formatted_e = parse_errors(e)
            print(f"[italic red]Order problem:[/italic red] {formatted_e}")

    try:
        ItemRL(location="rc2ma", price="999", callno_tag="8528", callno="23-123456")
    except ValidationError as exc:
        for e in exc.errors():
            formatted_e = parse_errors(e)
            print(f"[italic red]Item problem:[/italic red] {formatted_e}")


if __name__ == "__main__":
    simulate()
