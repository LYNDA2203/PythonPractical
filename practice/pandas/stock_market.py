'''Dataset Example (AAPL_stock_data.csv):
Date	Open	High	Low	Close	Volume
2024-01-01	150.5	155.0	149.5	154.0	1000000
2024-01-02	154.0	158.0	152.0	157.5	1100000
2024-01-03	157.5	160.0	156.0	158.0	900000
...	...	...	...	...	...'''
import pandas as pd 

#loading the stock data from csv file and displaying  the first 5 rows
stock_data = pd.read_csv("AAPL_stock_data.csv")
print("First 5 rows:\n",stock_data.head())

#daily return percentage based on the close price
stock_data['Daily_return (%)']=stock_data['Close'].pct_change()*100
print("\nDaily Return (%): \n",stock_data[['Date','Daily_return (%)']].head())

#Average closing price of stock
avg_close_price = stock_data['Close'].mean()
print(f"\n Average closing Price:{avg_close_price:.2f}")

#Finding the max and min closing price
max_close_price = max(stock_data['Close'])
min_close_price = min(stock_data['Close'])
print(f"\n Maximum closing price:{max_close_price:.2f} \n Minimum closing price:{min_close_price:.2f}")

#Filter out the days of volume  top 10%
volume_threshold = stock_data['Volume'].quantile(0.9)
high_volume_days = stock_data[stock_data['Volume']>volume_threshold]
print(f"\nHigh Volume Days (>90th percentile):\n",high_volume_days)

#date of highest close value
high_closing_value = stock_data.loc[stock_data['Close'].idxmax(),'Date']
print(f"\n Date with Highest Close Price:{high_closing_value}")

#average of the last 3 closing prices
stock_data['3-day_MA'] = stock_data['Close'].rolling(window=3).mean()
print("\n3-Day Moving Average:\n",stock_data[['Date','Close','3-day_MA']].head(10))