import yfinance as yf
import matplotlib.pyplot as plt
import plotly.graph_objects as go

tickers = ['NVDA', 'AAPL']



data = yf.download("AAPL", start="2020-01-01", end="2021-01-01")
data['Close'].plot()
plt.title("Apple Stock Prices")
plt.show()