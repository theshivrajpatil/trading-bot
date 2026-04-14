import streamlit as st
from bot.orders import place_order

st.title("Trading Bot UI")

symbol = st.text_input("Symbol", "BTCUSDT")
side = st.selectbox("Side", ["BUY", "SELL"])
order_type = st.selectbox("Type", ["MARKET", "LIMIT", "STOP_LIMIT"])
qty = st.number_input("Quantity", min_value=0.0)

price = None
stop_price = None

if order_type in ["LIMIT", "STOP_LIMIT"]:
    price = st.number_input("Price", min_value=0.0)

if order_type == "STOP_LIMIT":
    stop_price = st.number_input("Stop Price", min_value=0.0)

if st.button("Place Order"):
    try:
        res = place_order(symbol, side, order_type, qty, price, stop_price)
        st.success("Order placed")
        st.json(res)
    except Exception as e:
        st.error(str(e))