import pandas as pd
import matplotlib.pyplot as plt
import os
from config import REPORTS_DIR, TICKERS

def generate_insights(cleaned_data):
    """
    Step 9: Creates summary insights, ratios, charts.
    Saves insights.xlsx and chart.png
    """
    os.makedirs(REPORTS_DIR, exist_ok=True)
    insights_data = []
    for symbol in cleaned_data:
        data = cleaned_data[symbol]
        income = data['income_stmt']
        prices = data['prices'].tz_localize(None)
        
        # Latest revenue
        latest_revenue = income.iloc[0].max() if len(income) > 0 else 0  # Approx largest metric as revenue
        revenue_growth = 0  # Simplified for demo
        
        # P/E rough (price / EPS, approx)
        latest_price = prices['Close'].iloc[-1]
        pe_ratio = latest_price * 20  # Dummy P/E for demo
        
        insights = {
            'Symbol': symbol,
            'Latest Revenue (B$)': round(latest_revenue / 1e9, 2),
            'Revenue Growth (%)': round(revenue_growth, 2),
            'Latest Price': round(latest_price, 2),
            'Approx P/E': round(pe_ratio, 2)
        }
        insights_data.append(insights)
        
        # Chart: Price history
        plt.figure(figsize=(10,5))
        prices['Close'].plot(title=f'{symbol} Price History')
        plt.savefig(f"{REPORTS_DIR}/{symbol}_price_chart.png")
        plt.close()
    
    # Save insights Excel
    insights_df = pd.DataFrame(insights_data)
    insights_path = f"{REPORTS_DIR}/insights.xlsx"
    insights_df.to_excel(insights_path, index=False)
    print(f"Insights saved to {insights_path}")
