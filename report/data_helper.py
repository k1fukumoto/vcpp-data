import pandas as pd
from matplotlib import pyplot as plt
import datetime
import numpy as np

CSV_FILES = [
    '../data/GlobalUsageReport_02-22-2018.csv',
    '../data/GlobalUsageReport.csv'
]

def swap_month_date(dt):
    _dt = dt
    if (dt.year == 2018):
        _dt = datetime.datetime(dt.year,dt.day,dt.month)
        
    return _dt
        
def load_one_file(file):
    print('Start reading {}...'.format(file),end='')
    df = pd.read_csv(file,encoding="ISO-8859-1") #,parse_dates=['Usage Period'])
    df['Usage Period'] = pd.to_datetime(df['Usage Period']).map(swap_month_date)
    print(' {:,} records found'.format(df.shape[0]))
    return df
    
def load_files(files):
    return pd.concat(list(map(load_one_file,files))).drop_duplicates(subset=['Service Provider','Usage Period','SKU','Contract No','Site Name'],keep='first')
