import os
import langchainhub as hub
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from langchain_core.tools import tool

##
## Single Agents Example ##
##
## This example demonstrates single agent with 2 tools:
## Tool1: search_web - to gather information on a topic
## Tool2: save_to_file - to save the information to a file
## The agent will take a user query, search web if needed and then save the results to a file.
## 

# Load your API keys from .env
load_dotenv()

# --- STEP 1: DEFINE TOOLS ---
from tools.search import search_web
from tools.savefile import save_to_file

tools = [save_to_file, search_web] # Include the web search tool in the agent's toolset

# --- STEP 2: SETUP AGENT COMPONENTS ---

# Use GPT-4o-mini (highly efficient for tool calling)
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

# 2. Setup the Agent using the new create_agent function
# This replaces create_tool_calling_agent and AgentExecutor
agent = create_agent(
    model=llm, #"gpt-4o-mini", # You can pass the model name directly or a ChatOpenAI instance
    tools=tools,
    system_prompt="You are a helpful research assistant. Use your tools to find info and save it."
)

# --- STEP 3 RUN THE AGENT ---

query = "Find out who won the 2022 Super Bowl, then save a 1-sentence summary to a file named 'winner.txt'"
result = agent.invoke({"messages": [("user", query)]})

# Print the final response
print(result["messages"][-1].content)