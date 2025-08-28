# Strategy Parameters
RISK_PARAMS = {
    "max_inventory": 1000,           # Max base currency holdings
    "inventory_skew": 0.05,          # ±5% inventory tolerance
    "vwap_period": 30,               # VWAP time window (minutes)
    "min_spread": 0.001,             # 0.1% minimum spread
    "max_spread": 0.01,              # 1% maximum spread
    "circuit_breaker_drawdown": 0.05, # 5% drawdown triggers halt
    "ema_short": 5,                  # Short EMA period
    "ema_long": 20                   # Long EMA period
}
