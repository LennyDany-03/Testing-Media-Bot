<div align="center">
  
# 📈 Stock Market RAG Bot

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![LangChain](https://img.shields.io/badge/LangChain-Enabled-green.svg)](https://langchain.com/)
[![OpenAI](https://img.shields.io/badge/OpenAI-Powered-orange.svg)](https://openai.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

<p align="center">
  <img src="https://raw.githubusercontent.com/sindresorhus/awesome/main/media/logo.svg" alt="Logo" width="200" height="200">
</p>

**Intelligent financial news analysis powered by RAG technology**

</div>

<p align="center">
  <a href="#features">Features</a> •
  <a href="#technologies">Technologies</a> •
  <a href="#installation">Installation</a> •
  <a href="#usage">Usage</a> •
  <a href="#example">Example</a> •
  <a href="#roadmap">Roadmap</a> •
  <a href="#license">License</a>
</p>

---

## 🌟 Overview

The Stock Market RAG Bot is an intelligent system that scrapes financial market news from multiple sources, processes the data, and enables users to ask natural language questions about market trends, company performance, and economic indicators.

\`\`\`
                     ┌───────────────┐
                     │  News Sources │
                     └───────┬───────┘
                             │
                             ▼
┌───────────────┐    ┌───────────────┐    ┌───────────────┐
│  Economic     │───▶│  Data         │◀───│  MoneyControl │
│  Times        │    │  Processing   │    │               │
└───────────────┘    └───────┬───────┘    └───────────────┘
                             │                     ▲
                             ▼                     │
                     ┌───────────────┐             │
                     │  Vector       │             │
                     │  Database     │             │
                     └───────┬───────┘             │
                             │                     │
                             ▼                     │
┌───────────────┐    ┌───────────────┐    ┌───────────────┐
│  User         │───▶│  RAG          │───▶│  NY Times     │
│  Query        │    │  Pipeline     │    │               │
└───────────────┘    └───────────────┘    └───────────────┘
\`\`\`

## ✨ Features <a name="features"></a>

- 🔍 **Multi-source News Scraping**
  - Economic Times (`Economy.py`)
  - MoneyControl (`MoneyControl.py`) 
  - NY Times (`NY-times.py`)
  
- 🧹 **Intelligent Data Processing**
  - Cleans and merges data from multiple sources (`combain.py`)
  - Removes duplicates and normalizes text
  - Stores final dataset in `combined_market_news.csv`
  
- 🤖 **Advanced RAG Pipeline**
  - Semantic search over financial news
  - Context-aware responses to market queries
  - Natural language understanding of complex financial concepts

- 📊 **Financial Insights**
  - Market trend analysis
  - Company performance tracking
  - Economic indicator monitoring

## 🛠️ Technologies <a name="technologies"></a>

<table>
  <tr>
    <td align="center"><img src="https://www.python.org/static/community_logos/python-logo.png" width="100px;" alt=""/><br /><b>Python</b></td>
    <td align="center"><img src="https://www.selenium.dev/images/selenium_logo_square_green.png" width="100px;" alt=""/><br /><b>Selenium</b></td>
    <td align="center"><img src="https://pandas.pydata.org/static/img/pandas_mark.svg" width="100px;" alt=""/><br /><b>Pandas</b></td>
  </tr>
  <tr>
    <td align="center"><img src="https://avatars.githubusercontent.com/u/126733545?s=200&v=4" width="100px;" alt=""/><br /><b>LangChain</b></td>
    <td align="center"><img src="https://www.chromadb.com/img/chroma.svg" width="100px;" alt=""/><br /><b>ChromaDB</b></td>
    <td align="center"><img src="https://www.crummy.com/software/BeautifulSoup/bs4/doc/_images/6.1.jpg" width="100px;" alt=""/><br /><b>BeautifulSoup</b></td>
  </tr>
</table>

## 📁 Project Structure

\`\`\`
Stock-Market-RAG-Bot/
│
├── Economy.py            # Scrapes Economic Times
├── MoneyControl.py       # Scrapes MoneyControl
├── NY-times.py           # Scrapes NY Times
├── combain.py            # Cleans and merges all CSVs
├── RAG.py                # RAG-based chatbot interface
├── requirements.txt      # Python dependencies
├── combined_market_news.csv  # Final cleaned dataset
└── venv/                 # Virtual environment
\`\`\`

## 🚀 Installation <a name="installation"></a>

1. **Clone the repository**
   \`\`\`bash
   git clone https://github.com/your-username/stock-market-rag-bot.git
   cd stock-market-rag-bot
   \`\`\`

2. **Create and activate a virtual environment**
   \`\`\`bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   \`\`\`

3. **Install dependencies**
   \`\`\`bash
   pip install -r requirements.txt
   \`\`\`

4. **Set up environment variables**
   \`\`\`bash
   # Create a .env file with your API keys
   echo "OPENAI_API_KEY=your_openai_api_key" > .env
   \`\`\`

## 📋 Usage <a name="usage"></a>

### 1. Scrape the latest news

Run each scraper to collect the most recent financial news:

\`\`\`bash
python Economy.py
python MoneyControl.py
python NY-times.py
\`\`\`

### 2. Process and combine the data

\`\`\`bash
python combain.py
\`\`\`

### 3. Start the RAG chatbot

\`\`\`bash
python RAG.py
\`\`\`

## 💬 Example Interaction <a name="example"></a>

\`\`\`
🤖 Stock Market RAG Bot initialized! Ask me anything about recent financial news.
❓ Ask a stock market question (type 'exit' to quit): What are the current trends in tech stocks?

📊 Based on recent news, tech stocks have been showing mixed performance. 
   Apple and Microsoft have reported strong quarterly earnings, driving their 
   stock prices up by 3.2% and 2.8% respectively. However, there are concerns 
   about semiconductor shortages affecting the broader tech sector. 
   
   The NASDAQ composite index has gained 1.5% this week, outperforming the 
   S&P 500. Analysts are particularly watching AI-related stocks, which have 
   seen significant volatility but remain on an upward trend for the year.
   
   Would you like more specific information about any particular tech company?

❓ Ask a stock market question (type 'exit' to quit): exit
🤖 Thank you for using Stock Market RAG Bot! Goodbye!
\`\`\`

## ⚠️ Notes

- Some warnings (e.g., `[WinError 6] The handle is invalid`) are safe to ignore as they occur during WebDriver cleanup
- Make sure ChromeDriver and browser versions match
- The bot provides information based on the most recently scraped articles, not real-time data

## 🗺️ Roadmap <a name="roadmap"></a>

- [ ] Automate daily scraping using CRON or Task Scheduler
- [ ] Integrate live market data APIs
- [ ] Deploy as a web app using Flask or FastAPI
- [ ] Add sentiment analysis for news articles
- [ ] Implement user authentication system
- [ ] Create visualization dashboard for market trends

## 📄 License <a name="license"></a>

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Lenny Dany Derek D**

[![GitHub](https://img.shields.io/badge/GitHub-Profile-blue?style=flat&logo=github)](https://github.com/your-username)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue?style=flat&logo=linkedin)](https://linkedin.com/in/your-username)

---

<div align="center">
  <sub>Built with ❤️ by Lenny Dany Derek D</sub>
</div>
