"""Accounting calculator for observed/simulated maker fills. No live trading."""
import argparse
import csv
from dataclasses import dataclass
from pathlib import Path

BPS = 10_000.0

@dataclass
class Totals:
    rows: int = 0
    fill_notional_usd: float = 0.0
    spread_capture_usd: float = 0.0
    markout_cost_usd: float = 0.0
    other_cost_usd: float = 0.0
    rebates_usd: float = 0.0
    liquidity_rewards_usd: float = 0.0

    @property
    def net_pnl_usd(self):
        return (self.spread_capture_usd - self.markout_cost_usd -
                self.other_cost_usd + self.rebates_usd +
                self.liquidity_rewards_usd)

    @property
    def net_return_on_filled_notional_pct(self):
        return self.net_pnl_usd / self.fill_notional_usd * 100 if self.fill_notional_usd else 0.0

def calculate(rows):
    totals = Totals()
    required = {"fill_notional_usd", "spread_capture_bps", "markout_bps",
                "other_cost_bps", "rebate_usd", "liquidity_reward_usd"}
    for index, row in enumerate(rows, start=2):
        missing = required - row.keys()
        if missing:
            raise ValueError(f"Row {index} missing columns: {', '.join(sorted(missing))}")
        notional = float(row["fill_notional_usd"])
        if notional < 0:
            raise ValueError(f"Row {index}: fill_notional_usd cannot be negative")
        totals.rows += 1
        totals.fill_notional_usd += notional
        totals.spread_capture_usd += notional * float(row["spread_capture_bps"]) / BPS
        totals.markout_cost_usd += notional * float(row["markout_bps"]) / BPS
        totals.other_cost_usd += notional * float(row["other_cost_bps"]) / BPS
        totals.rebates_usd += float(row["rebate_usd"])
        totals.liquidity_rewards_usd += float(row["liquidity_reward_usd"])
    return totals

def main():
    parser = argparse.ArgumentParser(description="Research-only CSV accounting tool")
    parser.add_argument("--input", required=True, help="Path to input CSV")
    args = parser.parse_args()
    with Path(args.input).open(newline="", encoding="utf-8") as f:
        totals = calculate(csv.DictReader(f))
    print("POLYMARKET EDGE LAB — RESEARCH OUTPUT")
    print("Not a forecast or evidence of future profitability.")
    print(f"Rows:                     {totals.rows}")
    print(f"Filled notional:          ${totals.fill_notional_usd:,.2f}")
    print(f"Gross spread capture:     ${totals.spread_capture_usd:,.4f}")
    print(f"Post-fill markout cost:   ${totals.markout_cost_usd:,.4f}")
    print(f"Other costs:              ${totals.other_cost_usd:,.4f}")
    print(f"Maker rebates:            ${totals.rebates_usd:,.4f}")
    print(f"Liquidity rewards:        ${totals.liquidity_rewards_usd:,.4f}")
    print(f"Net P&L:                  ${totals.net_pnl_usd:,.4f}")
    print(f"Net P&L / filled notional: {totals.net_return_on_filled_notional_pct:.4f}%")
    print("Return on filled notional is not return on capital and can mislead.")

if __name__ == "__main__":
    main()
