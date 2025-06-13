import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

# Setup options
options = uc.ChromeOptions()
options.add_argument("--no-sandbox")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36")

driver = uc.Chrome(options=options)

try:
    driver.get("https://www.moneycontrol.com/news/business/markets/")

    # Wait until the article blocks are present
    WebDriverWait(driver, 15).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "li.clearfix"))
    )

    article_blocks = driver.find_elements(By.CSS_SELECTOR, "li.clearfix")

    article_list = []

    for block in article_blocks:
        try:
            title_tag = block.find_element(By.CSS_SELECTOR, "h2 a")
            title = title_tag.text.strip()
            link = title_tag.get_attribute("href")
        except:
            title = link = ""

        try:
            summary = block.find_element(By.CSS_SELECTOR, "p").text.strip()
        except:
            summary = ""

        if title and link:
            article_list.append({
                "Title": title,
                "Link": link,
                "Summary": summary
            })

    df = pd.DataFrame(article_list)
    df.to_csv("scrape2.csv", index=False, encoding="utf-8-sig")
    print("✅ Exported to moneycontrol_market_news.csv")

finally:
    driver.quit()
