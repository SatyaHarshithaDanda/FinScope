import os
from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from phi.playground import Playground, serve_playground_app
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Define the high-performance model for FinScope
# We use 70b-versatile as it is the most reliable for complex financial logic
shared_model = Groq(id="llama-3.3-70b-versatile")

# --- 1. The Web Research Agent ---
web_search_agent = Agent(
    name="FinScope News Scout",
    # This description appears in the Playground UI sidebar
    description="I am your eyes on the market. I track real-time news, sentiment, and global events.",
    model=shared_model,
    tools=[DuckDuckGo()],
    instructions=[
        "Search for the latest news articles for the given stock symbol.",
        "Always provide the URL sources for your findings.",
        "Focus on news from the last 24-48 hours.",
        "CRITICAL: When using DuckDuckGo, numerical parameters like 'max_results' MUST be integers (e.g., 5), not strings (e.g., '5')."
    ],
    show_tool_calls=True,
    markdown=True,
)

# --- 2. The Financial Data Agent ---
finance_agent = Agent(
    name="FinScope Quant Analyst",
    description="I provide deep-dive fundamental analysis, stock prices, and analyst recommendations.",
    model=shared_model,
    tools=[
        YFinanceTools(
            stock_price=True, 
            analyst_recommendations=True, 
            stock_fundamentals=True,
            company_news=False # We let News Scout handle news for better stability
        ),
    ],
    instructions=[
        "Use tables to display all financial data (P/E ratios, Market Cap, etc.).",
        "Explain financial jargon (like RSI or EBITDA) briefly to educate the user.",
        "Compare current stock prices against analyst target prices.",
        "CRITICAL: All numerical tool arguments MUST be passed as integers, not strings."
    ],
    show_tool_calls=True,
    markdown=True,
)

# --- 3. The Multi-Agent Platform ---
# The manager agent coordinates the strategy
finscope_manager = Agent(
    name="FinScope Strategy Manager",
    description="The lead strategist for FinScope. I synthesize news and data into actionable investment strategies.",
    team=[web_search_agent, finance_agent],
    model=shared_model,
    instructions=[
        "Coordinate between the News Scout and the Quant Analyst.",
        "Always include a 'Risk Analysis' section in your final report.",
        "Summarize recommendations from major banks (Buy/Hold/Sell).",
        "If a tool call fails, attempt to explain the data manually or try once more with integer parameters."
    ],
    show_tool_calls=True,
    markdown=True,
)

# Create the Playground app
app = Playground(agents=[finscope_manager, finance_agent, web_search_agent]).get_app()

if __name__ == "__main__":
    # Ensure this matches your filename (if your file is finscope.py, use "finscope:app")
    serve_playground_app("finscope:app", reload=True)