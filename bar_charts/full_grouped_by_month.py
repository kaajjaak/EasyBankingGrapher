from dotenv import load_dotenv
import os
from utils.chart_utils import read_csv_file, filter_negative_values
from utils.plot_utils import plot_bar_chart

# Load environment variables
load_dotenv()

# Read the CSV file
filename = os.getenv("FILE_NAME")
data = read_csv_file(filename)

# Filter out the negative values (spending)
negative_values = filter_negative_values(data)

# Group data by month
negative_values['Month'] = negative_values['Uitvoeringsdatum'].dt.to_period('M')
monthly_spending = negative_values.groupby('Month')['Bedrag'].sum().reset_index()

# Plot the bar chart using the function from plot_utils
plot_bar_chart(monthly_spending['Month'].astype(str), monthly_spending['Bedrag'], xlabel='Month', ylabel='Spending', title='Spending for All Data Grouped by Month', save_file='../output/spending_by_month.png')
