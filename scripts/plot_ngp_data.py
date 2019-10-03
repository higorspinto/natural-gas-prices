'''
Plot Natural Gas Prices Data

Plotting NGP data in static files.
'''

import pandas as pd
import matplotlib.pyplot as plt 

# input file names
directory_path = "../data/"
file_daily_name = directory_path + "natural_gas_prices_daily.csv"
file_monthly_name = directory_path + "natural_gas_prices_monthly.csv"
file_annual_name = directory_path + "natural_gas_prices_annual.csv"

# reading data
df_daily = pd.read_csv(file_daily_name) 
df_monthly = pd.read_csv(file_monthly_name)
df_annual = pd.read_csv(file_annual_name)

# png file names
static_dir_path = "../static/"
daily_png_file_name = static_dir_path + "ngp_daily.png"
monthly_png_file_name = static_dir_path + "ngp_monthly.png"
annual_png_file_name = static_dir_path + "ngp_annual.png"

#ploting daily data
fig, ax1 = plt.subplots()

ax1.plot(df_daily.Date, df_daily.Price)
ax1.set_ylabel('Price (Dollars per Million Btu)')

plt.xticks(rotation='vertical')
ax1.xaxis.set_major_locator(plt.MaxNLocator(20))
plt.tight_layout()
plt.savefig(daily_png_file_name)


#ploting monthly data
fig, ax1 = plt.subplots()

ax1.plot(df_monthly.Date, df_monthly.Price)
ax1.set_ylabel('Price (Dollars per Million Btu)')

plt.xticks(rotation='vertical')
ax1.xaxis.set_major_locator(plt.MaxNLocator(20))
plt.tight_layout()
plt.savefig(monthly_png_file_name)

#ploting annual data
fig, ax1 = plt.subplots()

ax1.plot(df_annual.Date, df_annual.Price)
ax1.set_ylabel('Price (Dollars per Million Btu)')

plt.xticks(df_annual.Date, pd.DatetimeIndex(df_annual.Date).year, rotation='vertical')
plt.tight_layout()
plt.savefig(annual_png_file_name)



