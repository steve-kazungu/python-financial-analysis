import yfinance as yf

#Get Apple stock data
stock = yf.Ticker("TSLA")
data = stock.history(period ="6mo")

#Get the closing prices
prices = data['Close']

#Calculate metrics
average = prices.mean()
latest = prices.iloc[-1]
highest = prices.max()
lowest = prices.min()

#Print results
print("Stock: TSLA")
print("Average price: $" , round(average , 2))
print("Latest price: $" , round(latest , 2))
print("Highest price: $", round(highest , 2))
print("Lowest price: $", round(lowest , 2))