import pandas as pd
import logging

logging.basicConfig(level=logging.INFO)

def clean_data(df):
    try:
        df["Price"] = df["Price"].str.replace("$","").str.replace(",","").astype(float)
        df["Market Cap"] = df["Market Cap"].str.replace("$","").str.replace(",","").astype(float)
        logging.info("Data cleaned successfully.")
        return df
    except Exception as e:
        logging.error(f"Error cleaning data: {e}")
        return df