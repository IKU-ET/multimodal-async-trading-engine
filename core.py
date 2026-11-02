
import asyncio
import random
import yfinance as yf
import pandas as pd

# CONFIGURATION ZONE - Change these dials to test different strategies!
TARGET_TICKER = "AAPL"   # Try "AAPL", "NVDA", "TSLA", or "RELIANCE.NS"
ALPHA_FILTER = 0.8       # ECE Smoothing factor (0.01 to 1.0)
STARTING_CAPITAL = 50000.0  # Starting virtual money pool

print(f"⏳ Accessing cloud database for {TARGET_TICKER} market signals...")
ticker_data = yf.download(TARGET_TICKER, period="3mo", interval="1d")

if isinstance(ticker_data.columns, pd.MultiIndex):
    ticker_data.columns = ticker_data.columns.get_level_values(0)

price_list = ticker_data['Close'].dropna().tolist()
print(f"Successfully loaded {len(price_list)} days of execution ticks!\n")

# Macro Context Feed Pipeline
news_headlines = [
    "NVIDIA launches next-generation architecture with 2x performance jump",
    "Global chip supply face short-term logistics delays in Europe",
    "Top tech giants place massive new orders for NVIDIA AI hardware",
    "Competitors announce cheaper alternative AI processing units",
    "NVIDIA quarterly profit beats consensus expectations by twenty percent"
]

# Global Whiteboard (Shared Cache)
system_whiteboard = {
    "llm_sentiment": 0.0,
    "system_active": True,
    "virtual_cash": STARTING_CAPITAL,
    "shares_held": 0,
    "total_portfolio_value": STARTING_CAPITAL
}

def analyze_text_sentiment(headline):
    headline_lower = headline.lower()
    if "launch" in headline_lower or "beat" in headline_lower or "massive" in headline_lower:
        return 0.85
    elif "delay" in headline_lower or "competitor" in headline_lower:
        return -0.70
    else:
        return 0.0

# 🐢 THE TURTLE AGENT (Text contextual pipeline)
async def turtle_llm_agent():
    headline_index = 0
    while system_whiteboard["system_active"]:
        await asyncio.sleep(2.0)
        current_headline = news_headlines[headline_index % len(news_headlines)]
        headline_index += 1
        
        processed_score = analyze_text_sentiment(current_headline)
        system_whiteboard["llm_sentiment"] = processed_score

# ⚡ THE CHEETAH MATH AGENT (Upgraded with Automated Portfolio Math Execution)
async def cheetah_math_agent():
    print("[Engine] Core streaming nodes active...")
    ema_price = price_list[0]
    
    for i in range(1, len(price_list)):
        if not system_whiteboard["system_active"]:
            break
            
        await asyncio.sleep(0.2)
        raw_price = price_list[i]
        
        # ECE DSP Filtering transformation
        ema_price = (ALPHA_FILTER * raw_price) + ((1 - ALPHA_FILTER) * ema_price)
        current_sentiment = system_whiteboard["llm_sentiment"]
        
        # Keep tracking total asset net value continuously based on current market price
        system_whiteboard["total_portfolio_value"] = system_whiteboard["virtual_cash"] + (system_whiteboard["shares_held"] * raw_price)
        
        if i % 5 == 0:
            print(f"\n--- Day #{i} Market Ticker Check ---")
            print(f"Price: ${raw_price:.2f} | Filtered Trend: ${ema_price:.2f} | AI Vibe Score: {current_sentiment}")
            
            # AUTOMATED TRADING TRANSACTION EXECUTION
            if raw_price > ema_price and current_sentiment > 0.3 and system_whiteboard["virtual_cash"] > raw_price:
                shares_to_buy = int(system_whiteboard["virtual_cash"] // raw_price)
                if shares_to_buy > 0:
                    system_whiteboard["shares_held"] += shares_to_buy
                    system_whiteboard["virtual_cash"] -= (shares_to_buy * raw_price)
                    print(f"   🟢 EXECUTED BUY: Acquired {shares_to_buy} shares at ${raw_price:.2f} each.")
                    
            elif raw_price < ema_price and current_sentiment < -0.3 and system_whiteboard["shares_held"] > 0:
                shares_to_sell = system_whiteboard["shares_held"]
                system_whiteboard["virtual_cash"] += (shares_to_sell * raw_price)
                system_whiteboard["shares_held"] = 0
                print(f"   🔴 EXECUTED LIQUIDATION: Sold {shares_to_sell} shares at ${raw_price:.2f} each.")
            else:
                print("   ⚪ SYSTEM STATE: HOLDING CURRENT ALLOCATIONS")
                
            print(f"   ↳ [Ledger Audit] Cash Account: ${system_whiteboard['virtual_cash']:.2f} | Active Position: {system_whiteboard['shares_held']} Shares | Net Assets: ${system_whiteboard['total_portfolio_value']:.2f}")

    # Stream wrap up: Force total liquidity liquidation at final price point to audit performance metrics
    final_price = price_list[-1]
    if system_whiteboard["shares_held"] > 0:
        system_whiteboard["virtual_cash"] += (system_whiteboard["shares_held"] * final_price)
        system_whiteboard["shares_held"] = 0
    
    system_whiteboard["total_portfolio_value"] = system_whiteboard["virtual_cash"]
    
    # 🏁 DYNAMIC PERFORMANCE SUMMARY SUMMARY
    print("\n=======================================================")
    print("🏁 BACKTEST SIMULATION COMPLETE")
    print(f"Initial Starting Pool: ${STARTING_CAPITAL:,.2f}")
    print(f"Final Account Net Assets: ${system_whiteboard['total_portfolio_value']:,.2f}")
    
    net_return = ((system_whiteboard["total_portfolio_value"] - STARTING_CAPITAL) / STARTING_CAPITAL) * 100
    print(f"Total Strategy Growth Metric: {net_return:.2f}%")
    print("=======================================================")
    
    system_whiteboard["system_active"] = False

# CENTRAL ORCHESTRATOR OPERATOR RUNNER
async def main():
    print("Powering up the asynchronous system core...\n")
    try:
        await asyncio.gather(
            turtle_llm_agent(),
            cheetah_math_agent()
        )
    except KeyboardInterrupt:
        print("\nStopping engine cleanly...")
        system_whiteboard["system_active"] = False

if __name__ == "__main__":
    asyncio.run(main())
