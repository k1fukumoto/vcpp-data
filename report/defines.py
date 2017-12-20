#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import datetime

RELOAD_CSV = False

CSV_FILE = '../data/GlobalUsageReport.csv'

END_QUARTER = [
               datetime.date(2017,8,1),
               datetime.date(2017,9,1),
               datetime.date(2017,10,1)
               ]
YEAR_AGO_QUARTER = map(lambda x: x.replace(year=x.year-1),END_QUARTER)

START_QUARTER = [
                datetime.date(2016,1,1),
                datetime.date(2016,2,1),
                datetime.date(2016,3,1)
                ]

QUARTER_RANGE = (START_QUARTER,END_QUARTER)

START_MONTH = QUARTER_RANGE[0][0]
END_MONTH = QUARTER_RANGE[1][2]


COUNTRY2GEO = {
        'Algeria': 'EMEA',
        'Argentina': 'AMER',
        'Armenia': 'EMEA',
        'Australia': 'APAC',
        'Austria': 'EMEA',
        'Bahamas': 'AMER',
        'Bangladesh': 'APAC',
        'Belarus': 'EMEA',
        'Belgium': 'EMEA',
        'Bermuda': 'AMER',
        'Bolivia': 'AMER',
        'Bosnia and Herzegovina': 'EMEA',
        'Brazil': 'AMER',
        'Bulgaria': 'EMEA',
        'Canada': 'AMER',
        'Cayman Islands': 'AMER',
        'Chile': 'AMER',
        'China': 'APAC',
        'Colombia': 'AMER',
        'Costa Rica': 'AMER',
        'Croatia': 'EMEA',
        'CuraÃ§ao': 'AMER',
        'Cyprus': 'EMEA',
        'Czech Republic': 'EMEA',
        'Denmark': 'EMEA',
        'Dominican Republic': 'AMER',
        'Ecuador': 'AMER',
        'Egypt': 'EMEA',
        'Estonia': 'EMEA',
        'Faeroe Islands': 'EMEA',
        'Fiji': 'APAC',
        'Finland': 'EMEA',
        'France': 'EMEA',
        'Germany': 'EMEA',
        'Ghana': 'EMEA',
        'Greece': 'EMEA',
        'Greenland': 'EMEA',
        'Guadeloupe': 'EMEA',
        'Guam': 'AMER',
        'Guatemala': 'AMER',
        'Guernsey': 'EMEA',
        'Hong Kong': 'APAC',
        'Hungary': 'EMEA',
        'Iceland': 'EMEA',
        'India': 'APAC',
        'Indonesia': 'APAC',
        'Ireland': 'EMEA',
        'Isle of Man': 'EMEA',
        'Israel': 'EMEA',
        'Italy': 'EMEA',
        'Jamaica': 'AMER',
        'Japan': 'APAC',
        'Jersey': 'EMEA',
        'Jordan': 'EMEA',
        'Kazakhstan': 'EMEA',
        'Kenya': 'EMEA',
        'Korea': 'APAC',
        'Kuwait': 'EMEA',
        'Latvia': 'EMEA',
        'Lebanon': 'EMEA',
        'Liechtenstein': 'EMEA',
        'Lithuania': 'EMEA',
        'Luxembourg': 'EMEA',
        'Macao': 'APAC',
        'Macedonia': 'EMEA',
        'Madagascar': 'EMEA',
        'Malaysia': 'APAC',
        'Malta': 'EMEA',
        'Martinique': 'EMEA',
        'Mauritius': 'EMEA',
        'Mexico': 'AMER',
        'Monaco': 'EMEA',
        'Morocco': 'EMEA',
        'Myanmar': 'APAC',
        'Namibia': 'EMEA',
        'Netherlands': 'EMEA',
        'New Caledonia': 'EMEA',
        'New Zealand': 'APAC',
        'Nigeria': 'EMEA',
        'Norway': 'EMEA',
        'Oman': 'EMEA',
        'Panama': 'AMER',
        'Papua New Guinea': 'APAC',
        'Peru': 'AMER',
        'Philippines': 'APAC',
        'Poland': 'EMEA',
        'Portugal': 'EMEA',
        'Puerto Rico': 'AMER',
        'Qatar': 'EMEA',
        'Romania': 'EMEA',
        'Russian Federation': 'EMEA',
        'RÃ©union': 'EMEA',
        'Saudi Arabia': 'EMEA',
        'Serbia': 'EMEA',
        'Singapore': 'APAC',
        'Slovakia': 'EMEA',
        'Slovenia': 'EMEA',
        'South Africa': 'EMEA',
        'Spain': 'EMEA',
        'Sri Lanka': 'APAC',
        'Sweden': 'EMEA',
        'Switzerland': 'EMEA',
        'Taiwan': 'APAC',
        'Thailand': 'APAC',
        'Trinidad and tobago': 'AMER',
        'Turkey': 'EMEA',
        'Ukraine': 'EMEA',
        'United Arab Emirates': 'EMEA',
        'United Kingdom': 'EMEA',
        'United States': 'AMER',
        'Uruguay': 'AMER',
        'VietNam': 'APAC'
    }

