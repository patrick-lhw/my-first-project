# Preliminary open-source competitor audit

**Scope:** README-level triage only, not a line-by-line source-code, license or security audit. Record commit SHA and date before deeper review.

## 1. yluoc/polymaker
https://github.com/yluoc/polymaker

Reported design: maker-only CLOB V2 bot, Gamma-based market selection, post-only two-sided quoting around microprice, inventory management and liquidity-reward targeting. README describes paper mode and separate live gates.

Key lesson: its README explicitly reports that a small live test lost more to adverse selection than rewards generated. That is the strongest initial warning against treating rewards as passive income.

Verify in source: queue position, partial fills, cancellation latency, reward attribution versus actual payouts, resolution inventory, fail-closed behavior on stale data, secret handling, dependencies and test coverage.

Decision: research reference only until code-level review and reproducible tests.

## 2. GoPolymarket/polymarket-trader
https://github.com/GoPolymarket/polymarket-trader

Reported design: Go-based CLOB bot with market making and order-book imbalance signal; paper/dry-run modes; per-market caps, daily loss controls and consecutive-loss cooldown; WebSocket feed and staged rollout.

Caution: its README describes a volume-generation / Builder Program objective. Volume or grant qualification is not positive trading P&L. Paper mode and risk controls do not prove profitability.

Verify in source: fill realism, queue and markout handling, realized plus unrealized loss calculations, out-of-sample signal tests, authentication, secret logging, license and dependency health.

Decision: possible architecture reference; do not copy or deploy before code, license and security review.

## Comparison

| Dimension | polymaker | polymarket-trader |
|---|---|---|
| Focus | Maker liquidity/rewards | Market making + directional signal |
| Explicit adverse-selection warning | Yes, in README | Not established by README |
| Paper/dry-run | Reported | Reported |
| Independent profitability evidence | Not established; README reports losses in small live test | Not found in this preliminary review |
| Research use | Reward-versus-markout framing | Architecture and risk-gate reference |

## Audit standard
A full audit should capture commit SHA, exact license, CI/test results, dependency tree, open issues, API version assumptions, fill-model behavior and whether tests reproduce claimed outputs. Stars, marketing, screenshots and short cherry-picked samples are not profitability evidence.
