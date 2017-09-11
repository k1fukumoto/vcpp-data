#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import config as cfg
import plot_helper as ph
from matplotlib import pyplot as plt

def plot(df):
    # sort by revenue size at the last month
    df_lm = df[df['Usage Period'] == cfg.LAST_QUARTER[2]]

    s_sp = df_lm[df_lm['Partner Group Name'] == 'NTT'].groupby('Service Provider')['Value (USD)'].sum().sort_values(ascending=False)

    for sp in s_sp.index:
        s_sprev = df[df['Service Provider'] == sp].groupby('Usage Period')['Value (USD)'].sum()
    
        # populate 0s for all months to capture no-report months
#        for i in up_index:
#            if not i in partner_rev.keys():
#                partner_rev.set_value(i,0.0)
#                data = partner_rev.sort_index()
    
        plt.plot(s_sprev.index,s_sprev.values,'o-',label=sp)

    ph.format_trend_chart()

    plt.title('NTT Group Revenue Trend Chart')
    plt.show()
    
plot(df)