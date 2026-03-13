import yfinance as yf
from crewai.tools import tool

@tool("get_stock_data")
def get_stock_data(ticker: str):
    """Fetches 5 day closing prices, current price and average volume for a given stock ticker."""

    stock = yf.Ticker(ticker)
    hist = stock.history(period="5d")
    average_volume=hist["Volume"].mean()

    result={"ticker":ticker,
            "5_day_closing_prices":hist["Close"].tolist(),
            "current_price":float(hist["Close"].iloc[-1]),
            "average_volume":float(average_volume)}
    return result