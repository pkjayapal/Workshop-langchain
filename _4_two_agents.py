import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from langchain_core.tools import tool
from tavily import TavilyClient # Use the direct client

##
## Two Agents Example ##
##
## This example demonstrates a multi-agent workflow 
## Agent 1 (Researcher) uses a web search tool to gather information on a topic
## Agent 2 (Writer) uses a file-saving tool to write and save a blog post 
##

# Load your API keys from .env
load_dotenv()

# --- STEP 1: DEFINE TOOLS ---
from tools.search import search_web
from tools.savefile import save_to_file


llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

# --- STEP 2: CREATE THE TWO AGENTS ---

# Agent 1: The Researcher (has web search tool)
researcher = create_agent(
    model=llm, 
    tools=[search_web],
    system_prompt="You are a helpful researcher that can search the web for information."
)

# Agent 2: The Writer (has file saving tools)
writer = create_agent(
    model=llm, 
    tools=[save_to_file],
    system_prompt="You are a helpful assistant that can save information to files when asked."
)

# --- STEP 3: MULTI-AGENT WORKFLOW ---

def run_multi_agent_workflow(topic):

    print(f"\n--- PHASE 1: {topic} Research ---")
    
    # New syntax uses 'messages' and returns a message history
    res_response = researcher.invoke({
        "messages": [("user", f"Find 3 key facts about {topic}.")]
    })
    
    # Extract the last message content
    
    raw_data = res_response["messages"][-1].content
    print(f"Researcher found: {raw_data[:100]}...")

    print(f"\n--- PHASE 2: Writing & Saving ---")
    writer.invoke({
        "messages": [("user", f"Based on this research: '{raw_data}', write a short blog post and save it to 'blog.txt'.")]
    })
    print("Done! Check blog.txt")

if __name__ == "__main__":
    run_multi_agent_workflow("The future of AI agents in 2026")