import pandas as pd
import numpy as np
from datetime import timedelta


def read_csv_file(file_name):
    data = pd.read_csv(file_name, delimiter=';', parse_dates=['Uitvoeringsdatum'], dayfirst=True)
    return data


def filter_negative_values(data):
    negative_values = data[data['Bedrag'] < 0].copy()
    negative_values.loc[:, 'Bedrag'] = np.abs(negative_values['Bedrag'])
    return negative_values


def filter_data_by_days(data, days):
    latest_date = data['Uitvoeringsdatum'].max()
    days_ago = latest_date - timedelta(days=days)
    filtered_data = data[data['Uitvoeringsdatum'] >= days_ago].copy()
    return filtered_data
