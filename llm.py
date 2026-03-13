from dotenv import load_dotenv
from crewai import LLM
import os

load_dotenv()

llm = LLM(
    model="groq/llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY"),
    max_tokens=1200,
    temperature=0.3,
    max_retries=5
)
