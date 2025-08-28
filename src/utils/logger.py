import logging
import os
from logging.handlers import RotatingFileHandler

def setup_logger(name, log_file='market_maker.log', level=logging.INFO):
    """
    Setup logger with file and console handlers
    """
    # Create logs directory if it doesn't exist
    os.makedirs('logs', exist_ok=True)
    
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    
    # File handler with rotation
    file_handler = RotatingFileHandler(
        f'logs/{log_file}', 
        maxBytes=10*1024*1024,  # 10MB
        backupCount=5
    )
    file_handler.setFormatter(formatter)
    
    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    
    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    return logger

# Global logger instance
logger = setup_logger('market_maker')
