from tools.stock_tool import get_stock_data
from crewai import Agent
from llm import llm

stock_analyst=Agent(
    role="Stock Data Analyst",
    goal="Analyze trend, price, volume, movement",
    backstory="You have worked for a a Stock Exchange firm. You have more than 10 years of experience.You know how to read stock movement, profit, loss, ternds",
    tools=[get_stock_data],
    llm=llm,
    verbose=True
)