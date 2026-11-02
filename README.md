# Multimodal Distributed Multi-Agent Hybrid Trading Architecture

An institutional-grade, multi-language distributed algorithmic trading framework modeled after high-frequency trading (HFT) system topologies. The architecture decouples high-speed hardware-level data packet ingestion from text-based alternative intelligence and portfolio execution matrices using separate microservice system nodes.

## System Topology & Microservices Map

The repository is divided into isolated processing layers running concurrently across unique terminal nodes:

*   **`market_engine.c` (Ultra-Low-Latency Hardware Muscle Node):** A native, compiled C engine designed to ingest high-frequency raw network packet arrays at the hardware layer. It bypasses slow runtime environments by updating a low-latency shared tracking memory layout (`live_price_shm.txt`) directly.
*   **`new_agent.py` (Alternative Text Intelligence AI Node):** A standalone microservice that handles incoming unstructured textual pipelines. It simulates live financial headline scraping, extracts numeric sentiment parameters (-1.0 to +1.0), and broadcasts metrics over an independent pipeline loop.
*   **`price_agent.py` (Quantitative Strategy Matrix Core):** A dedicated Python processing node that reads streaming market tick buffers, applies an ECE Exponential Moving Average (EMA) smoothing equation to clean out market noise, and automatically queries the Risk Node for transactional clearances.
*   **`risk_agent.py` (Autonomous Capital Risk Guard Node):** The strict boardroom risk management officer. It intercepts execution requests, audits ledger cache positions against rigid position parameters (`MAX_POSITION_LIMIT`), and issues binding transaction verdicts to protect virtual capital.
*   **`core.py` (Internal Asynchronous Backbone Prototype):** A single-process asynchronous framework model utilizing Python's `asyncio` event loop to simulate parallel task management using an in-memory shared whiteboard.

## Low-Latency Strategy Optimization Dials
*   `ALPHA_FILTER`: Adjusts the digital signal processing noise filtering weight threshold (0.01 to 1.0).
*   `STARTING_CAPITAL`: Dictates the localized financial resource allocation boundary.
*   `MAX_CAPITAL_PER_TRADE_PERCENT`: Enforces strict maximum spending limits per transaction loop.

