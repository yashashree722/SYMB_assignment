import requests
import pandas as pd
from datetime import datetime, timedelta

def fetch_data(lat: float, lon: float):
    end_date = datetime.now().date() - timedelta(days=1)    
    start_date = end_date - timedelta(days=2)  
    url = "https://api.open-meteo.com/v1/forecast"   
    params = {
       "latitude": lat,
        "longitude": lon,
        "hourly": "temperature_2m,relative_humidity_2m",
        "start_date": start_date.strftime("%Y-%m-%d"),
        "end_date": end_date.strftime("%Y-%m-%d"),
        "timezone": "auto"
    }
    print(f"start date is {start_date} and end date is {end_date}")
    response = requests.get(url, params=params)
    if response.status_code != 200:
        raise Exception(f"API request failed {response.status_code}")
    data = response.json()
    df = pd.DataFrame({
        "timestamp": data["hourly"]["time"],
        "temperature_2m": data["hourly"]["temperature_2m"],
        "relative_humidity_2m": data["hourly"]["relative_humidity_2m"]
    })
    
    return df


if __name__ == "__main__":
    df = fetch_data(47.37, 8.55)
    print(df)
