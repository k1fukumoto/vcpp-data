#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pandas as pd
import config as cfg

CSVDATA = "../data/GlobalUsageReport.csv"

try:
    df_raw
except NameError:
    df_raw = pd.read_csv(CSVDATA,encoding="ISO-8859-1",parse_dates=['Usage Period'])
    df_raw.loc[df_raw['Partner Group Name'] == 'Dimension Data','Partner Group Name'] = 'NTT'

df_raw.groupby('Usage Period')['Value (USD)'].sum().plot()

df = df_raw[(df_raw['Usage Period']<=cfg.LAST_QUARTER[2]) & (df_raw['Usage Period']>=cfg.PREV_QUARTER[0])]

