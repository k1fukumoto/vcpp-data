#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from matplotlib import pyplot as plt
# import config as cfg
import plot_helper as ph

def plot_rev_trend(data,lbl):
#    plt.plot(data.index,(data.values/data.values[0]-1)*100,'o-',label=lbl,linewidth=5.0,markersize=9.0)
    plt.plot(data.index,(data.values/data.values[0]-1)*100,'o-',label=lbl)
        
def plot(df):
    for d in [
                [df.groupby('Usage Period')['Value (USD)'].sum(),'vCAN Total'],
                [df[df['Partner Status']=='Showcase'].groupby('Usage Period')['Value (USD)'].sum(),'Showcase Total'],
                [df[df['Partner Group Name']=='NTT'].groupby('Usage Period')['Value (USD)'].sum(),'NTT Group Total']
            ]:
        plot_rev_trend(d[0],d[1])
 
    ax = ph.format_trend_chart()
    ax.set_yticklabels(['+{:,.0f}%'.format(x) for x in ax.get_yticks()])

 #   ax.legend(loc="lower right", bbox_to_anchor=(1,0))
    plt.show()