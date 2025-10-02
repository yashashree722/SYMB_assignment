from fastapi import FastAPI
from fastapi.responses import StreamingResponse
import sqlite3
import pandas as pd
from io import BytesIO
from datetime import datetime, timedelta


def get_last_48_hours_data():
    conn = sqlite3.connect("weather.db")
    cursor = conn.cursor()

    now = datetime.now()
    start_time = now - timedelta(hours=48)

    query = """
        SELECT * FROM weather
        WHERE timestamp >=datetime('now', '-48 hours')
        ORDER BY timestamp ASC
    """
    cursor.execute(query)
    rows = cursor.fetchall()
    conn.close()

    df = pd.DataFrame(rows, columns=["timestamp", "temperature_2m", "relative_humidity_2m"])

    return df