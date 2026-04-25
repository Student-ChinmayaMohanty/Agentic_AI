from agno.agent import Agent
from agno.models.groq import Groq
from dotenv import load_dotenv
from agno.tools.duckduckgo import DuckDuckGoTools

def build_agent ():
    return Agent (
        model=Groq(id="llama-3.3-70b-versatile"),
        tools=[DuckDuckGoTools()],
        markdown=True,
        instructions="You are helpful and expert travel agent.",
        add_datetime_to_context=True
    )
    
    
    
Groqai_agent = build_agent ()

Groqai_agent.print_response("is it safe to travel Uae?")