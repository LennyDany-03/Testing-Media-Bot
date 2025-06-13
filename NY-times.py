import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time
import random

# Setup undetected Chrome options
options = uc.ChromeOptions()
options.add_argument("--no-sandbox")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36")

driver = uc.Chrome(options=options)

try:
    driver.get("https://www.nytimes.com/section/business/economy")

    # Wait until articles are present
    WebDriverWait(driver, 20).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "section#stream-panel ol li"))
    )

    # Scroll to ensure all dynamic content loads
    for _ in range(3):
        driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")
        time.sleep(random.uniform(1, 2))

    # Get all article <li> blocks
    articles = driver.find_elements(By.CSS_SELECTOR, "section#stream-panel ol li")

    data = []

    for article in articles:
        try:
            h3 = article.find_element(By.TAG_NAME, "h3").text.strip()
            a_tag = article.find_element(By.TAG_NAME, "a").get_attribute("href")
            p = article.find_element(By.TAG_NAME, "p").text.strip()
        except:
            continue

        if h3 and a_tag:
            data.append({
                "Headline": h3,
                "Link": a_tag,
                "Summary": p
            })

    df = pd.DataFrame(data)
    df.to_csv("scrape3.csv", index=False, encoding="utf-8-sig")
    print("✅ Exported to nytimes_economy_news.csv")

finally:
    driver.quit()
