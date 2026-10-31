# Polymarket Edge Lab

**Research-only prototype. No live trading, wallet integration, or private-key handling.**

A beginner-friendly, reproducible research project to test whether Polymarket liquidity provision, maker rebates, or price discrepancies have a measurable edge after execution costs and adverse selection.

> No profitability is claimed. The included CSV is synthetic and only verifies arithmetic; it is not trading evidence.

## Why this project exists
The research question is whether potential spread capture and platform incentives exceed post-fill adverse selection, operational costs, inventory risk and reward competition.

## Quick start (Python 3.10+, no third-party packages)
```bash
python -m unittest discover -s polymarket-edge-lab/tests -v
python -m polymarket-edge-lab.edge_lab.backtest --input polymarket-edge-lab/data/synthetic_example.csv
```
For easiest execution, download this folder and run the commands from inside it:
```bash
python -m unittest discover -s tests -v
python -m edge_lab.backtest --input data/synthetic_example.csv
```

## Current status
- [x] Research question and safety boundary documented
- [x] Preliminary competitor README audit
- [x] CSV-based accounting calculator and unit tests
- [ ] Live data collector
- [ ] Timestamped order-book replay
- [ ] Conservative queue/partial-fill model
- [ ] Out-of-sample report
- [ ] Shadow-mode validation

## What the calculator measures
Net P&L = spread capture − post-fill markout cost − other costs + realized maker rebates + realized liquidity rewards.

Never treat an advertised reward pool as money earned. Do not double-count spread and fee benefits. The CSV tool is accounting scaffolding, not a complete simulator.

## Risk boundary
Indicative future capital is US$1,000; maximum experimental drawdown tolerance is 10% of deployed capital (nominally US$100 if all capital is deployed). A software stop cannot guarantee losses remain under this limit. Initial live allocation: **US$0**.

No live trading will be added without separate explicit authorization, current eligibility/legal checks, independent review and validated shadow/paper results. Never commit seed phrases, private keys, API secrets or wallet exports. Never bypass geographic or platform restrictions.

## Research references
- [Research memo](docs/research_memo.md)
- [Preliminary open-source audit](docs/competitor_audit.md)
- [Polymarket API overview](https://help.polymarket.com/en/articles/13364254-does-polymarket-have-an-api)
- [Trading fees](https://help.polymarket.com/en/articles/13364478-trading-fees)
- [Maker rebates](https://help.polymarket.com/en/articles/13364471-maker-rebates-program)
- [Liquidity rewards](https://help.polymarket.com/en/articles/13364466-liquidity-rewards)
- [Research data overview](https://institute.polymarket.com/data)

## License
MIT applies to this project's original scaffolding. Referenced external projects retain their own licenses; no external source code is copied here.
