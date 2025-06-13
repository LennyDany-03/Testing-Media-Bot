import pandas as pd

# Load CSVs
df1 = pd.read_csv("scrape1.csv")
df2 = pd.read_csv("scrape2.csv")
df3 = pd.read_csv("scrape3.csv")

# Combine
df = pd.concat([df1, df2, df3], ignore_index=True)

# Drop duplicates and empty rows
df.drop_duplicates(subset=["Headline", "URL"], inplace=True)
df.dropna(subset=["Headline", "URL", "Summary"], inplace=True)

# Save combined file
df.to_csv("combined_market_news.csv", index=False)
print("✅ Saved cleaned data to combined_market_news.csv")
