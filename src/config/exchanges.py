import ccxt
import os
from dotenv import load_dotenv

load_dotenv()

def get_exchange_config(exchange_name):
    """
    Configure and return exchange instance
    """
    exchange_config = {
        'apiKey': os.getenv(f'{exchange_name.upper()}_API_KEY'),
        'secret': os.getenv(f'{exchange_name.upper()}_API_SECRET'),
        'enableRateLimit': True,
        'options': {
            'defaultType': 'spot',
            'adjustForTimeDifference': True,
        }
    }
    
    # Exchange-specific configurations
    if exchange_name == 'bitmart':
        exchange_config['uid'] = os.getenv('BITMART_UID')
    
    return exchange_config

def initialize_exchange(exchange_name):
    """
    Initialize exchange connection
    """
    exchange_class = getattr(ccxt, exchange_name)
    config = get_exchange_config(exchange_name)
    exchange = exchange_class(config)
    
    # Set sandbox mode if testing
    if os.getenv('TEST_MODE', 'False').lower() == 'true':
        exchange.set_sandbox_mode(True)
    
    return exchange
