import unittest
from unittest.mock import Mock, patch
import numpy as np

from src.core.price_oracle import PriceOracle

class TestPriceOracle(unittest.TestCase):
    
    def setUp(self):
        self.mock_exchange = Mock()
        self.oracle = PriceOracle(self.mock_exchange)
    
    @patch('numpy.convolve')
    def test_calc_ema(self, mock_convolve):
        # Mock the convolve function
        mock_convolve.return_value = [100.0]
        
        data = [95, 100, 105, 100, 95]
        result = self.oracle.calc_ema(data, 5)
        
        self.assertEqual(result, 100.0)
        mock_convolve.assert_called_once()
    
    def test_get_vwap(self):
        # Mock OHLCV data
        mock_ohlcv = [
            [None, None, None, None, 100, 10],  # [timestamp, open, high, low, close, volume]
            [None, None, None, None, 101, 20],
            [None, None, None, None, 102, 30],
        ]
        self.mock_exchange.fetch_ohlcv.return_value = mock_ohlcv
        
        result = self.oracle.get_vwap('BTC/USDT', 3)
        
        # Expected VWAP: (100*10 + 101*20 + 102*30) / (10+20+30) = 101.33
        expected = (100*10 + 101*20 + 102*30) / (10+20+30)
        self.assertAlmostEqual(result, expected, places=2)
        
if __name__ == '__main__':
    unittest.main()
