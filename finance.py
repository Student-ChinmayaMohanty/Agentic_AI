from agno.agent import Agent
from agno.models.groq import Groq
from dotenv import load_dotenv
from agno.tools.duckduckgo import DuckDuckGoTools
from agno.tools.yfinance import YFinanceTools
def build_agent ():
    return Agent (
        model=Groq(id="llama-3.3-70b-versatile"),
        tools=[DuckDuckGoTools(),YFinanceTools()],
        markdown=True,
        description="You are a comprehensive investment analyst with access to all financial data functions.",
    instructions=[
        "Use any financial function as needed for investment analysis",
        "Format your response using markdown and use tables to display data",
        "Provide detailed analysis and insights based on the data",
        "Include relevant financial metrics and recommendations",
    ],
        add_datetime_to_context=True,
        debug_mode=True
    )
    
    
    
Groqai_agent = build_agent ()

Groqai_agent.print_response("Share the MSFT stock prise in INR and analyst recomendation ?")