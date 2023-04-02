from dotenv import load_dotenv
import os
import pandas as pd
from utils.chart_utils import read_csv_file, filter_negative_values, filter_data_by_days
from utils.plot_utils import plot_bar_chart

# Load environment variables
load_dotenv()

# Read the CSV file
filename = os.getenv("FILE_NAME")
data = read_csv_file(filename)

# Filter out the negative values (spending)
negative_values = filter_negative_values(data)

# Filter data from the last 365 days
filtered_data = filter_data_by_days(negative_values, 365)

# Group data by month
filtered_data.loc[:, 'Month'] = filtered_data['Uitvoeringsdatum'].dt.to_period('M')
monthly_spending = filtered_data.groupby('Month')['Bedrag'].sum().reset_index()

# Create a complete date range for the last 12 months
latest_date = filtered_data['Uitvoeringsdatum'].max().to_period('M').to_timestamp()
date_range = pd.date_range(latest_date - pd.DateOffset(months=11), latest_date, freq='MS').to_period('M')

# Merge the complete date range with the spending data
monthly_spending = monthly_spending.set_index('Month').reindex(date_range).fillna(0).reset_index().rename(columns={'index': 'Month'})

# Plot the bar chart using the function from plot_utils
plot_bar_chart(monthly_spending['Month'].astype(str), monthly_spending['Bedrag'], xlabel='Month', ylabel='Spending', title='Spending Over the Last 365 Days Grouped by Month', save_file='../output/last_365_days_grouped_by_month.png')