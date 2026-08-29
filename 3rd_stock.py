import yfinance as yf

#======ASSUMPTIONS======
#Change these to test different scenarios
growth_rate = 0.08 
wacc = 0.08
terminal_growth = 0.025
years = 5

#======PULL DATA======
def get_company_data(ticker):
    """Pull FCF, Cash, Debt and Shares for DCF analysis."""
    stock = yf.Ticker(ticker)
    cashflow = stock.cashflow
    balance = stock.balance_sheet

    #Safety Check
    if cashflow.empty or balance.empty:
        print("No data for " + ticker)
        return None

    #Pull raw numbers
    FCF = cashflow.loc['Free Cash Flow'].iloc[0]
    cash = balance.loc['Cash And Cash Equivalents'].iloc[0]
    total_debt = balance.loc['Total Debt'].iloc[0]
    shares = stock.info['sharesOutstanding']

    return{
        'FCF': round(FCF,2),
        'Cash': round(cash,2),
        'Total Debt':round(total_debt,2),
        'Shares': round(shares,2)
    }

# ====== DCF MODEL======
def run_dcf(data):
    """Calculate Enterprise Value and Fair Stock Price."""
    FCF = data['FCF']

    # Project 5 Years and Discount back
    projected_fcf = FCF
    total_pv = 0

    print("\n=== 5-YEAR PROJECTION ===")
    for year in range(1, years + 1):
        projected_fcf = projected_fcf * (1 + growth_rate)
        pv = projected_fcf / ((1 + wacc) ** year) 
        total_pv = total_pv + pv
        print("Year:", year, "FCF = ", round(projected_fcf, 2), "PV = ",round(pv, 2))

    # Terminal Value
    terminal_value = projected_fcf * (1 + terminal_growth) / (wacc - terminal_growth)
    pv_terminal = terminal_value / ((1 + wacc) ** years)

    # Enterprise Value
    enterprise_value = total_pv + pv_terminal
    equity_value = enterprise_value - data['Total Debt'] + data['Cash']
    price_per_share = equity_value/data['Shares'] 

    return{
        'Terminal Value' : round(terminal_value,2),
        'PV of Terminal': round(pv_terminal,2),
        'Enterprise Value': round(enterprise_value,2),
        'Equity Value': round(equity_value,2),
        'Price per Share': round(price_per_share, 2)
    }

apple = get_company_data("AAPL")
valuation = run_dcf(apple)

print("FCF:" ,apple['FCF'])
print("Cash:",apple['Cash'])
print("Total Debt:",apple['Total Debt'])
print("Shares:", apple['Shares'])
print("Terminal Value:",valuation['Terminal Value'])
print("PV of Terminal:", valuation['PV of Terminal'])
print("Enterprise Value:", valuation['Enterprise Value'])
print("Equity Value:", valuation['Equity Value'])
print("Price per Share:", valuation['Price per Share'])



    




