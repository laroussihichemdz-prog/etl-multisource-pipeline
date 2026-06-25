import pandas as pd
import requests
import json

def extract_csv(path):
   df = pd.read_csv(path,sep=',')
   return df

df=extract_csv('data/raw/orders.csv')
print(df.head())



