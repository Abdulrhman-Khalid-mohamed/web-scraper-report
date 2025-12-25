import requests
from bs4 import BeautifulSoup
import pandas as pd
import logging

logging.basicConfig(level=logging.INFO)

def scrape_crypto(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "lxml")
        table = soup.find("table")
        rows = table.tbody.find_all("tr")[:10]
        data = []
        for row in rows:
            cols = row.find_all("td")
            name = cols[2].p.text
            price = cols[3].a.text
            market_cap = cols[6].p.text
            data.append({"Name": name, "Price": price, "Market Cap": market_cap})
        df = pd.DataFrame(data)
        logging.info("Scraping completed successfully.")
        return df
    except Exception as e:
        logging.error(f"Error scraping website: {e}")
        return pd.DataFrame()