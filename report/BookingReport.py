#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd
import config as cfg
from matplotlib import pyplot as plt
import plot_helper as ph
import datetime
import math

CSVDATA = "../data/BookingsReport.csv"

def first_date_of_month(x):
    if(math.isnan(x.year)):
        return math.nan
    else:
        return datetime.date(x.year,x.month,1)
    
try:
    df_raw
except NameError:
    df_raw = pd.read_csv(CSVDATA,encoding="ISO-8859-1",parse_dates=['CMO'])
    
    CMO_month = list(map(lambda x: first_date_of_month(pd.Timestamp(x)),df_raw['CMO'].values))
    df_raw['CMO_month'] = pd.Series(CMO_month,index=df_raw.index)
    

df = df_raw[(df_raw['Product Group'] == 'VCLOUD AIR NETWORK') &
            (df_raw['Gam Rep'] == 'GLOBAL ACCOUNT-NTT') &
            (df_raw['Ship To Organization'].str.match('NTT DATA'))
            ]

for sp in sorted(set(df['Ship To Organization'])):
    print(sp)

g = df.groupby('CMO_month')['$ Detail Total'].sum()

plt.plot(g.index,g.values,'o-',label='MRR')
ph.format_trend_chart()
plt.show()
#
#    df = df_raw[(df_raw['Usage Period']<=cfg.LAST_QUARTER[2]) & (df_raw['Usage Period']>=cfg.PREV_QUARTER[0])]

#import rev_growth
#rev_growth.plot(df)
#
#import size_vs_growth
#size_vs_growth.plot(df,
#                    {'type':['GEO','RANK'],
#                     'min_rev_growth':10000})

#size_vs_growth.plot(df[(df['Partner Group Name']=='NTT') &
#                       (df['Service Provider']!='NTT DATA Inc.')],
#                    {'type':['NO_SPLIT'],
#                     'min_rev_growth':10000})

#size_vs_growth.plot(df[(df['Country']=='Japan')],
#                    {'type':['NO_SPLIT'],
#                     'min_rev_growth':10000})
#    
#import partner_growth
#partner_growth.plot(df)
