#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from matplotlib import pyplot as plt
from functools import reduce
import pandas as pd
from defines import *


def format_trend_chart(yticklabel='{:,.0f}K'):
    ax = plt.gca()
    # grids
    ax.yaxis.grid(which="major", color='black', linestyle='dashed', linewidth=.3)
    ax.xaxis.grid(which="minor", color='black', linestyle='dashed', linewidth=.3)

    # y axis ticks
    ax.set_yticklabels([yticklabel.format(x/1000) for x in ax.get_yticks()])

    # legend
    ax.legend(loc="lower left", bbox_to_anchor=(1,0))

    # x axis
    plt.gcf().autofmt_xdate() 
    
    return ax


def plot_trend_chart(df,key_ts='Usage Period',key_rev='Value (USD)'):
    df.groupby(key_ts)[key_rev].sum().plot()
    format_trend_chart()
    plt.show()
    
def data_vcpp_trend(df):
    df_by_up = df.groupby('Usage Period')

    rev = df_by_up['Value (USD)'].sum()
    pc = pd.Series(list(map(lambda x: len(x), df_by_up['Service Provider'].unique())),index=rev.index)
    
    x0=pc.loc[END_MONTH.replace(year=END_MONTH.year-1)]
    x1=pc.loc[END_MONTH]
    print("YoY Partner Count Growth: +{:.0f}%".format((x1/x0-1)*100))

    x0 = reduce(lambda x,y:x+y,map(lambda x: rev.loc[x],map(lambda x: x.replace(year=x.year-1),END_QUARTER)))
    x1 = reduce(lambda x,y:x+y,map(lambda x: rev.loc[x],END_QUARTER))
    growth = 100*(x1/x0-1)
    print("YoY Quarterly Revenue Growth : +{:.0f}%".format(growth))
    
    return rev.index, rev.values, pc.values
    
    
def plot_vcpp_trend(df):
    x, y1, y2 = data_vcpp_trend(df)
    
    plt.close()
    fig,ax1 = plt.subplots()
    ax2 = ax1.twinx()
    
    ax1.bar(x,y1,10,label='Total Revenue')
    ax1.yaxis.grid(which="major", color='black', linestyle='dashed', linewidth=.3)
    ax1.set_yticklabels(['${:,.0f}K'.format(x/1000) for x in ax1.get_yticks()])
    ax1.set_ylabel('vCAN Total MRR')
    ax1.legend(loc="lower right", bbox_to_anchor=(1,0))
    
    ax2.plot(x,y2,'o-',c='tomato',label='Partner Count')    
    ax2.set_ylim(bottom=3500,top=5500)
    ax2.set_ylabel('vCAN Partner Count')
    ax2.legend(loc="lower right", bbox_to_anchor=(1,0.1))
    
    fig = plt.gcf()
    fig.autofmt_xdate() 
    plt.title("VCPP Revenue & Partner Count")
    fig.set_size_inches(10,6)
    plt.show()
    
def plot_size_growth(sps,rev,rate,siz):    
    plt.scatter(rev,rate,s=siz/500,alpha=0.6)
                
    ax = plt.gca()
    for i,sp in enumerate(sps):
        ax.annotate(sp,xy=(rev[i],rate[i]), xytext=(rev[i],rate[i]))      

    ax.minorticks_on()
    ax.grid(True, which='both')

    ax.xaxis.grid(which="major", color='black', linestyle='dashed', linewidth=.3)
    ax.yaxis.grid(which="major", color='black', linestyle='dashed', linewidth=.3)
    ax.yaxis.grid(which="minor", color='black', linestyle='dashed', linewidth=.3)

    ax.set_xticklabels(['${:,.0f}K'.format(x/1000) for x in ax.get_xticks()])
    ax.set_xlabel('YoY QRR Increase')
    ax.set_yticklabels(['+{:,.0f}%'.format(y) for y in ax.get_yticks()])
    ax.set_ylabel('YoY QRR Growth')

    plt.gcf().set_size_inches(12,6)
 
    plt.title('Revenue Size vs Growth Distribution')
    
    
from scipy.optimize import curve_fit

def fn_rev_growth(x,a,b):
    return b*a**x

def calc_growth_rate(df,alpha=1.0,beta=-0.5,plot=False,fit=True):
    df = df[['Usage Period','Value (USD)']].groupby(['Usage Period']).sum().reset_index()

    month_ago_rev = df['Value (USD)'].shift(1)
    mom_growth = (df['Value (USD)'] - month_ago_rev)/month_ago_rev
    mom_growth_dev = abs((mom_growth - mom_growth.mean())/mom_growth.std())

    popt = [.0,.0]
    if fit:
        popt, pcov = curve_fit(fn_rev_growth,
                               df.index[(mom_growth_dev<alpha) & (mom_growth > beta)],
                               df[(mom_growth_dev<alpha) & (mom_growth > beta)]['Value (USD)'])

    if plot:
        plt.bar(df['Usage Period'],df['Value (USD)'],15)
        if fit:
            print('growth: {}'.format(popt[0]**12))
            print('base  : {}'.format(popt[1]))
            
            plt.plot(df['Usage Period'],fn_rev_growth(df.index,popt[0],popt[1]),dashes=[6,2])
            plt.bar(df[(mom_growth_dev>=alpha) | (mom_growth <= beta)]['Usage Period'],
                    df[(mom_growth_dev>=alpha) | (mom_growth <= beta)]['Value (USD)'],15)
        fig = plt.gcf()
        fig.autofmt_xdate() 
        plt.show()   

    return popt
    