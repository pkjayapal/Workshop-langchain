# Workshop-langchain
Learn Agentic AI by building hands-on agents using python and langchain 

# Workshop targeted for Multi-agent orchestration and understanding
No agent, single agent, single agent with tools, multi agent in langchain and langgraph 

# Tech Stack
Framework: LangChain & LangGraph
LLM: OpenAI (GPT-4o-mini)
APIs: SerpApi (Google Flights)
APIs: Tavily
Tool: Save File

#📋 Prerequisites
Python 3.9+
API Keys:
OpenAI API Key
SerpApi Key
Tavily Key

##⚙️ Installation
Clone the repository:
```
bash
git clone <your-repo-url>
cd Langchain-hello
```

## Set up a Virtual Environment:
```
bash
python -m venv .venv
### Windows:
.venv\Scripts\activate
### Mac/Linux:
source .venv/bin/activate
```
Use code with caution.

## Install Dependencies:
```
bash
pip install langchain-openai langgraph serpapi python-dotenv
```
Use code with caution.

## Environment Variables:
Create a .env file in the root directory:
```
env
OPENAI_API_KEY=your_openai_key_here
SERPAPI_API_KEY=your_serpapi_key_here
TAVILY_API_KEY=your_tavily_key_here
```
Use code with caution.

##📂 Project Structure
```
.
├── output/              # Generated flight reports
├── tools/
│   ├── __init__.py
│   ├── search_tool.py   # SerpApi flight search logic
│   ├── save_file.py     # SerpApi flight search logic
│   └── file_tool.py     # Local file saving logic
├── no_agent.py                # Single agent orchestration
├── single_agent.py            # Single agent orchestration
├── single_agent_two_tools.py  # Single agent orchestration
├── two_agents.py              # Single agent orchestration
├── two_agents_graph.py        # Single agent orchestration
└── .env                 # API keys (git-ignored)
```
Use code with caution.

## 🏃 Usage
Run the main script and enter your request when prompted:
```
bash
python no_agent.py
```
Use code with caution.

