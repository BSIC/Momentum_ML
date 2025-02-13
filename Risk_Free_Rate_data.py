import yfinance as yf

# Download 3-Months Bill Yield daily data
data = yf.download('^IRX', start='1995-01-01', end='2024-12-31')['Close']
print(data)

# Save data to a CSV file
data.to_csv('rf_data.csv')