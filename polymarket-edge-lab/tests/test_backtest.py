import unittest
from edge_lab.backtest import calculate

class BacktestTests(unittest.TestCase):
    def test_net_accounting(self):
        row = {"fill_notional_usd": "1000", "spread_capture_bps": "12",
               "markout_bps": "8", "other_cost_bps": "1",
               "rebate_usd": "0.20", "liquidity_reward_usd": "0.50"}
        result = calculate([row])
        self.assertAlmostEqual(result.spread_capture_usd, 1.2)
        self.assertAlmostEqual(result.markout_cost_usd, 0.8)
        self.assertAlmostEqual(result.other_cost_usd, 0.1)
        self.assertAlmostEqual(result.net_pnl_usd, 1.0)

    def test_empty_input(self):
        result = calculate([])
        self.assertEqual(result.rows, 0)
        self.assertEqual(result.net_pnl_usd, 0.0)

    def test_negative_notional_rejected(self):
        row = {"fill_notional_usd": "-1", "spread_capture_bps": "1",
               "markout_bps": "1", "other_cost_bps": "0",
               "rebate_usd": "0", "liquidity_reward_usd": "0"}
        with self.assertRaises(ValueError):
            calculate([row])

if __name__ == "__main__":
    unittest.main()
