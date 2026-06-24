import pandas as pd
import random
from datetime import datetime, timedelta
from faker import Faker



def create_restautant():
    restaurants=[
        {"ID":'R1',"Name":"Funky Food Mitte","Adress":"21 Mitte street","Phone":"0769 89 76 56","lat":52.5200,"long":13.4050},
        {"ID":'R2',"Name":"Funky Food spandau","Adress":"12 spandau street","Phone":"0769 89 76 58","lat":52.5353,"long":13.2013}
    ]
    df =  pd.DataFrame(restaurants)
    return df   

create_restautant()

def save_csv(df,name):
    df.to_csv(f'data/raw/{name}', index=False, sep=",")


df =create_restautant()
save_csv(df,"Restautrants.csv")