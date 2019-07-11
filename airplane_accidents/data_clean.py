import pandas as pd
import numpy as np
from datetime import datetime

raw_data = pd.read_csv('data/raw.csv', sep = '|')

# clean column time
data_c = raw_data.copy()
data_c['time'] = data_c.time.str.replace('c', '')\
    .str.replace(':','')\
    .str.replace(';','')\
    .str.replace('Z','')\
    .str.replace('"','')\
    .str.replace('.','')\
    .str.replace('?', '0000')
data_c['time'] = data_c.time.str.strip()
data_c['time'] = np.where(data_c['time'].str.len() < 4, '0'+data_c['time'], data_c['time'])
data_c['time'] = np.where(data_c['time'].str.len() > 4, data_c['time'].str[:-1], data_c['time'])

# replace ? with NANs
data_nan = data_c.copy()
cols = ['cn_ln',
        'crew_aboard',
        'crew_fatalities',
        'date',
        'flight_no',
        'ground',
        'location',
        'operator',
        'passengers_aboard',
        'passengers_fatalities',
        'registration',
        'route',
        'summary',
        'total_aboard']

for col in cols:
    data_nan[col] = np.where(data_nan[col] == '?', np.nan, data_nan[col])

# remove leading and trailing white spaces
for col in ['ac_type', 'location', 'operator', 'route', 'summary']:
    data_nan[col] = data_nan[col].str.strip()

# format date-time
data_dt = data_nan.copy()
data_dt['dt'] = data_dt['date'] + ' ' + data_dt['time']
data_dt['dt'] = pd.to_datetime(data_dt['dt'], format='%B %d, %Y %H%M')

raw_data = pd.read_csv('data/API_IS.AIR.DPRT_DS2_en_csv_v2_6211.csv')
