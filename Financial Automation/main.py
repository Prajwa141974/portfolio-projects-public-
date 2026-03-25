from data_pull import pull_financial_data
from cleaner import clean_financial_data
from excel_update import update_excel_files
from insights import generate_insights

if __name__ == "__main__":
    while True:
        symbol = input("\nEnter stock symbol (e.g. AAPL, MSFT) or 'quit': ").strip().upper()
        if symbol == 'QUIT':
            print("Goodbye!")
            break
        if not symbol:
            print("No symbol entered. Please try again.")
            continue
        try:
            print(f"=== Generating report for {symbol} ===")
            raw_data = pull_financial_data([symbol])
            if not raw_data:
                print("Ticker '{symbol}' not found. Please check spelling and try again.".format(symbol=symbol))
                continue
            cleaned_data = clean_financial_data(raw_data)
            update_excel_files(cleaned_data)
            generate_insights(cleaned_data)
            print(f"=== {symbol} report ready in reports/ ===")
            print("Enter another or 'quit'")
        except Exception as e:
            print(f"Error with ticker '{symbol}': {{e}}. Please try again.".format(e=e))

