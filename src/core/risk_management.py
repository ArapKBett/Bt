class RiskManager:
    def __init__(self, exchange, symbol):
        self.exchange = exchange
        self.symbol = symbol
        self.max_drawdown = 0.05
        
    def check_circuit_breaker(self, initial_balance):
        current_balance = self.exchange.fetch_balance()['free']
        drawdown = (initial_balance - current_balance) / initial_balance
        return drawdown >= self.max_drawdown
    
    def check_inventory_risk(self, base_currency):
        balance = self.exchange.fetch_balance()
        return balance[base_currency] > RISK_PARAMS["max_inventory"]
