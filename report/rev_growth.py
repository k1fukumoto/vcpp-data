#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from matplotlib import pyplot as plt
import config as cfg
from functools import reduce

def plot(df):
    fig,ax1 = plt.subplots()
    ax2 = ax1.twinx()

    rev = df.groupby('Usage Period')['Value (USD)'].sum()
    ax1.bar(rev.index,rev.values,10,label='Total Revenue')

    cnt = df.groupby('Usage Period')['Service Provider'].unique()
    pcnts = list(map(lambda x: len(x), cnt.values))
    ax2.plot(cnt.index,pcnts,'o-',c='tomato',label='Partner Count')
    ax2.set_ylim(bottom=3500,top=3500*rev.values.max()/rev.values.min())
    ax2.set_ylabel('vCAN Partner Count')
    ax2.legend(loc="lower right", bbox_to_anchor=(1,0.1))

    x0=len(cnt.loc[cfg.PREV_QUARTER[2]])
    x1=len(cnt.loc[cfg.LAST_QUARTER[2]])

    print("YoY Partner Count Growth: +{:.0f}%".format((x1/x0-1)*100))

    x0=reduce(lambda x,y:x+y,map(lambda x: rev.loc[x],cfg.PREV_QUARTER))
    x1=reduce(lambda x,y:x+y,map(lambda x: rev.loc[x],cfg.LAST_QUARTER))

    print("YoY Revenue Growth: +{:.0f}%".format((x1/x0-1)*100))

    ax1.yaxis.grid(which="major", color='black', linestyle='dashed', linewidth=.3)
    ax1.set_yticklabels(['${:,.0f}K'.format(x/1000) for x in ax1.get_yticks()])
    ax1.set_ylabel('vCAN Total MRR')
    ax1.legend(loc="lower right", bbox_to_anchor=(1,0))

    fig = plt.gcf()
    fig.autofmt_xdate() 
    #plt.title("vCAN Business Trend")
    fig.set_size_inches(10,6)
    plt.show()
    
