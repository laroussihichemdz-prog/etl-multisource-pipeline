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
{'IDarticle':'00016','IDfamily':'F3','Name':'Margherita','Price':8.99,'cost':2.80},
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
def create_orders():
    orders = []
    start_date=datetime(2024,1,1)
    IdC=1
    for id_restaurant,nb_orders in [('R1',80),('R2',50)]:
        for  day in range(90):
            date = start_date + timedelta(days=day)
            day = date.weekday()
            if day == 4 :
                adjusted_orders = int(nb_orders* 1.3)
            elif day == 5 :
                adjusted_orders = int(nb_orders * 2.1)   
            elif day in [0,1,2,3,6]:
                adjusted_orders = int(nb_orders*0.7)
            else: 
                adjusted_orders=nb_orders
                    

            for i in range(adjusted_orders):
                
                heure = random.randint(10, 23)
                minute = random.randint(0, 59)
                heure_str = f"{heure:02d}:{minute:02d}:00"

                orders.append ({
                    'IDOrder': f"C{IdC:04d}",
                    'IDrestaurant': id_restaurant,
                    'IDclient': 1,
                    'date': date ,
                    'heure': heure_str,
                    'modepaiement': random.choice(['Cash','Card']),
                    'remise': float(random.choice([0,0,0,0,10,20,30,40])),
                    'IDcaissier': random.choice([1,2,3]),
                    'etatpaiement':random.choice( [1,0])  
                    })
                IdC += 1 
    df = pd.DataFrame(orders)
    return df
def create_orders_line(df_orders,df_articles):
    lines=[]
    line_counter=1
    for index,row in df_orders.iterrows():
        nb_articles = random.choice([1,1,2,2,2,2,3,3,3,5,8]) 
        for  _ in range(nb_articles):
            article=df_articles.sample(1).iloc[0]
            lines.append ({
            'IDlines' :line_counter,
            'IDOrder': row['IDOrder'] ,  
            'quantity':random.choice([1,1,1,1,2,2,2,2,3,3,4,4]),
            'article_id': article['IDarticle'],
            'unit_price': article['Price'] 
            })
            line_counter +=1
    df = pd.DataFrame(lines)    
    return df  
def inject_errors(df,colonne,valeur,Tfrac):
    indice = df.sample(frac=Tfrac).index 
    df.loc[indice,colonne]=valeur
    return df




def save_csv(df,name):
    df.to_csv(f'data/raw/{name}', index=False, sep=",")
    

dfR =create_restautant()
save_csv(dfR,"Restautrants.csv")

dfF = create_families()
save_csv(dfF,"Families.csv")

dfA =  create_articles()
save_csv(dfA,"Articles.csv")

dfO = create_orders()
dfO=inject_errors(dfO, 'modepaiement', None,0.03)
dfO=inject_errors(dfO, 'remise', 999,0.03)
save_csv(dfO,"orders.csv")

dfOL = create_orders_line(dfO,dfA)
# Sur OrdersLines
dfOL=inject_errors(dfOL, 'unit_price', 0,0.03)
dfOL=inject_errors(dfOL, 'quantity', 0,0.03)
save_csv(dfOL,"OrdersLines.csv")


