from bot.client import get_client
from bot.logger import get_logger
from bot.exceptions import OrderExecutionError

logger = get_logger()


def place_order(symbol, side, order_type, quantity, price=None, stop_price=None):
    client = get_client()

    try:
        logger.info(f"Request: {symbol} {side} {order_type} qty={quantity}")

        if order_type == "MARKET":
            response = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=quantity
            )

        elif order_type == "LIMIT":
            response = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="LIMIT",
                quantity=quantity,
                price=price,
                timeInForce="GTC"
            )

        elif order_type == "STOP_LIMIT":
            response = client.futures_create_order(
                symbol=symbol,
                side=side,
                type="STOP",
                quantity=quantity,
                price=price,
                stopPrice=stop_price,
                timeInForce="GTC"
            )

        else:
            raise OrderExecutionError("Unsupported order type")

        logger.info(f"Response: {response}")
        return response

    except Exception as e:
        logger.error(f"Error: {str(e)}")
        raise OrderExecutionError(str(e))