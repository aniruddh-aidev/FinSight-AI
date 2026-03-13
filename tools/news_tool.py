from newsapi import NewsApiClient
from dotenv import load_dotenv
from crewai.tools import tool
import os

load_dotenv()

@tool("Get News")
def get_news(query: str):
     """Fetches the latest 5 news articles for a given stock or sector query."""
     api=NewsApiClient(api_key=os.getenv("NEWS_API_KEY"))

     response=api.get_everything(
        q=query,
        language="en",
        sort_by="publishedAt",
        page_size=5
    )

     articles=[]
     for a in response["articles"]:
        articles.append({
            "title":a["title"],
            "description":a["description"],
            "url":a["url"]
        })

     return articles

