import pandas as pd
from config import TICKERS

def clean_financial_data(raw_data):
    """Cleans data: dropna, fillna, numeric."""

    cleaned = {}
    for symbol in raw_data:
        dfs = raw_data[symbol]
        cleaned_symbol = {}
        # Prices
        cleaned_symbol['prices'] = dfs['prices'].dropna().tz_localize(None)
        # Financials
        for stmt in ['balance_sheet', 'income_stmt', 'cashflow']:
            df = dfs[stmt].fillna(0)
            df = df.apply(pd.to_numeric, errors='coerce').fillna(0)
            cleaned_symbol[stmt] = df
        cleaned[symbol] = cleaned_symbol
    return cleaned
