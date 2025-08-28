import asyncio
import signal
import sys
from dotenv import load_dotenv

from config.exchanges import initialize_exchange
from core.bot import MarketMakerBot
from utils.logger import logger

# Load environment variables
load_dotenv()

class Application:
    def __init__(self):
        self.bot = None
        self.loop = asyncio.get_event_loop()
        
        # Register signal handlers
        signal.signal(signal.SIGINT, self.signal_handler)
        signal.signal(signal.SIGTERM, self.signal_handler)
    
    def signal_handler(self, signum, frame):
        logger.info(f"Received signal {signum}, shutting down...")
        if self.bot:
            self.bot.is_running = False
        self.loop.stop()
        sys.exit(0)
    
    async def run(self):
        try:
            # Initialize exchange
            exchange_name = os.getenv('EXCHANGE', 'bitmart')
            exchange = initialize_exchange(exchange_name)
            
            # Load trading pairs from environment
            trading_pairs = os.getenv('TRADING_PAIRS', 'BTC/USDT,ETH/USDT').split(',')
            
            # Initialize bot
            self.bot = MarketMakerBot(exchange)
            
            # Fetch initial balance
            initial_balance = exchange.fetch_balance()['USDT']['free']
            logger.info(f"Initial balance: {initial_balance} USDT")
            
            # Run bot for each trading pair
            for pair in trading_pairs:
                logger.info(f"Starting market making for {pair}")
                # In production, you might want to run these in separate threads
                self.bot.run(pair, initial_balance)
                
        except Exception as e:
            logger.error(f"Application error: {e}")
            self.signal_handler(signal.SIGTERM, None)

if __name__ == "__main__":
    app = Application()
    try:
        asyncio.run(app.run())
    except KeyboardInterrupt:
        app.signal_handler(signal.SIGINT, None)
