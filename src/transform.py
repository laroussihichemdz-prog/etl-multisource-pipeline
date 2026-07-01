import pandas as pd

def clean_orders(df_orders, df_lines):
    # Remove duplicate rows
    df_orders = df_orders.drop_duplicates()
    df_lines = df_lines.drop_duplicates()
    
    # Calculate total amount per order line
    df_lines['line_total'] = df_lines['unit_price'] * df_lines['quantity']
    
    # Group by order to get gross total per order
    gross_totals = df_lines.groupby('IDOrder')['line_total'].sum()
    
    gross_totals = gross_totals.reset_index()
    gross_totals.columns = ['IDOrder', 'gross_total']
    
    # Merge orders with gross totals
    df_complete = df_orders.merge(gross_totals, on='IDOrder', how='left')
    
    # Fix aberrant discounts (999 → 9.99, decimal point encoding bug)
    df_complete.loc[df_complete['remise'] == 999, 'remise'] = 999 / 100
    print(f"Aberrant discounts fixed: {(df_complete['remise'] == 9.99).sum()} rows")
    
    # Calculate net total after discount
    df_complete['net_total'] = df_complete['gross_total'] * (1 - df_complete['remise'] / 100)
    
    return df_complete

df_orders = pd.read_csv('data/raw/orders.csv')
df_lines = pd.read_csv('data/raw/OrdersLines.csv')
result = clean_orders(df_orders, df_lines)
print(result.head())
print(result.columns.tolist())
