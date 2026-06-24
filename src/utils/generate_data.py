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
def create_families():
    family=[
        {'IDfamily':'F1','name':'Cold Starters / Salads'},
        {'IDfamily':'F2','name':'Burgers'},
        {'IDfamily':'F3','name':'Pizza'},
        {'IDfamily':'F4','name':'Sandwiches'},
        {'IDfamily':'F5','name':'Crispy'},
        {'IDfamily':'F6','name':'Desserts'},
        {'IDfamily':'F7','name':'Drinks'}
    ]
    df=pd.DataFrame(family)
    return df
def create_articles():
    article=[
        {'IDarticle':'00001','IDfamily':'F2','Name':'Classic Burger','Price':5.99,'cost':2.10},
        # Burgers
        {'IDarticle':'00002','IDfamily':'F2','Name':'Chicken Burger','Price':6.49,'cost':2.30},
        {'IDarticle':'00003','IDfamily':'F2','Name':'Meat Burger','Price':7.49,'cost':2.80},
{'IDarticle':'00004','IDfamily':'F2','Name':'Fish Burger','Price':6.99,'cost':2.50},
{'IDarticle':'00005','IDfamily':'F2','Name':'Veggie Burger','Price':5.49,'cost':1.80},
{'IDarticle':'00006','IDfamily':'F2','Name':'Double Burger','Price':8.99,'cost':3.40},

# Cold Starters / Salads
{'IDarticle':'00007','IDfamily':'F1','Name':'Caesar Salad','Price':4.99,'cost':1.60},
{'IDarticle':'00008','IDfamily':'F1','Name':'Mixed Salad','Price':4.49,'cost':1.40},
{'IDarticle':'00009','IDfamily':'F1','Name':'Green Salad','Price':3.99,'cost':1.20},
{'IDarticle':'00010','IDfamily':'F1','Name':'Carrot Salad','Price':3.49,'cost':1.00},

# Sandwiches
{'IDarticle':'00011','IDfamily':'F4','Name':'Classic Sandwich','Price':4.99,'cost':1.70},
{'IDarticle':'00012','IDfamily':'F4','Name':'Tuna Sandwich','Price':5.49,'cost':1.90},
{'IDarticle':'00013','IDfamily':'F4','Name':'Chicken Sandwich','Price':5.99,'cost':2.10},
{'IDarticle':'00014','IDfamily':'F4','Name':'Meat Sandwich','Price':6.49,'cost':2.30},
{'IDarticle':'00015','IDfamily':'F4','Name':'Three Cheese Sandwich','Price':5.99,'cost':2.00},

# Pizza
{'IDarticle':'00016','IDfamily':'F3','Name':'Margherita','Price':8.99,'cost':5.0},
{'IDarticle':'00017','IDfamily':'F3','Name':'Pepperoni','Price':9.99,'cost':3.20},
{'IDarticle':'00018','IDfamily':'F3','Name':'BBQ Chicken','Price':10.49,'cost':3.50},
{'IDarticle':'00019','IDfamily':'F3','Name':'Four Cheese','Price':10.99,'cost':3.80},
{'IDarticle':'00020','IDfamily':'F3','Name':'Veggie Pizza','Price':8.49,'cost':2.60},

# Crispy
{'IDarticle':'00021','IDfamily':'F5','Name':'Crispy Chicken','Price':6.99,'cost':2.40},
{'IDarticle':'00022','IDfamily':'F5','Name':'Crispy Strips x4','Price':5.49,'cost':1.80},
{'IDarticle':'00023','IDfamily':'F5','Name':'Crispy Strips x8','Price':9.49,'cost':3.20},
{'IDarticle':'00024','IDfamily':'F5','Name':'Crispy Wrap','Price':6.49,'cost':2.20},
{'IDarticle':'00025','IDfamily':'F5','Name':'Crispy Burger','Price':7.49,'cost':2.60},

# Desserts
{'IDarticle':'00026','IDfamily':'F6','Name':'Chocolate Brownie','Price':3.49,'cost':0.90},
{'IDarticle':'00027','IDfamily':'F6','Name':'Cheesecake','Price':3.99,'cost':1.10},
{'IDarticle':'00028','IDfamily':'F6','Name':'Ice Cream','Price':2.99,'cost':0.70},
{'IDarticle':'00029','IDfamily':'F6','Name':'Apple Pie','Price':3.49,'cost':0.90},
{'IDarticle':'00030','IDfamily':'F6','Name':'Cookie','Price':1.99,'cost':0.50},

# Drinks
{'IDarticle':'00031','IDfamily':'F7','Name':'Coca-Cola','Price':2.49,'cost':0.50},
{'IDarticle':'00032','IDfamily':'F7','Name':'Sprite','Price':2.49,'cost':0.50},
{'IDarticle':'00033','IDfamily':'F7','Name':'Orange Juice','Price':2.99,'cost':0.70},
{'IDarticle':'00034','IDfamily':'F7','Name':'Water','Price':1.49,'cost':0.20},
{'IDarticle':'00035','IDfamily':'F7','Name':'Milkshake','Price':3.99,'cost':1.00},
{'IDarticle':'00036','IDfamily':'F7','Name':'Iced Tea','Price':2.49,'cost':0.50},
    ]
    df = pd.DataFrame(article)
    return df

def save_csv(df,name):
    df.to_csv(f'data/raw/{name}', index=False, sep=",")
    

df =create_restautant()
save_csv(df,"Restautrants.csv")

df = create_families()
save_csv(df,"Families.csv")

df =  create_articles()
save_csv(df,"Articles.csv")
