import threading
import logging
import pandas as pd
from time import sleep
from typing import List

# --- Setup logging ---
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# --- Data Processing ---
class StockDataProcessor:
    def __init__(self, data: pd.DataFrame):
        self.data = data

    def clean_data(self):
        logging.info("Cleaning data...")
        # Simulating data cleaning (e.g., removing NaN values)
        self.data.dropna(inplace=True)
        logging.info(f"Data cleaned: {len(self.data)} rows remaining")

    def analyze_data(self):
        logging.info("Analyzing data...")
        # Simulating some analysis (e.g., calculating moving average)
        self.data['MovingAverage'] = self.data['Price'].rolling(window=3).mean()
        logging.info(f"Data analyzed: {self.data[['Date', 'MovingAverage']].tail()}")

    def process(self):
        self.clean_data()
        self.analyze_data()

# --- Worker for parallel processing ---
class DataProcessorThread(threading.Thread):
    def __init__(self, processor: StockDataProcessor):
        super().__init__()
        self.processor = processor

    def run(self):
        logging.info(f"Starting thread for data processing")
        self.processor.process()
        logging.info(f"Data processing finished")

# --- Simulating Stock Data ---
def generate_stock_data() -> pd.DataFrame:
    # Simulating stock data
    dates = pd.date_range(start='2023-01-01', periods=100, freq='D')
    prices = [100 + (i + (i * 0.02)) for i in range(100)]  # Prices increase with small fluctuations
    return pd.DataFrame({'Date': dates, 'Price': prices})

# --- Main Program ---
def main():
    # Step 1: Generate random stock data
    stock_data = generate_stock_data()
    logging.info("Generated stock data.")

    # Step 2: Create a processor for the data
    processor = StockDataProcessor(stock_data)

    # Step 3: Use threading to process the data in parallel
    thread1 = DataProcessorThread(processor)
    thread2 = DataProcessorThread(processor)

    # Step 4: Start threads
    thread1.start()
    thread2.start()

    # Step 5: Wait for threads to finish
    thread1.join()
    thread2.join()

    logging.info("All threads completed.")

if __name__ == "__main__":
    main()
