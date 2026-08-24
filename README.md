# python-financial-analysis
Automated stock analysis pulling live data from Yahoo Finance

##Scripts
| File | What it does |
|------| ------------ |
|'firts_stock.py' | Pulls prices, calculates average/ high / low / latest|
|'second_stock.py'| Pulls income statement + balance sheet, calculates 7 metrics for any company|

##Metrics
Revenue, Net Income, Gross Profit, Operating Income, **Profit Margin** ,**ROE**, **Debt_to_Equity**

##Sample OutPut (NVDA vs AMZN vs GOOGL )
| Company | Profit Margin | ROE | D/E |
|NVIDIA   | 55.60%        |76.33%|0.07|
|GOOGLE   |32.81%         |31.83%|0.14|
|AMAZON   |10.83%         |18.89%|0.37|

##Run It
'''bash
pip install yfinance pandas
py second_stock.py
