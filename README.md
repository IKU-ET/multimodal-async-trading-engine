# Multimodal Asynchronous Quantitative Trading Architecture

An engineering-first algorithmic trading backtesting engine built to simulate concurrent multi-agent decision matrices. The framework separates high-speed mathematical digital signal processing from slow textual sentiment logic using non-blocking asynchronous event loops.

## Core Engineering Features

* **Asynchronous Non-Blocking Core:** Utilizing Python's `asyncio` event loop to ensure a high-frequency trading simulation engine (Cheetah) executes on market ticks concurrently without suffering data lag or blocking from slow text analysis pipelines (Turtle).
* **Decoupled Shared Cache:** Implements a unified in-memory "Whiteboard" state dictionary acting as a zero-latency database lookup layout for real-time asset alignment.
* **ECE Digital Signal Processing Filter:** Implements an adjustable Exponential Moving Average (EMA) signal smoothing algorithm to clear erratic market noise and locate true price trend breakouts.
* **Real-World Cloud Data Stream:** Integrates the `yfinance` architecture to pipe structured 3-month daily time-series financial datasets straight to your local system paths.
* **Automated Resource Allocation Ledger:** Features a self-calculating accounting matrix that computes capital constraints, handles multi-asset inventory sizing, executes automated entry/liquidation triggers, and logs dynamic performance dashboards.

## System Parameters & Strategy Dials

The architecture features a localized configuration tier at the core initialization line to enable immediate strategic optimization tests:
* `TARGET_TICKER`: The asset baseline target data pipeline (e.g., AAPL).
* `ALPHA_FILTER`: The mathematical tuning knob dictating ECE smoothing noise limits.
* `STARTING_CAPITAL`: The virtual asset liquidity constraint.
