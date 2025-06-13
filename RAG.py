import pandas as pd
from langchain_ollama import OllamaLLM
from langchain_community.vectorstores import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA
import csv

# Step 1: Load the CSV dataset safely
df = pd.read_csv("combined_market_news.csv", quoting=csv.QUOTE_ALL)

# Step 2: Convert rows into LangChain Documents (skip rows with missing Summary)
docs = []
for _, row in df.iterrows():
    headline = str(row.get("Headline", "")).strip()
    summary = str(row.get("Summary", "")).strip()
    url = str(row.get("URL", "")).strip()

    if not summary:  # Skip entries without meaningful content
        continue

    content = f"Headline: {headline}\n\nSummary: {summary}\n\nURL: {url}"
    docs.append(Document(page_content=content))


# Step 3: Split documents into manageable chunks
splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
split_docs = splitter.split_documents(docs)

# Step 4: Generate vector embeddings
embedding = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# Step 5: Store vectors in ChromaDB
vectordb = Chroma.from_documents(split_docs, embedding=embedding, persist_directory="./chroma_db")
vectordb.persist()

# Step 6: Load LLaMA model via Ollama
llm = OllamaLLM(model="llama3.2")

# Step 7: Setup Retrieval-Augmented QA
qa = RetrievalQA.from_chain_type(llm=llm, retriever=vectordb.as_retriever())

# Step 8: Run interactive chatbot
print("\n💡 Stock Market RAG Bot Initialized! Ask questions based on the news dataset.")
while True:
    query = input("\n❓ Ask a stock market question (type 'exit' to quit): ").strip()
    if query.lower() == 'exit':
        print("👋 Exiting. Have a great day!")
        break

    try:
        result = qa.invoke({"query": query})
        print(f"\n💬 {result['result'] if isinstance(result, dict) else result}")
    except Exception as e:
        print(f"⚠️ Error: {e}")
