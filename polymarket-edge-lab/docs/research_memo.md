# Research memo — 2026-10-31

## Executive conclusion
No strategy is approved for live trading. Initial research priority: maker liquidity with explicit post-fill markout measurement. Run an arbitrage scanner as a second track. Simple reward farming must not be presumed profitable.

A particularly relevant warning appears in the public `yluoc/polymaker` README: its author reports that a small-wallet live test lost more to adverse selection than it earned from liquidity rewards. This is self-reported, not an independent audit, but it directly challenges the passive-income hypothesis.

## Strategy hypotheses

### H1 — Maker liquidity / maker rebates
Potential revenue: spread capture plus eligible rebates and/or liquidity rewards.
Risks: adverse selection, queue priority, partial fills, inventory imbalance, resolution exposure, reward dilution and cancellation latency.
Evidence needed: order-book replay, measured markouts at multiple horizons, rewards attributed to eligible quotes, and inventory/resolution P&L.

### H2 — Cross-market arbitrage
Potential revenue: acquire logically equivalent claims for less than their executable payout bound.
Risks: contracts may not be equivalent; resolution wording may differ; one leg may fill without the other; displayed liquidity may be too small; capital may be locked.
Evidence needed: contract-rule matching, depth-aware two-leg execution simulation, partial-fill handling and settlement audit.

### H3 — Directional / order-book imbalance
Potential revenue: a signal predicts price better than the market after costs.
Risks: signal decay, leakage, regime shifts, fees and overfitting.
Priority: lower until a defensible, independently validated signal exists.

## Official platform mechanics to encode
Official help pages describe category-specific taker fees, maker rebates funded by eligible taker fees, and market-specific liquidity rewards with spread/size eligibility and payout thresholds. Terms can change; capture the live terms and retrieval timestamp rather than hard-coding program rates.

The official data overview describes market data and historical price endpoints suitable for research. Historical prices alone are insufficient for a credible maker-fill simulation; timestamped order-book depth and trade data are needed.

## Evaluation protocol
1. Save immutable timestamped snapshots, trades, fee metadata, reward rules and market resolution wording.
2. Replay only information available at each historical timestamp; prohibit look-ahead bias.
3. Model queue position, partial fills, trade-through, cancel latency and post-fill adverse movement.
4. Separate spread capture, markout, costs, realized rebates, realized rewards, inventory mark-to-market and resolution P&L.
5. Tune only on a training period; freeze parameters before out-of-sample tests.
6. Report net P&L, max drawdown, worst day, fill rate, capital utilization, event exposure, turnover, markouts by horizon and confidence intervals.
7. Run real-time shadow mode before any live execution is considered.

## Capital and acceptance gates
Future capital budget: US$1,000. Maximum experimental drawdown tolerance: 10% of deployed capital (nominally US$100 if all capital is deployed); actual losses may exceed a stop due to gaps, illiquidity or failed cancellation. Initial live allocation: US$0.

Minimum gates before considering deployment:
- At least 30 days of clean shadow data across varied market conditions (necessary but not sufficient).
- Positive net P&L in a separate out-of-sample period using conservative fill/cost assumptions.
- Results not dominated by one market or exceptional event.
- Stress tests with worse fills, higher markouts, lower rewards and API interruptions.
- Reproducible tests, independent code/security review, current eligibility/legal checks, and separate explicit user authorization.

## Sources
- https://help.polymarket.com/en/articles/13364254-does-polymarket-have-an-api
- https://help.polymarket.com/en/articles/13364478-trading-fees
- https://help.polymarket.com/en/articles/13364471-maker-rebates-program
- https://help.polymarket.com/en/articles/13364466-liquidity-rewards
- https://institute.polymarket.com/data
- https://github.com/yluoc/polymaker
- https://github.com/GoPolymarket/polymarket-trader
