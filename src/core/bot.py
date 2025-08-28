import time
from .price_oracle import PriceOracle
from .risk_management import RiskManager

class MarketMakerBot:
    def __init__(self, exchange):
        self.exchange = exchange
        self.oracle = PriceOracle(exchange)
        self.risk_manager = RiskManager(exchange, symbol)
        self.is_running = False
        
    def calculate_spread(self, symbol):
        vwap = self.oracle.get_vwap(symbol)
        ema_ratio = self.oracle.get_ema_ratio(symbol)
        
        # Dynamic spread based on volatility
        spread = max(RISK_PARAMS["min_spread"], 
                    min(RISK_PARAMS["max_spread"], 0.005 * (1/ema_ratio)))
        
        bid_price = vwap * (1 - spread)
        ask_price = vwap * (1 + spread)
        return bid_price, ask_price
    
    def run(self, symbol, initial_balance):
        self.is_running = True
        while self.is_running:
            try:
                if self.risk_manager.check_circuit_breaker(initial_balance):
                    self.cancel_all_orders(symbol)
                    break
                    
                bid, ask = self.calculate_spread(symbol)
                self.place_orders(symbol, bid, ask)
                time.sleep(30)
                
            except Exception as e:
                self.handle_error(e)
    
    def place_orders(self, symbol, bid_price, ask_price):
        # Cancel existing orders first
        self.exchange.cancel_all_orders(symbol)
        
        # Place new orders
        self.exchange.create_limit_buy_order(
            symbol, 
            amount=self.calculate_order_size(),
            price=bid_price
        )
        self.exchange.create_limit_sell_order(
            symbol,
            amount=self.calculate_order_size(),
            price=ask_price
          )
