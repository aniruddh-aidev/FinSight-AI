from tools.news_tool import get_news
from crewai import Agent
from llm import llm


news_fetcher=Agent(
    role="News Collection Specialist",
    goal="Find the 5 latest news regarding the given sector or company",
    backstory="You spent 10 years as a researcher at a major financial news agency, monitoring markets across global markets. Your expertise lies in quickly finding the most important and influential news articles for any given company or sector.",
    tools=[get_news],
    llm=llm,
    verbose=True
)