from dotenv import load_dotenv
import os
import pandas as pd
from datetime import timedelta
from utils.chart_utils import read_csv_file, filter_negative_values, filter_data_by_days
from utils.plot_utils import plot_bar_chart

# Load environment variables
load_dotenv()

# Read the CSV file
filename = os.getenv("FILE_NAME")
data = read_csv_file(filename)

# Filter out the negative values (spending)
negative_values = filter_negative_values(data)

# Filter data from the last 30 days
filtered_data = filter_data_by_days(negative_values, 30)

# Group data by day
filtered_data.loc[:, 'Day'] = filtered_data['Uitvoeringsdatum'].dt.to_period('D')
daily_spending = filtered_data.groupby('Day')['Bedrag'].sum().reset_index()

# Create a complete date range for the last 30 days
latest_date = filtered_data['Uitvoeringsdatum'].max().to_period('D').to_timestamp()
date_range = pd.date_range(latest_date - timedelta(days=29), latest_date).to_period('D')

# Merge the complete date range with the spending data
daily_spending = daily_spending.set_index('Day').reindex(date_range).fillna(0).reset_index().rename(columns={'index': 'Day'})

# Plot the bar chart using the function from plot_utils
plot_bar_chart(daily_spending['Day'].astype(str), daily_spending['Bedrag'], xlabel='Day', ylabel='Spending', title='Spending Over the Last 30 Days Grouped by Day', save_file='../output/last_30_days.png')
