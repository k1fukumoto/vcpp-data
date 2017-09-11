#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
from matplotlib import pyplot as plt
import config as cfg

def format_chart(opts={}):
    ax = plt.gca()
#for cols in data[1:,:]:
#    ax.annotate(cols[0],
#                xy=(cols[4],cols[3]), 
#                xytext=(cols[4],cols[3]))

# Grid
    ax.xaxis.grid(which="major", color='black', linestyle='dashed', linewidth=.3)
    ax.yaxis.grid(which="major", color='black', linestyle='dashed', linewidth=.3)
# Axis Label
    ax.set_xticklabels(['${:,.0f}K'.format(x/1000) for x in ax.get_xticks()])
    ax.set_xlabel('YoY QRR Increase')
    ax.set_yticklabels(['+{:.0f}%'.format(y*100) for y in ax.get_yticks()])
    ax.set_ylabel('YoY QRR Growth')
# Legend
    if not 'no_legend' in opts.keys():
        ax.legend(loc="upper right")
    
    plt.gcf().set_size_inches(10,6)
    plt.title('Revenue Size vs Growth Distribution')

def build_size_growth_table(df,opts):
    df_last = df[(df['Usage Period'] >= cfg.LAST_QUARTER[0]) & (df['Usage Period'] <= cfg.LAST_QUARTER[2])]
    df_prev = df[(df['Usage Period'] >= cfg.PREV_QUARTER[0]) & (df['Usage Period'] <= cfg.PREV_QUARTER[2])]
    s_last = df_last.groupby('Service Provider')['Value (USD)'].sum().sort_values(ascending=False)
    s_prev = df_prev.groupby('Service Provider')['Value (USD)'].sum().sort_values(ascending=False)

    data = np.array(['Service Provider','Previous','Latest','Growth','Increse','GEO','Country'])

    for sp in s_last.index:
        if sp in s_prev.index:
            prev = s_prev.loc[sp]
            last = s_last.loc[sp]
            if prev > 0 and (last-prev)>opts['min_rev_growth'] and last/prev < 50: # One company grew +12000%
                df_sp = df_last[df_last['Service Provider']==sp]
                country = df_sp.groupby('Country')['Value (USD)'].sum().sort_values(ascending=False).index[0]
                geo = cfg.COUNTRY2GEO[country]
                growth = last/prev-1
#                data = np.vstack([data,[sp,prev,last*(last/prev-1),growth,last-prev,geo,country]])
                data = np.vstack([data,[sp,prev,last,growth,last-prev,geo,country]])
                if last-prev >300000:
                    print('{:32} {:12} ({}) ${:10,.0f} ({:.0f}%)'.format(sp,country,geo,last-prev,growth*100))
    return data
    
def plot(df,opts={}):
    data = build_size_growth_table(df,opts)
    ax = plt.gca()
    
    if 'NO_SLICE' in opts['type']:
        plt.scatter(data[1:,4],data[1:,3],s=data[1:,2].astype(np.float)/2000,alpha=0.6)

        format_chart({'no_legend': True})
        
        for cols in data[1:,:]:
            ax.annotate(cols[0],
                        xy=(cols[4],cols[3]), 
                        xytext=(cols[4],cols[3]))
        plt.show()

    if 'RANK' in opts['type']:
        ranges=[[1,20],[21,50],[51,data.shape[0]-1]]
        for r in ranges:
            plt.scatter(data[r[0]:r[1],4],data[r[0]:r[1],3],s=data[r[0]:r[1],2].astype(np.float)/2000,alpha=0.6,label='{} - {}'.format(r[0],r[1]))
        
        for row in data[1:,:][data[1:,4].astype(float) > 500000.0]:
            ax.annotate(row[0],
                        xy=(row[4],row[3]), 
                        xytext=(row[4],row[3]))
        format_chart()
        plt.show()

    if 'GEO' in opts['type']:
        geos=['AMER','APAC','EMEA']    
        for geo in geos:
            geo_data = data[data[:,5]==geo]
            plt.scatter(geo_data[:,4],geo_data[:,3],s=geo_data[:,2].astype(np.float)/2000,alpha=0.6,label=geo)
    
        format_chart()
        plt.show()

#    apac_data = data[data[:,5]=='APAC']    
#    for c in sorted(set(apac_data[:,6])):
#        c_data = apac_data[apac_data[:,6]==c]
#        plt.scatter(c_data[:,4],c_data[:,3],s=c_data[:,2].astype(np.float)/1000,alpha=0.6,label=c)
#    format_chart()
#    plt.show()

plot(df,
     {'type':['GEO','RANK'],
      'min_rev_growth':10000})

plot(df[(df['Partner Group Name']=='NTT') &
        (df['Service Provider']!='NTT DATA Inc.')],
    {'type':['NO_SLICE'],
     'min_rev_growth':10000})
    
plot(df[(df['Country']=='Japan')],
    {'type':['NO_SLICE'],
     'min_rev_growth':10000})
    