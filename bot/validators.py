from bot.exceptions import ValidationError

VALID_SIDES = {"BUY", "SELL"}
VALID_TYPES = {"MARKET", "LIMIT", "STOP_LIMIT"}


def validate_symbol(symbol):
    if not symbol or len(symbol) < 6:
        raise ValidationError("Invalid symbol")


def validate_side(side):
    if side not in VALID_SIDES:
        raise ValidationError("Side must be BUY or SELL")


def validate_order_type(order_type):
    if order_type not in VALID_TYPES:
        raise ValidationError(f"Order type must be one of {VALID_TYPES}")


def validate_quantity(qty):
    try:
        qty = float(qty)
        if qty <= 0:
            raise ValidationError("Quantity must be > 0")
        return qty
    except:
        raise ValidationError("Invalid quantity")


def validate_price(price, order_type):
    if order_type in {"LIMIT", "STOP_LIMIT"}:
        if price is None:
            raise ValidationError("Price required")
        return float(price)


def validate_stop_price(stop_price, order_type):
    if order_type == "STOP_LIMIT":
        if stop_price is None:
            raise ValidationError("Stop price required")
        return float(stop_price)