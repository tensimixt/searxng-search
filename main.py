from fastapi import FastAPI, Query
import requests
from typing import Optional

app = FastAPI()

def search_searxng(query="elon musk", categories="news", time_range="day"):
    base_url = "https://searxng-railway-production-65a7.up.railway.app/search"
    params = {
        'q': query,
        'format': 'json',
        'categories': categories,
        'time_range': time_range
    }
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": str(e)}

@app.get("/search")
def search(
    q: str = Query("elon musk", description="Search query"),
    categories: str = Query("news", description="Categories"),
    time_range: str = Query("day", description="Time Range")
):
    results = search_searxng(q, categories, time_range)
    return results
