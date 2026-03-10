import os
from dotenv import load_dotenv
from langchain_core.tools import tool
import serpapi

# --- 1. DEFINE THE FLIGHT SEARCH TOOL ---
@tool
def search_flights(departure_id: str, arrival_id: str, outbound_date: str, return_date: str = None):
    """
    Searches for flights using SerpApi's Google Flights engine.
    departure_id/arrival_id: 3-letter airport codes (e.g., 'JFK', 'LAX').
    outbound_date/return_date: Format 'YYYY-MM-DD'.
    """

    client = serpapi.Client(api_key=os.getenv("SERPAPI_API_KEY"))

    result = client.search(
        engine="google_flights",
        departure_id=departure_id,
        arrival_id=arrival_id,
        outbound_date=outbound_date,
        return_date=return_date,
        currency="USD"
        )
    
    return str(result.get("best_flights", "No flights found."))
