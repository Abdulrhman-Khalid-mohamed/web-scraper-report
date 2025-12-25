import matplotlib.pyplot as plt
import os
import logging

logging.basicConfig(level=logging.INFO)

def generate_report(df, output_file):
    try:
        df.to_excel(output_file, index=False)
        logging.info(f"Report saved to {output_file}")
        plt.figure(figsize=(10,6))
        plt.bar(df["Name"], df["Price"])
        plt.xlabel("Cryptocurrency")
        plt.ylabel("Price (USD)")
        plt.title("Top 10 Cryptocurrencies")
        chart_file = output_file.replace(".xlsx", ".png")
        plt.savefig(chart_file)
        logging.info(f"Chart saved to {chart_file}")
    except Exception as e:
        logging.error(f"Error generating report: {e}")