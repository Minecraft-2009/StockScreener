import yfinance as yf
import numpy as np
from pandas_datareader import data
import plotly.graph_objects as go


Tickers=["AAPL","GOOG","RY","HPQ"]

# Define the stock symbol and date range
stock_symbol = "AAPL"  # Example: Apple Inc.
start_date = "2023-01-01"
end_date = "2023-12-31"

# Download historical data
stock_data = yf.download(stock_symbol, start=start_date, end=end_date)

specific_date = "2023-06-01"
specific_date_data = stock_data.loc[specific_date]

print(specific_date_data)

fig = go.Figure(data=[go.Candlestick(x=stock_data.index,
                                     open=stock_data['Open'],
                                     high=stock_data['High'],
                                     low=stock_data['Low'],
                                     close=stock_data['Close'])])

fig.update_layout(title=f"{stock_symbol} Stock Prices",
                  xaxis_rangeslider_visible=True)

fig.show()
