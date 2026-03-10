import os
from langchain_core.tools import tool
from langchain_core.tools import tool, InjectedToolCallId
from langchain_core.messages import ToolMessage
from langgraph.types import Command
from langgraph.types import Command
from typing import Annotated

# --- HANDOFF TOOLS ---

@tool
def handoff_to_writer(
    research_summary: str, 
    tool_call_id: Annotated[str, InjectedToolCallId] # Injects the ID needed for the response
):
    """Call this when research is finished to start the writing phase."""
    return Command(
        update={
            "messages": [
                ToolMessage(
                    content="Transferring control to writer.", 
                    tool_call_id=tool_call_id
                )
            ]
        },
        goto="writer"
    )

@tool
def handoff_to_researcher(
    missing_info: str,
    tool_call_id: Annotated[str, InjectedToolCallId]
):
    """Call this if you need the researcher to find more specific details."""
    return Command(
        update={
            "messages": [
                ToolMessage(
                    content="Transferring control to researcher.", 
                    tool_call_id=tool_call_id
                )
            ]
        },
        goto="researcher"
    )