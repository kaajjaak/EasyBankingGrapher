from dotenv import load_dotenv
import os
from utils.chart_utils import read_csv_file
from utils.plot_utils import plot_pie_chart

# Load environment variables
load_dotenv()

# Read the CSV file
filename = os.getenv("FILE_NAME")
data = read_csv_file(filename)

# Calculate total spending and earnings
total_spending = data[data['Bedrag'] < 0]['Bedrag'].sum()
total_earnings = data[data['Bedrag'] >= 0]['Bedrag'].sum()

# Plot the pie chart
plot_pie_chart([abs(total_spending), total_earnings], ['Spending', 'Earnings'], 'Spending vs Earnings', '../output/total_spending_vs_earnings.png')
