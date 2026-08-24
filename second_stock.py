import yfinance as yf

def analyze_company(ticker):
    stock = yf.Ticker(ticker)
    income = stock.financials
    balance = stock.balance_sheet

    revenue = income.loc['Total Revenue'].iloc[0]
    net_income = income.loc['Net Income'].iloc[0]
    gross_profit = income.loc['Gross Profit'].iloc[0]
    operating_income = income.loc['Operating Income'].iloc[0] 
    total_equity = balance.loc['Stockholders Equity'].iloc[0]
    total_debt = balance.loc['Total Debt'].iloc[0]

    profit_margin = (net_income/revenue) * 100
    roe = (net_income/total_equity) * 100
    debt_to_equity = total_debt/total_equity

    result = {
        'Revenue': round(revenue , 2),
        'Net Income': round(net_income , 2),
        'Gross Profit': round(gross_profit , 2),
        'Operating Income': round(operating_income , 2),
        'Profit Margin': round(profit_margin , 2),
        'ROE': round(roe , 2),
        'Debt/Equity': round(debt_to_equity , 2)
    }

    return(result)

google = analyze_company("GOOGL")
nvidia = analyze_company("NVDA")
amazon = analyze_company("AMZN")

print("===REVENUE===")
print("GOOGL:", google['Revenue'])
print("NVDA:", nvidia['Revenue'])
print("AMZN:", amazon['Revenue'])

print("===NET INCOME===")
print("GOOGL:", google['Net Income'])
print("NVDA:", nvidia['Net Income'])
print("AMZN:", amazon['Net Income'])

print("===GROSS PROFIT===")
print("GOOGL:", google['Gross Profit'])
print("NVDA:", nvidia['Gross Profit'])
print("AMZN:", amazon['Gross Profit'])

print("===OPERATING INCOME===")
print("GOOGL:", google['Operating Income'])
print("NVDA:", nvidia['Operating Income'])
print("AMZN:", amazon['Operating Income'])

print("===PROFIT MARGIN===")
print("GOOGL:", google['Profit Margin'])
print("NVDA:", nvidia['Profit Margin'])
print("AMZN:", amazon['Profit Margin'])

print("===ROE===")
print("GOOGL:", google['ROE'])
print("NVDA:", nvidia['ROE'])
print("AMZN:", amazon['ROE'])

print("===DEBT/EQUITY===")
print("GOOGL:", google['Debt/Equity'])
print("NVDA:", nvidia['Debt/Equity'])
print("AMZN:", amazon['Debt/Equity'])