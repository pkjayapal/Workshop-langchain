import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

##
## No Agent Example ##
##
## This is a simple example of using an LLM without any tools or agents.
## Run this to test your API key and make sure everything is working before moving on to the
## This just takes the question (user input) and sends it directly to the LLM, then prints the response.
##

# Load the API key from your .env file
load_dotenv()

# 1. Initialize the LLM (using a cost-efficient model)
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)

# 2. Ask a simple question
question = "Say 'Hello World' and tell me one cool thing LangChain can do."

# 3. Invoke the model
response = llm.invoke(question)

# 4. Print the response content
print(response.content)