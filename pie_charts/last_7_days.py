from dotenv import load_dotenv
import os
from utils.chart_utils import read_csv_file, filter_data_by_days
from utils.plot_utils import plot_pie_chart

# Load environment variables
load_dotenv()

# Read the CSV file
filename = os.getenv("FILE_NAME")
data = read_csv_file(filename)

# Filter data for the last 7 days
filtered_data = filter_data_by_days(data, 7)

# Filter out negative values (spending) and calculate total spending and earnings
positive_values = filtered_data[filtered_data['Bedrag'] >= 0]['Bedrag'].sum()
negative_values = filtered_data[filtered_data['Bedrag'] < 0]['Bedrag'].sum()

# Plot the pie chart
plot_pie_chart([abs(negative_values), positive_values], ['Spending', 'Earnings'], 'Spending vs Earnings for the Last 7 Days', '../output/last_7_days_piechart.png')
