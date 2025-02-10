import yfinance as yf

# Download 10-Year Treasury Yield daily data
data = yf.download('^TNX', start='1995-01-01', end='2024-12-31')['Close']
print(data)

# Save data to a CSV file
data.to_csv('rf_data.csv')