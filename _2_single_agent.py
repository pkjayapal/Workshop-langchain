import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langchain.agents import create_agent

##
## Single Agent Example ##
## 
## This is a simple example of an autonomous agent 
## that can search for flights using the SerpApi Google Flights engine.
## The agent will take a user query, determine if it needs to search for flights,
## and then use the search_flights tool to get real-time flight information.
##

# --- 1. DEFINE THE FLIGHT SEARCH TOOL ---
from tools.searchflights import search_flights

load_dotenv()

# --- 2. AGENT SETUP ---
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
tools = [search_flights]

# Create the autonomous agent
agent = create_agent(
            llm, 
            tools, 
            system_prompt="You are a helpful travel assistant that can search for flights using the 'search_flights' tool. Always use this tool when asked about flight information.")

# --- 3. RUN THE SEARCH ---
if __name__ == "__main__":
    # Example input: "Find the cheapest flight from NYC to London on May 10th 2024"
    query = input("Enter your travel request: ")
    
    inputs = {"messages": [("user", query)]}
    
    print("\n--- Agent is searching for flights... ---\n")
    result = agent.invoke(inputs)
    
    # Print the agent's final summary of the flights found
    print(result["messages"][-1].content)