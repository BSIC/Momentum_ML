import yfinance as yf

# Download S&P 500 daily data
data = yf.download('^GSPC', start='1995-01-01', end='2024-12-31')[['Close']]
# print((data['Close'] == data['Adj Close']).all())

# Save data to a CSV file
data.to_csv('s&p500_data.csv')