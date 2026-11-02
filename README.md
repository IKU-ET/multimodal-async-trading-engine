# Multimodal Distributed Multi-Agent Quantitative Architecture

An engineering-first distributed algorithmic trading framework modeled after institutional high-frequency trading (HFT) architectures. The engine separates computational mathematical processing from textual semantic analysis across completely independent microservice system nodes.

## System Topology & Microservices

The repository is divided into decoupled algorithmic processing components that execute concurrently:

*   **`core.py` (Internal Asynchronous Backbone):** A single-process prototype utilizing Python's `asyncio` event loop to coordinate parallel tasks using an in-memory "Whiteboard" state dictionary.
*   **`new_agent.py` (Textual Intelligence Node):** A standalone microservice that simulates live alternative text ingestion feeds. It continuously extracts programmatic sentiment matrix layers (`-1.0` to `+1.0`) and broadcasts them to a shared system pipeline.
*   **`price_agent.py` (Quantitative DSP Execution Node):** A standalone mathematical runtime service that ingests real-time price tick feeds. It maps an adjustable ECE Exponential Moving Average (EMA) smoothing equation to raw inputs to filter out market noise and dynamically intercepts data updates from the Text Node.

## Core System Dials
The mathematical engine variables can be optimized at the top initialization layer of the nodes:
*   `ALPHA_FILTER`: Dictates the digital signal processing noise filtering weight (0.01 to 1.0).
*   `STARTING_CAPITAL`: Sets the initial asset resource liquidity boundary.
