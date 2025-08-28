# Market Making Bot

A production-ready market making bot designed to provide liquidity while resisting manipulation.

## Features

- VWAP-based pricing to avoid last-price anchoring
- Dynamic spreads based on market volatility
- Circuit breakers for risk management
- Multi-exchange support (Bitmart, LBank, MintMe)
- Inventory management and position limits

## Setup

1. Clone the repository:
`git clone https://github.com/ArapKBett/Bt
cd Bt`

2. Install dependencies
   `pip install -r requirements.txt`

3. Set up environment variables
   `cp .env.example .env`

4. Run the bot
   `python src/main.py`

Docker deployment 
1. Build image
   `docker build -t market-making-bot .`

2. Run the container
   `docker run -d --name mm-bot --env-file .env market-making-bot`

   
