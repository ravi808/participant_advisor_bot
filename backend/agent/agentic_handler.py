from langchain.agents import initialize_agent, Tool
from langchain.llms import OpenAI
from langchain.tools import tool
import json

@tool
def get_stock_price(symbol: str) -> str:
    """Fetch the current stock price for a given stock symbol."""
    return "120"  # Dummy value

@tool
def simulate_tax_scenario(input_str: str) -> str:
    """Calculate estimated tax based on grant_units and sale_price provided as a JSON string."""
    try:
        data = json.loads(input_str)
        grant_units = data["grant_units"]
        sale_price = data["sale_price"]
        estimated_tax = (grant_units * sale_price) * 0.3
        return f"Estimated tax: ${estimated_tax:.2f}"
    except Exception as e:
        return f"Error parsing input: {str(e)}"

tools = [get_stock_price, simulate_tax_scenario]
llm = OpenAI(temperature=0)
agent = initialize_agent(tools, llm, agent_type="zero-shot-react-description", verbose=True)

def run_agentic_query(query: str) -> str:
    return agent.run(query)
