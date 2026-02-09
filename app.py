import streamlit as st
import yfinance as yf
import pandas as pd
from indicators import calculate_rsi

st.title("📊 Crypto Analytics Dashboard")

coin = st.selectbox(
    "Select cryptocurrency:",
    ["BTC-USD", "ETH-USD", "SOL-USD"]
)

data = yf.download(coin, period="6mo")["Close"]

rsi = calculate_rsi(data)

st.subheader("Price Chart")
st.line_chart(data)

st.subheader("RSI Indicator")
st.line_chart(rsi)
