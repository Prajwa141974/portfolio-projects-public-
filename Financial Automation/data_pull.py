import yfinance as yf
from config import PRICE_PERIOD

def pull_financial_data(tickers=None):
    if tickers is None:
        from config import TICKERS
        tickers = TICKERS
    data = {}
    for symbol in tickers:
        print('Fetching ' + symbol + '...')
        ticker = yf.Ticker(symbol)
        prices = ticker.history(period=PRICE_PERIOD)
        balance_sheet = ticker.balance_sheet
        income_stmt = ticker.income_stmt
        cashflow = ticker.cashflow
        data[symbol] = {'prices': prices, 'balance_sheet': balance_sheet, 'income_stmt': income_stmt, 'cashflow': cashflow}
    return data
