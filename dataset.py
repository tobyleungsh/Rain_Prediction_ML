from functools import reduce
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt



data_list = ['temp', 'wind', 'humidity','rain']

def cleaning(li):
    df_list = []
    for st in li:
        df = pd.read_csv(f"/workspaces/weather/data/hk_{st}.csv", index_col = False)
        df1 = df.drop(df[df['complete'] != "C"].index)
        df1['date'] = df1['year'] + '-' + df1['month'].astype('Int64').astype(str) + '-' + df1['day'].astype('Int64').astype(str)
        df1['date'] = pd.to_datetime(df1['date'])
        df2 = df1.drop(["year", 'month', 'day', 'complete'], axis = 1)
        df_list.append(df2)
    df_merged = reduce(lambda left,right: pd.merge(left,right,on=['date'], how='inner'), df_list)
    df_merged = df_merged[['date', 'temp', 'humidity', 'rainfall', 'wind_speed']]
    return df_merged

df = cleaning(data_list)
df.info()