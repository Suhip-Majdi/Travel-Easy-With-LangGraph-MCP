# ✈️ Travel Easy with LangGraph & MCP

An intelligent multi-agent travel planning system built with **LangGraph**, **MCP (Model Context Protocol)**, **PostgreSQL Memory**, and **Streamlit**.

The application uses specialized AI agents to collaboratively generate personalized travel plans, search destinations, retrieve weather forecasts, gather flight information, and maintain conversational memory across interactions.

---

## 🚀 Overview

Travel Easy is a real-world AI application that demonstrates how multiple AI agents can work together to solve complex travel-planning tasks.

Instead of relying on a single LLM call, the system orchestrates several specialized agents through LangGraph, enabling:

* Destination research
* Flight information retrieval
* Weather forecasting
* Hotel recommendations
* Trip itinerary generation
* Persistent memory using PostgreSQL

The project also integrates MCP servers to provide real-time external data access.

---

## ✨ Features

### Multi-Agent Architecture

Uses LangGraph to coordinate specialized AI agents.

### Persistent Memory

Stores conversation history and checkpoints using PostgreSQL.

### Real-Time Search

Uses Tavily Search MCP for destination research and web search.

### Flight Information

Retrieves airline and airport information through AviationStack MCP.

### Weather Forecasts

Provides destination weather insights using OpenWeather APIs.

### Interactive UI

Streamlit-powered web application for an intuitive user experience.

### Scalable Design

Designed using modular agent architecture for future expansion.

---

## 🏗️ System Architecture

```text
User
 │
 ▼
Travel Coordinator Agent
 │
 ├── Destination Agent
 │      └── Tavily Search MCP
 │
 ├── Flight Agent
 │      └── AviationStack MCP
 │
 ├── Weather Agent
 │      └── OpenWeather MCP
 │
 ├── Hotel Agent
 │      └── Tavily Search MCP
 │
 ▼
LangGraph Workflow
 │
 ▼
PostgreSQL Memory
 │
 ▼
Final Travel Plan
```

---

## 🛠️ Tech Stack

### AI & Orchestration

* LangGraph
* LangChain
* Groq LLM
* MCP (Model Context Protocol)

### Data Sources

* Tavily Search
* AviationStack API
* OpenWeather API

### Backend

* Python
* PostgreSQL
* Psycopg

### Frontend

* Streamlit

---

## 📂 Project Structure

```text
Travel-Easy-With-LangGraph-MCP/
│
├── frontend.py
├── main.py
├── mcp_client.py
├── .env
├── requirements.txt
│
├── checkpoints/
├── assets/
└── README.md
```

### Key Files

| File          | Description                                      |
| ------------- | ------------------------------------------------ |
| main.py       | LangGraph workflow and agent definitions         |
| frontend.py   | Streamlit user interface                         |
| mcp_client.py | MCP integrations and external tool communication |
| .env          | Environment variables                            |
| README.md     | Project documentation                            |

---

## 🔑 Required API Keys

Create accounts and generate API keys from:

* Groq
* Tavily
* AviationStack
* OpenWeatherMap

---

## ⚙️ Environment Setup

### 1. Clone Repository

```bash
git clone https://github.com/Suhip-Majdi/Travel-Easy-With-LangGraph-MCP.git

cd Travel-Easy-With-LangGraph-MCP
```

---

### 2. Create Virtual Environment

```bash
python -m venv agentenv
```

Activate:

#### Windows

```bash
agentenv\Scripts\activate
```

#### Linux / macOS

```bash
source agentenv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

If requirements.txt is unavailable:

```bash
pip install langgraph
pip install langchain
pip install langchain-openai
pip install langchain-groq
pip install langchain-community
pip install langchain-tavily
pip install streamlit
pip install requests
pip install python-dotenv
pip install psycopg[binary]
pip install psycopg_pool
pip install langgraph-checkpoint-postgres
```

---

## 🐘 PostgreSQL Setup

### Create Database

```sql
CREATE DATABASE langgraph_memory_demo;
```

### Example Connection String

```env
DATABASE_URL=postgresql://postgres:YOUR_PASSWORD@localhost:5432/langgraph_memory_demo
```

---

## 🔐 Environment Variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY=YOUR_GROQ_API_KEY

TAVILY_API_KEY=YOUR_TAVILY_API_KEY

AVIATIONSTACK_API_KEY=YOUR_AVIATIONSTACK_API_KEY

OPENWEATHER_API_KEY=YOUR_OPENWEATHER_API_KEY

DATABASE_URL=postgresql://postgres:YOUR_PASSWORD@localhost:5432/langgraph_memory_demo
```

---

## 🔌 MCP Integrations

### Tavily MCP

Provides:

* Web Search
* Destination Research
* Hotel Discovery

### AviationStack MCP

Provides:

* Airport Information
* Airline Information
* Flight Data

### Weather MCP

Provides:

* Current Weather
* Forecast Data
* Travel Weather Insights

---

## ▶️ Running the Application

### Streamlit Interface

```bash
streamlit run frontend.py
```

---

### Terminal Version

```bash
python main.py
```

---

## 💡 Example Prompts

```text
Plan a 7-day trip to Japan under $2,000 including flights, hotels, and sightseeing.
```

```text
Create a family-friendly travel itinerary for Dubai with a budget of $3,000.
```

```text
Suggest a luxury 5-day trip to Switzerland including weather forecasts and hotel recommendations.
```

---

## 📈 Future Improvements

* Flight booking integration
* Hotel booking APIs
* Expense optimization
* Interactive maps
* Multi-language support
* Voice-enabled travel assistant
* RAG-based travel knowledge base

---

## 👨‍💻 Author

Suhaib Majdi

AI Engineer | Generative AI Developer | Multi-Agent Systems Enthusiast

LinkedIn:
(Add your LinkedIn profile here)

GitHub:
https://github.com/Suhip-Majdi

---

## ⭐ Support

If you found this project useful, consider starring the repository and sharing it with others interested in:

* Generative AI
* LangGraph
* Multi-Agent Systems
* MCP
* AI Travel Assistants
