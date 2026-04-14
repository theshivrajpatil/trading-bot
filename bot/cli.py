import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from bot.orders import place_order
from bot.validators import *
from bot.exceptions import ValidationError, OrderExecutionError


def ask(prompt, required=True):
    while True:
        value = input(prompt).strip()
        if value or not required:
            return value
        print("Required field.")


def main():
    print("\nTrading Bot (Testnet)\n")

    try:
        symbol = ask("Symbol (BTCUSDT): ").upper()
        side = ask("Side (BUY/SELL): ").upper()
        order_type = ask("Type (MARKET/LIMIT/STOP_LIMIT): ").upper()
        qty = ask("Quantity: ")

        price = None
        stop_price = None

        if order_type in {"LIMIT", "STOP_LIMIT"}:
            price = ask("Price: ")

        if order_type == "STOP_LIMIT":
            stop_price = ask("Stop Price: ")

        # validation
        validate_symbol(symbol)
        validate_side(side)
        validate_order_type(order_type)
        qty = validate_quantity(qty)
        price = validate_price(price, order_type)
        stop_price = validate_stop_price(stop_price, order_type)

        print("\n--- Order Summary ---")
        print(symbol, side, order_type, qty, price, stop_price)

        confirm = ask("Confirm (yes/no): ").lower()
        if confirm != "yes":
            print("Cancelled.")
            return

        order = place_order(symbol, side, order_type, qty, price, stop_price)

        print("\nSuccess")
        print("Order ID:", order.get("orderId"))
        print("Status:", order.get("status"))

    except ValidationError as ve:
        print(f"\nValidation Error: {ve}")

    except OrderExecutionError as oe:
        print(f"\nOrder Error: {oe}")

    except Exception as e:
        print(f"\nUnexpected Error: {e}")


if __name__ == "__main__":
    main()