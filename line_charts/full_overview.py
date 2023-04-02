from dotenv import load_dotenv
import os
from utils.chart_utils import read_csv_file, filter_negative_values
from utils.plot_utils import plot_line_chart

# Load environment variables
load_dotenv()

# Read the CSV file
filename = os.getenv("FILE_NAME")
data = read_csv_file(filename)

# Filter out the negative values (spending)
negative_values = filter_negative_values(data)

# Group data by day
negative_values['Day'] = negative_values['Uitvoeringsdatum'].dt.to_period('D')
daily_spending = negative_values.groupby('Day')['Bedrag'].sum().reset_index()

# Plot the line chart using the function from plot_utils
plot_line_chart(daily_spending['Day'].astype(str), daily_spending['Bedrag'], xlabel='Day', ylabel='Spending', title='Spending for All Data Grouped by Day', save_file='../output/spending_by_day.png')
