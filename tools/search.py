import os
from langchain_core.tools import tool
from tavily import TavilyClient

@tool
def search_web(query: str) -> str:
    """
    Searches the web for real-time information. 
    Use this for news, sports scores, current events or research
    """
    client = TavilyClient(api_key=os.environ["TAVILY_API_KEY"])

    # Get search results and return them as a string for the AI
    response = client.search(query=query, max_results=2)
    return str(response['results'])