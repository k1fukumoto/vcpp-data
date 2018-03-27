#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
from matplotlib import pyplot as plt
from defines import *

def format_chart(data,opts={}):
    ax = plt.gca()
#for cols in data[1:,:]:
#    ax.annotate(cols[0],
#                xy=(cols[4],cols[3]), 
#                xytext=(cols[4],cols[3]))

# Grid
    ax.minorticks_on()
    ax.grid(True, which='both')

    ax.xaxis.grid(which="major", color='black', linestyle='dashed', linewidth=.3)
    ax.yaxis.grid(which="major", color='black', linestyle='dashed', linewidth=.3)
    ax.yaxis.grid(which="minor", color='black', linestyle='dashed', linewidth=.3)

# Axis Label
    ax.set_xticklabels(['${:,.0f}K'.format(x/1000) for x in ax.get_xticks()])
    ax.set_xlabel('YoY QRR Increase')
    ax.set_yticklabels(['+{:.0f}%'.format(y*100) for y in ax.get_yticks()])
    ax.set_ylabel('YoY QRR Growth')

   # Legend
    if not 'no_legend' in opts.keys():
        ax.legend(loc="upper right")       
   
#    plt.gcf().set_size_inches(10,20)
#    plt.plot([0, 1500000], [0.27, 0.27], color='tomato', linestyle='-', linewidth=2)

    plt.title('Revenue Size vs Growth Distribution')
    
    annotate_sp_name(ax,data,opts)


def build_size_growth_table(df,opts,time_frame='LAST_12',group_key='Service Provider'):
    df_last = df[(df['Usage Period'] >= END_QUARTER[0]) & (df['Usage Period'] <= END_QUARTER[2])]
    df_prev = df[(df['Usage Period'] >= START_QUARTER[0]) & (df['Usage Period'] <= START_QUARTER[2])]
    s_last = df_last.groupby(group_key)['Value (USD)'].sum().sort_values(ascending=False)
    s_prev = df_prev.groupby(group_key)['Value (USD)'].sum().sort_values(ascending=False)

    data = np.array(['Service Provider','Previous','Latest','Growth','Increse','GEO','Country'])

    for sp in s_last.index:
        if sp in s_prev.index:
            prev = s_prev.loc[sp]
            last = s_last.loc[sp]
            if prev > 0 and (last-prev)>opts['min_rev_growth'] and last/prev < 50: # One company grew +12000%
                df_sp = df_last[df_last[group_key]==sp]
                country = df_sp.groupby('Country')['Value (USD)'].sum().sort_values(ascending=False).index[0]
                geo = COUNTRY2GEO[country]
                growth = last/prev-1
                if(time_frame == 'LAST_12'):
                    data = np.vstack([data,[sp,prev,last,growth,last-prev,geo,country]])
                elif(time_frame == 'NEXT_12'):
                    data = np.vstack([data,[sp,last,last*(growth+1),growth,last*growth,geo,country]])    
    return data
    
def annotate_sp_name(ax,data,opts):
    if ('show_sp_name' in opts.keys()):        
        for row in data[1:,:][data[1:,4].astype(float) > float(opts['show_sp_name'])]:
            print('{:40} {:16} ({}) ${:10,.0f} ({:,.0f}%)'.format(row[0],row[6],row[5],float(row[4]),float(row[3])*100))
            ax.annotate(row[0],
                        xy=(float(row[4]),float(row[3])), 
                        xytext=(float(row[4]),float(row[3])))      
        
def plot(df,opts={},time_frame='LAST_12',group_key='Service Provider'):
    data = build_size_growth_table(df,opts,time_frame,group_key)
    ax = plt.gca()
    
    if 'NO_SLICE' in opts['type']:
        plt.scatter(data[1:,4].astype(np.float),data[1:,3].astype(np.float),s=data[1:,2].astype(np.float)/1000,alpha=0.6)

        opts['no_legend'] = True
        format_chart(data,opts)
        plt.show()

    if 'RANK' in opts['type']:
        ranges=[[1,20],[21,50],[51,data.shape[0]-1]]
        for r in ranges:
            plt.scatter(data[r[0]:r[1],4],data[r[0]:r[1],3],s=data[r[0]:r[1],2].astype(np.float)/2000,alpha=0.6,label='{} - {}'.format(r[0],r[1]))

        format_chart(data,opts)
        plt.show()

    if 'GEO' in opts['type']:
        geos=['AMER','APAC','EMEA']    
        for geo in geos:
            geo_data = data[data[:,5]==geo]
            geo_data = geo_data[geo_data[:,4].astype(float) < 10000000.0]
            plt.scatter(geo_data[:,4],geo_data[:,3],s=geo_data[:,2].astype(np.float)/2000,alpha=0.6,label=geo)
            annotate_sp_name(ax,geo_data,opts)
    
        format_chart(geo_data,opts)
        plt.show()
    

#    apac_data = data[data[:,5]=='APAC']    
#    for c in sorted(set(apac_data[:,6])):
#        c_data = apac_data[apac_data[:,6]==c]
#        plt.scatter(c_data[:,4],c_data[:,3],s=c_data[:,2].astype(np.float)/1000,alpha=0.6,label=c)
#    format_chart()
#    plt.show()
    