# 🚀 How to Use: Stock Market RAG Bot (Windows)

This guide shows how to run the project using **PowerShell** or **CMD** on Windows.

---

## 🛠️ Step 1: Clone the Repository

### PowerShell or CMD

```powershell
git clone https://github.com/your-username/stock-market-rag-bot.git
cd Testing-Media-Bot
 ```

🧪 Step 2: Create and Activate Virtual Environment

PowerShell
```powershell
python -m venv venv
.\venv\Scripts\activate
 ```
CMD
```powershell
python -m venv venv
venv\Scripts\activate.bat
 ```
📦 Step 3: Install Required Libraries

PowerShell or CMD (after activating the virtual environment)
```powershell
pip install -r requirements.txt
 ```
📥 Step 4: Run the News Scraper Scripts

These scripts extract financial news and save it as CSV files.
```powershell
python Economy.py          # → market_news.csv
python MoneyControl.py     # → moneycontrol_market_news.csv
python NY-times.py         # → nytimes_economy_news.csv
 ```
🧹 Step 5: Combine and Clean All News Data
```powershell
python combain.py          # → combined_market_news.csv
 ```
💬 Step 6: Start the RAG Chatbot
```powershell
python RAG.py
 ```
You'll see:
```powershell
💡 Stock Market RAG Bot Initialized! Ask questions based on the news dataset.

❓ Ask a stock market question (type 'exit' to quit): which stocks are good today?

💬 Based on the news, ICICI Bank and HCL Tech are potential buys...
```
🛑 To Exit the Bot

Just type: ``` exit ``` 

🧑‍💻 Developed & Maintained by
Lenny Dany Derek D
🔗 GitHub: LennyDany-03
📂 Repo: Testing-Media-Bot
