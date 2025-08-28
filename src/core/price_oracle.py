import numpy as np
import ccxt

class PriceOracle:
    def __init__(self, exchange):
        self.exchange = exchange
        
    def get_vwap(self, symbol, period=30):
        """Calculate Volume-Weighted Average Price"""
        ohlcv = self.exchange.fetch_ohlcv(symbol, timeframe='1m', limit=period)
        closes = np.array([x[4] for x in ohlcv])
        volumes = np.array([x[5] for x in ohlcv])
        return np.sum(closes * volumes) / np.sum(volumes)
    
    def get_ema_ratio(self, symbol):
        """Calculate EMA trend ratio"""
        ohlcv = self.exchange.fetch_ohlcv(symbol, timeframe='1m', limit=30)
        closes = [x[4] for x in ohlcv]
        ema_short = self.calc_ema(closes, 5)
        ema_long = self.calc_ema(closes, 20)
        return ema_short / ema_long

    @staticmethod
    def calc_ema(data, period):
        weights = np.exp(np.linspace(-1., 0., period))
        weights /= weights.sum()
        return np.convolve(data, weights, mode='valid')[0]
