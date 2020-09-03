import pandas as pd
import numpy as np
import os
import re
from datetime import timedelta

files = [f for f in os.listdir('.') if f.endswith('.csv') and not f.startswith('.')]
# get data
def get_data(file):
    '''
    Reads in data from file, appends name of file in separate column
    '''
    data = pd.read_csv(file, sep = ';')
    name = re.findall('(^\w+)', str(file))
    data['origin'] = str(name[0])
    data['customer_no_new'] = str(name[0]) + '_' + data['customer_no'].astype(str)
    data['timestamp'] = pd.to_datetime(data['timestamp'])
    return data

dat_pre = [get_data(file) for file in files]
data = pd.concat(dat_pre, ignore_index = True)
data = data.drop(['customer_no'], axis = 1)

data = data.rename(columns = {'customer_no_new' : 'customer_no'})

# add missing checkout info

data['last_loc'] = data.groupby('customer_no')['location'].transform('last')

# find people whose final loc was not checkout

did_not_checkout = data[data['last_loc'] != 'checkout']

# find only last timestamp for these people

# get dataframe sorted by timestamp for each customer
did_not_checkout = did_not_checkout.groupby(['customer_no']).apply(lambda x: x.sort_values(['timestamp'], ascending = False)).reset_index(drop=True)
# select top row within each continent
new_checkouts = did_not_checkout.groupby('customer_no').head(1)

new_checkouts['timestamp'] = new_checkouts['timestamp'] + timedelta(minutes = 1)

new_checkouts['location'] = 'checkout'

data = pd.concat([data, new_checkouts])

data['last_loc'] = data.groupby('customer_no')['location'].transform('last')

data.index = pd.DatetimeIndex(data['timestamp'])

data = data.drop('last_loc', axis = 1)



# forward-fill


filled = data.groupby('customer_no').resample('T').ffill()
filled = filled.drop(['timestamp', 'customer_no'], axis = 1)

filled = filled.reset_index()


# shift

filled['previous'] = filled.groupby('customer_no')['location'].shift(1)
filled['previous'] = filled['previous'].replace(np.nan, 'entrance', regex=True)

# write to file

filled.to_csv('supermarket_all.csv')
