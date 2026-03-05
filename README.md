# 📊 FinScope: AI-Driven Investment Portfolio Simulator
FinScope is an **AI-powered investment portfolio simulator** created to
bridge the gap between complex financial data and practical financial
literacy. By leveraging an **Agentic AI architecture**, the platform
integrates real-time news insights, quantitative market data, and
intelligent strategy coordination to deliver clear and actionable
investment insights for retail investors.

This project was **developed during the Agentic AI Internship at Euron**,
where the primary objective was to design and implement **multi-agent
AI systems capable of performing advanced financial analysis and
decision support**.

Rather than functioning as a traditional financial dashboard,
FinScope operates as a **coordinated ecosystem of specialized AI
agents**. These agents collaborate to analyze market sentiment,
evaluate company fundamentals, and generate strategic portfolio
recommendations. In addition, the platform includes an educational
layer that explains financial metrics such as RSI, EBITDA, and P/E
ratios in real time, helping users not only make decisions but also
understand the reasoning behind them.

------------------------------------------------------------------------

## ❗ The Problem

Retail investors often face **information overload** when analyzing
stock markets. With thousands of indicators, news sources, and financial
metrics available, investors frequently experience **analysis
paralysis** or make decisions without fully understanding the underlying
data.

------------------------------------------------------------------------

## 💡 The Solution

FinScope leverages **Agentic AI** to synthesize financial data and
market sentiment into **clear, actionable, and educational insights**.

Instead of just showing numbers, FinScope explains **why a stock might
be a good or risky investment**, helping users learn how professional
analysts think.

------------------------------------------------------------------------

## 🚀 Key Features

### 🤖 Agentic AI Orchestration

FinScope uses a **Manager--Worker architecture** where specialized AI
agents collaborate to produce comprehensive investment insights.

-   **Strategy Manager** -- Coordinates the analysis and produces the
    final investment strategy.
-   **News Scout** -- Monitors global news and market sentiment using
    DuckDuckGo search.
-   **Quant Analyst** -- Retrieves financial data, stock fundamentals,
    and analyst recommendations using YFinance.

### 📈 Real-Time Market Intelligence

The platform gathers **live financial data and news sentiment** to
provide up-to-date analysis of stocks.

### ⚠️ Risk Analysis

Every recommendation includes a **risk assessment**, helping investors
understand potential volatility before making decisions.

### 📚 Financial Education Mode

FinScope explains complex financial concepts such as: - RSI (Relative
Strength Index) - EBITDA - P/E Ratio - Market Capitalization

This allows users to **learn while analyzing investments**.

------------------------------------------------------------------------

## ⚙️ How It Works

1.  **News Scout Agent 📰** searches for the latest global news related
    to a stock.
2.  **Quant Analyst Agent 📊** retrieves financial data such as stock
    price, fundamentals, and analyst ratings.
3.  **Strategy Manager Agent 🧠** synthesizes both sources and generates
    a detailed investment report.

The result is an **AI-generated investment strategy with explanations
for every recommendation.**

------------------------------------------------------------------------

## 🛠 Tech Stack

-   Python 🐍
-   Phidata (Agno)
-   Groq API ⚡
-   FastAPI 🚀
-   YFinance 📊
-   DuckDuckGo Search 🔎
-   Uvicorn
-   Python Dotenv

------------------------------------------------------------------------

## 📂 Project Structure

FinScope/ ├── finscope.py ├── requirements.txt ├── .env.example └──
README.md

------------------------------------------------------------------------

## 🧑‍💻 Installation

Clone the repository

git clone https://github.com/your-username/finscope.git cd finscope

Create virtual environment

python -m venv .venv source .venv/bin/activate

Install dependencies

pip install -r requirements.txt

Configure environment variables

GROQ_API_KEY=your_groq_api_key

------------------------------------------------------------------------

## ▶️ Running the Application

python finscope.py

------------------------------------------------------------------------

## 🧪 Example Query

Analyze NVIDIA stock and provide investment insights.

FinScope will generate: - 📰 Latest news sentiment - 📊 Financial
fundamentals - ⭐ Analyst ratings - ⚠️ Risk insights - 📈 Strategic
recommendation

------------------------------------------------------------------------

## 🔮 Future Improvements

-   Portfolio optimization simulation
-   Risk scenario modeling
-   Interactive financial dashboards
-   Additional financial API integrations
-   Personalized investor profiles

------------------------------------------------------------------------
