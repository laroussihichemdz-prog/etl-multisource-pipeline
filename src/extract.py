import pandas as pd
import requests
import json
from geopy.geocoders import Nominatim
from geopy.distance import geodesic

def extract_csv(path):
    df = pd.read_csv(path, sep=',')
    return df

def extract_api(lat, lon, rayon=500):
    import urllib.parse
    
    query = f"[out:json];node(around:{rayon},{lat},{lon});out;"
    url = "https://overpass-api.de/api/interpreter?data=" + urllib.parse.quote(query)
    
    headers = {
        'User-Agent': 'etl-pipeline/1.0'
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        print("Erreur:", response.text[:500])
        return None
    
    return response.json()
def extract_api_to_df(result):
    if result is None:
        print("Pas de résultat à convertir")
        return pd.DataFrame()
    
    data = []
    for element in result['elements']:
        if 'tags' in element:
            data.append({
                'id': element.get('id'),
                'lat': element.get('lat'),
                'lon': element.get('lon'),
                'name': element['tags'].get('name', 'N/A'),
                'amenity': element['tags'].get('amenity', 'N/A')
            })
    return pd.DataFrame(data)


