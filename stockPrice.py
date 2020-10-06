import yfinance as yf
import streamlit as st
import datetime
import pandas as pd

st.write("""
# Simple Stock Price App
Shown are the stock closing price and volume of Company of your choice
for given period.
""")


today = datetime.date.today()

# get the data provided by user text_input
def user_input_features():
    ticker = st.text_input("Ticker", 'AMZN')
    start_date = st.text_input("Start Date", '2020-01-01')
    end_date = st.text_input("End Date", f'{today}')
    return ticker, start_date, end_date

tickerSymbol, start, end = user_input_features()
start = pd.to_datetime(start)
end = pd.to_datetime(end)

#get data on this ticker
tickerData = yf.download(tickerSymbol,start,end)

st.write("""
## Closing Price
""")
st.line_chart(tickerData.Close)
st.write("""
## Closing Volume
""")
st.line_chart(tickerData.Volume)
