#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from matplotlib import pyplot as plt

def format_trend_chart():
    ax = plt.gca()
    # grids
    ax.yaxis.grid(which="major", color='black', linestyle='dashed', linewidth=.3)
    ax.xaxis.grid(which="minor", color='black', linestyle='dashed', linewidth=.3)

    # y axis ticks
    ax.set_yticklabels(['${:,.0f}K'.format(x/1000) for x in ax.get_yticks()])

    # legend
    ax.legend(loc="lower left", bbox_to_anchor=(1,0))

    # x axis
    plt.gcf().autofmt_xdate() 
    
    return ax