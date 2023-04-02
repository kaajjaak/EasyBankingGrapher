from dotenv import load_dotenv
import os
from utils.chart_utils import read_csv_file, filter_negative_values, filter_data_by_days
from utils.plot_utils import plot_line_chart

# Load environment variables
load_dotenv()

# Read the CSV file
filename = os.getenv("FILE_NAME")
data = read_csv_file(filename)

# Filter out the negative values (spending)
negative_values = filter_negative_values(data)

# Filter data from the last 365 days
filtered_data = filter_data_by_days(negative_values, 365)

# Group data by day
filtered_data['Day'] = filtered_data['Uitvoeringsdatum'].dt.to_period('D')


# Plot the line chart using the function from plot_utils
plot_line_chart(filtered_data['Day'].astype(str), filtered_data['Bedrag'], xlabel='Day', ylabel='Spending', title='Spending Over the Last 365 Days', save_file='../output/last_365_days_linechart.png')
