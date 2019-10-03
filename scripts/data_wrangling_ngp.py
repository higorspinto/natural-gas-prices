'''
Data Wrangling Natural Gas Prices

Getting daily Natural Gas Prices from the data source and writing in CSV files.

Source: https://www.eia.gov/dnav/ng/hist/rngwhhdD.htm
'''

import urllib.request
import pandas as pd 

### source names
file_url_source = "https://www.eia.gov/dnav/ng/hist_xls/RNGWHHDd.xls" # Daily Prices
file_name_source = "eia_daily_prices.xls"
sheet_name = "Data 1"

#output names
directory_path = "../data/"
file_daily_name = directory_path + "natural_gas_prices_daily.csv"
file_monthly_name = directory_path + "natural_gas_prices_monthly.csv"
file_annual_name = directory_path + "natural_gas_prices_annual.csv"

### Getting the source file
urllib.request.urlretrieve(file_url_source, file_name_source)

### Reading source file with pandas
df = pd.read_excel(file_name_source, sheet_name, header=None) 
df.columns = ["Date", "Price"]

### Dropping non-data lines
data_starting_line = 3
df = df.iloc[data_starting_line:,]

#Setting right data types
df.Date = df.Date.astype('datetime64')
df.Price = df.Price.astype('float64')

### exporting daily prices on csv file
df.to_csv(file_daily_name, index=False, encoding='utf8')

#Creating Monthly Summary
monthly_summary = df

# Set the datetime column as the index
monthly_summary.index = monthly_summary['Date'] 
monthly_summary = monthly_summary.drop(columns="Date")

# Resampling by month
monthly_summary = monthly_summary.Price.resample('MS').mean()

### exporting daily prices on csv file
monthly_summary.to_csv(file_monthly_name, index=True, header=True, encoding='utf8')

# Creating Annual summary
annual_summary = df

# Set the datetime column as the index
annual_summary.index = annual_summary['Date'] 
annual_summary = annual_summary.drop(columns="Date")

# Resampling by year
annual_summary = annual_summary.Price.resample('YS').mean()

### exporting annual prices on csv file
annual_summary.to_csv(file_annual_name, index=True, header=True, encoding='utf8')

