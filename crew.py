from crewai import Crew, Task, Process
from agents.sector_mapper import sector_mapper
from agents.news_fetcher import news_fetcher
from agents.sentiment_analyst import sentiment_analyst
from agents.stock_analyst import stock_analyst
from agents.synthesizer import synthesizer
from agents.report_writer import report_writer

# Task 1
sector_mapping_task = Task(
    description="Given the sector '{sector}', identify the top 4-5 most representative stock tickers in that sector.",      # tell it what to do with the user's input
    expected_output="A list of 4-5 stock ticker symbols e.g. ['AAPL', 'MSFT', 'GOOGL']",  # e.g. "A list of 4-5 stock tickers"
    agent=sector_mapper
)

# Task 2
news_fetching_task = Task(
    description="Fetch the 5 latest news articles for each of the stock tickers identified in the previous task.",      # fetch news for the tickers found above
    expected_output="5 latest news about the stock or sector",  # e.g. "5 news articles per ticker"
    agent=news_fetcher
)

sentiment_analyzing_task = Task(
    description="Analyze the sentiment of the news articles fetched in the previous task for each stock ticker. Score each as positive, negative or neutral.",
    expected_output="present sentiments regarding the stock or sector (eg.positive or negative)",  # e.g. "5 news articles per ticker"
    agent=sentiment_analyst
)

stock_analyzing_task = Task(
    description="Fetch and analyze the stock price data for each of the tickers identified in task 1. Look at price trends, current price and volume.",
    expected_output="report of stock's trend and performance",  # e.g. "5 news articles per ticker"
    agent=stock_analyst
)

synthesizing_task = Task(
    description="Combine the sentiment analysis and stock price data from the previous tasks. Identify which stocks look strongest and weakest and explain why.",      # fetch news for the tickers found above
    expected_output="A summary of the containing the overall performance of stock and public perception",  # e.g. "5 news articles per ticker"
    agent=synthesizer
)

report_writing_task = Task(
    description="Take the synthesis from the previous task and write it into a clean, user friendly investment report.",
    expected_output="A clean, structured investment brief with sections for each stock covering price trend, sentiment, and a buy/hold/sell recommendation for each stock.",
    agent=report_writer
)

def run_crew(sector):
    crew=Crew(
        agents=[sector_mapper, news_fetcher, sentiment_analyst, stock_analyst, synthesizer, report_writer],
        tasks=[sector_mapping_task, news_fetching_task, sentiment_analyzing_task, stock_analyzing_task, synthesizing_task, report_writing_task],
        process=Process.sequential,
        verbose=True,
        max_rpm=5
    )
    return crew.kickoff(inputs={"sector": sector})