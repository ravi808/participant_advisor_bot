from langchain.agents import initialize_agent, Tool
from langchain.llms import OpenAI
from langchain.tools import tool

@tool
def get_stock_price(symbol: str) -> str:
    return "120"

@tool
def simulate_tax_scenario(grant_units: int, sale_price: float) -> str:
    return f"Estimated tax: ${(grant_units * sale_price) * 0.3:.2f}"

tools = [get_stock_price, simulate_tax_scenario]
llm = OpenAI(temperature=0)
agent = initialize_agent(tools, llm, agent_type="zero-shot-react-description", verbose=True)

def run_agentic_query(query: str) -> str:
    return agent.run(query)