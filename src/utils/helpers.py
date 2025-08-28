import math
import time
from datetime import datetime

def calculate_order_size(balance, price, risk_percentage=0.02):
    """
    Calculate order size based on available balance and risk percentage
    """
    return (balance * risk_percentage) / price

def truncate(value, decimals=8):
    """
    Truncate a number to specified decimals
    """
    return math.floor(value * 10 ** decimals) / 10 ** decimals

def retry_api_call(func, max_retries=3, delay=1):
    """
    Retry API call with exponential backoff
    """
    for i in range(max_retries):
        try:
            return func()
        except Exception as e:
            if i == max_retries - 1:
                raise e
            time.sleep(delay * (2 ** i))
    
def timestamp_to_date(timestamp):
    """
    Convert timestamp to readable date
    """
    return datetime.fromtimestamp(timestamp / 1000).strftime('%Y-%m-%d %H:%M:%S')
