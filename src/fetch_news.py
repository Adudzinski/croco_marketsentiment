import requests
from datetime import datetime, timedelta
from dotenv import load_dotenv
import os
from pathlib import Path

env_path =  Path(__file__).resolve().parent.parent / '.env'
load_dotenv(dotenv_path=env_path)

news_api_key = os.getenv("NEWSAPI_KEY")

def fetch_headlines(config):
    keywords = config["company"]["keywords"]
    query = " OR ".join(keywords)
    
    params = {
        "q": query,
        "language": config["newsapi"].get("language", "en"),
        "pageSize": config["newsapi"].get("max_results", 25),
        "sortBy": config["newsapi"].get("sort_by", "publishedAt"),
        "from": (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d'),
        "apiKey": news_api_key
    }
    
    response = requests.get("https://newsapi.org/v2/everything", params=params)
    articles = response.json().get("articles", [])
    
    return [{"headline": a["title"], "source": a["source"]["name"], "date": a["publishedAt"]} for a in articles]

