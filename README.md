# 📊 Stock Market RAG Bot

A Retrieval-Augmented Generation (RAG) bot that scrapes financial news from multiple sources, processes it, and enables intelligent querying on the combined dataset.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![LangChain](https://img.shields.io/badge/LangChain-Latest-green)

## 🌟 Overview

This project creates an intelligent financial news assistant by:

1. **Scraping** market news from multiple reputable sources
2. **Processing** and combining the data into a unified dataset
3. **Embedding** the information in a vector database
4. **Retrieving** relevant context based on user queries
5. **Generating** accurate, contextual responses using LLMs

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- Chrome browser

### Installation

\`\`\`cmd
# Clone repository (using Git Bash or Git for Windows)
git clone https://github.com/LennyDany-03/stock-market-rag.git
cd stock-market-rag

# Set up virtual environment (CMD)
python -m venv venv
venv\Scripts\activate

# Alternative for PowerShell
# python -m venv venv
# .\venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt
\`\`\`

## 📊 How to Use

### 1. Collect Data
Run each scraper to gather the latest financial news:

\`\`\`cmd
python Economy.py
python MoneyControl.py
python NY-times.py
\`\`\`

### 2. Process Data
Combine and clean the collected data:

\`\`\`cmd
python combain.py
\`\`\`

### 3. Query the Data
Launch the RAG chatbot interface:

\`\`\`cmd
python RAG.py
\`\`\`

### Example Interaction

\`\`\`
❓ Ask a stock market question: What are the latest tech stock trends?

🤖 Based on recent news, tech stocks have shown mixed performance.
   Apple shares rose 2.3% following their AI announcement.
   Nvidia gained 1.7% as demand for AI chips remains strong.
   However, smaller tech companies are facing pressure due to
   rising interest rates.
\`\`\`

## 🧠 Technology Stack

| Category | Technologies |
|----------|--------------|
| **Core** | Python 3.8+, Pandas |
| **Web Scraping** | Selenium, undetected_chromedriver, BeautifulSoup, Requests |
| **AI/ML** | LangChain, ChromaDB |
| **Data Storage** | CSV, ChromaDB Vector Store |
| **Text Processing** | NLTK, spaCy |

## 📁 Project Structure

Directory structure:
└── lennydany-03-testing-media-bot/
    ├── README.md
    ├── combain.py
    ├── Economy.py
    ├── MoneyControl.py
    ├── NY-times.py
    ├── RAG.py
    └── requirements.txt


## ⚙️ Installation

### Prerequisites

- Python 3.8 or higher
- Chrome browser (for Selenium-based scrapers)

### Setup

1. **Clone the repository**

\`\`\`cmd
git clone https://github.com/LennyDany-03/stock-market-rag.git
cd stock-market-rag
\`\`\`

2. **Create and activate a virtual environment**

\`\`\`cmd
# Using CMD
python -m venv venv
venv\Scripts\activate

# Using PowerShell
# If you get execution policy errors, you may need to run:
# Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
# python -m venv venv
# .\venv\Scripts\Activate.ps1
\`\`\`

3. **Install dependencies**

\`\`\`cmd
pip install -r requirements.txt
\`\`\`

## 🚀 Usage

### 1. Data Collection

Run each scraper to collect the latest financial news:

\`\`\`cmd
python Economy.py
python MoneyControl.py
python NY-times.py
\`\`\`

### 2. Data Processing

Combine and clean the collected data:

\`\`\`cmd
python combain.py
\`\`\`

### 3. Launch the RAG Chatbot

Start the interactive query interface:

\`\`\`cmd
python RAG.py
\`\`\`

## 💬 Example Interactions

\`\`\`
❓ Ask a stock market question: What are the latest developments in tech stocks?

🤖 Based on the latest news, tech stocks have shown mixed performance. 
   Apple shares rose 2.3% following their AI announcement at WWDC. 
   Meanwhile, Nvidia continues its upward trend, gaining 1.7% today 
   as demand for AI chips remains strong. However, smaller tech companies 
   are facing pressure due to rising interest rates, with the Nasdaq 
   composite down 0.5% overall.
   
   Sources: [Economic Times (June 15, 2023), NY Times (June 14, 2023)]

❓ Ask a stock market question: How are global markets reacting to the latest Fed decision?

🤖 Global markets have responded cautiously to the Federal Reserve's decision 
   to maintain current interest rates. Asian markets showed modest gains with 
   the Nikkei up 0.8% and Shanghai Composite rising 0.3%. European markets 
   were mixed, with the FTSE 100 down 0.2% while the DAX gained 0.4%.
   
   Sources: [MoneyControl (June 15, 2023), NY Times (June 14, 2023)]
\`\`\`

## 👤 Author

**Lenny Dany Derek D**
- GitHub: [LennyDany-03](https://github.com/LennyDany-03)

---

<p align="center">
  Made with ❤️ for financial market enthusiasts and AI practitioners
</p>
