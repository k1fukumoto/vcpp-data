#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import config as cfg
from matplotlib import pyplot as plt

def plot_hist(data_prev,data_last,cutoff,title):
    plt.hist(data_last[:int(len(data_last)*cutoff)],bins=100,alpha=.8,label='2017 Q1')
    plt.hist(data_prev[:int(len(data_last)*cutoff)],bins=100,alpha=.8,label='2016 Q1')

    plt.xlabel("Quarterly Revenue (USD)")
    plt.ylabel("Number of Service Providers")
    plt.title(title)
    ax = plt.gca()
    fig = plt.gcf()
    ax.set_xticklabels(['${:,.0f}K'.format(x/1000) for x in ax.get_xticks()])
    ax.legend(loc="upper right")
    fig.set_size_inches(10,6)
    plt.show()
    
def plot(df):
    df_last_q = df[(df['Usage Period'] >= cfg.LAST_QUARTER[0]) & (df['Usage Period'] <= cfg.LAST_QUARTER[2])]
    df_prev_q = df[(df['Usage Period'] >= cfg.PREV_QUARTER[0]) & (df['Usage Period'] <= cfg.PREV_QUARTER[2])]
    data_last = df_last_q.groupby('Service Provider')['Value (USD)'].sum().sort_values(ascending=False)
    data_prev = df_prev_q.groupby('Service Provider')['Value (USD)'].sum().sort_values(ascending=False)
    
    plot_hist(data_prev,data_last,1.0,"Revenue Distribution - All SPs")
    plot_hist(data_prev,data_last,0.1,"Revenue Distribution - Top 10% SPs")
    
        
    total_last = df_last_q['Value (USD)'].sum()
    print("Total SP Count: {}".format(len(data_last)))
    print("Top {} SPs Contribution: {:.0f}%".format(10,data_last[:10].sum()/total_last*100))
    
    plt.pie(data_last.values,startangle=90,counterclock=False)
    plt.title('Revenue Distribution')
    plt.gcf().set_size_inches(3,3)
    plt.show()


plot(df)