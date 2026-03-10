import os
from typing import Literal
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from langchain_core.tools import tool
from langgraph.graph import StateGraph, MessagesState, START

from tools.search import search_web
from tools.savefile import save_to_file
from tools.handoff import handoff_to_writer

# --- Load environment variables and initialize the language model ---
load_dotenv()
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

# --- AGENT NODES ---

researcher_node = create_agent(
    llm, 
    tools=[search_web, handoff_to_writer],
    system_prompt="You are a Researcher. Gather facts using the 'search_web' tool. Once done, you MUST call 'handoff_to_writer' to pass your findings to the next stage."
)

writer_node = create_agent(
    llm, 
    tools=[save_to_file],
    system_prompt="You are a Writer. Write the post AND THEN use the save_to_file tool to save it."
)

# --- THE GRAPH ---

builder = StateGraph(MessagesState)

# 1. Add nodes
builder.add_node("researcher", researcher_node)
builder.add_node("writer", writer_node)

# 2. Define the flow
builder.add_edge(START, "researcher")

# 3. Add an edge from researcher to writer 
builder.add_edge("researcher", "writer")  # so the Command(goto="writer") has a valid path to follow. 

# 4. Compile the graph
graph = builder.compile()

# --- USER INPUT & EXECUTION ---

if __name__ == "__main__":
    
    # 1. Ask user for the topic and target filename
    user_topic = input("Enter the research topic: ")
    user_filename = input("Enter the output filename (e.g., my_blog.txt): ")

    # 2. Pass these into the initial graph state
    initial_input = {
        "messages": [
            ("user", f"Topic: {user_topic}. Research this and save the final post to '{user_filename}'.")
        ]
    }

    # 3. Run the graph with streaming to see the handoff in action
    print(f"\n--- Starting Workflow for: {user_topic} ---\n")
    for chunk in graph.stream(initial_input):
        
        # Print node updates to see the handoff happen
        for node_name, state_update in chunk.items():
            print(f"[Node: {node_name}] is processing...")
    
    # 4. Final message after completion
    print(f"\n--- Workflow Complete. Check '{user_filename}' for the result. ---")