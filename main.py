from fastapi import FastAPI,Query
import requests
import pandas as pd 
import sqlite3
from datetime import datetime, timedelta
from fetch_past_2_days_data import fetch_data
from io import BytesIO
from fastapi.responses import StreamingResponse
from fetch_data_from_db import get_last_48_hours_data

def save_to_sqlite(df: pd.DataFrame):
    conn = sqlite3.connect("weather.db")
    df.to_sql("weather", conn, if_exists="append", index=False)
    conn.close()


app = FastAPI()
@app.get('/weather-report')
def weather_data(lat:float=Query(...,), lon:float=Query(...)):
    try:
        df = fetch_data(lat, lon)
        print("data fetch successfully")
        save_to_sqlite(df)

        return {
            "message": "Saved to db ",
            "data" : df.to_dict(orient="records"),
            "records_inserted": len(df)
        }
    except Exception as e :
        return {"error":str(e)}



@app.get("/export/excel")
def export_excel():
    df = get_last_48_hours_data()

    output = BytesIO()
    df.to_excel("weather_last_48_hours.xlsx", index=False)  

    output.seek(0)

    filename = f"weather_last_48_hours.xlsx"
    return {
        "message" : "file genrated for last 48 hrs data",
        "file_name" : "weather_last_48_hours.xlsx"
    } 


