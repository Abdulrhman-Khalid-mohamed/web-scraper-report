import logging
from utils.scraper import scrape_crypto
from utils.processor import clean_data
from utils.reporter import generate_report
import config
import os

logging.basicConfig(level=logging.INFO)

def main():
    for url in config.URLS:
        df = scrape_crypto(url)
        if df.empty:
            logging.warning("No data scraped, skipping report.")
            continue
        df_clean = clean_data(df)
        output_file = os.path.join(config.OUTPUT_FOLDER, "crypto_report.xlsx")
        generate_report(df_clean, output_file)

if __name__ == "__main__":
    main()