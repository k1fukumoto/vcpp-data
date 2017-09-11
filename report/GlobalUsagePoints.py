#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd
import config as cfg

CSVDATA = "../data/GlobalUsageReport.csv"

try:
    df_raw
except NameError:
    df_raw = pd.read_csv(CSVDATA,encoding="ISO-8859-1",parse_dates=['Usage Period'])
    df_raw.info()

#g = df_raw.groupby('Usage Period')['Value (USD)'].sum()
#g.plot()
#plt.bar(g.index,g.values,10,label='MRR')
#ph.format_trend_chart()
#plt.show()
#
df = df_raw[(df_raw['Usage Period']<=cfg.LAST_QUARTER[2]) & (df_raw['Usage Period']>=cfg.PREV_QUARTER[0])]

df_raw.loc[df_raw['Partner Group Name'] == 'Dimension Data','Partner Group Name'] = 'NTT'

#print(df_dd)
#['Partner Group Name'] = 'NTT'


#import rev_growth
#rev_growth.plot(df)
#
#import size_vs_growth
#size_vs_growth.plot(df,
#                    {'type':['GEO','RANK'],
#                     'min_rev_growth':10000})
#
#size_vs_growth.plot(df[(df['Partner Group Name']=='NTT') &
#                       (df['Service Provider']!='NTT DATA Inc.')],
#                    {'type':['NO_SLICE'],
#                     'min_rev_growth':10000})
#
#size_vs_growth.plot(df[(df['Country']=='Japan')],
#                    {'type':['NO_SLICE'],
#                     'min_rev_growth':10000})
#    
#import partner_growth
#partner_growth.plot(df)
