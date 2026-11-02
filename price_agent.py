import asyncio
import os

# CONFIGURATION ZONE
ALPHA_FILTER = 0.8
STARTING_CAPITAL = 50000.0

# Mock stream of incoming "Live" price ticks (Phase 2 style)
live_market_ticks = [150.20, 151.45, 152.10, 149.80, 148.50, 153.25, 154.10, 152.00]

async def start_price_node():
    print(" [Price Agent Node] Powered Up. Listening for live market ticks...")
    
    # Initialize portfolio variables locally
    virtual_cash = STARTING_CAPITAL
    shares_held = 0
    ema_price = live_market_ticks[0]  # Initialize with first price point
    
    try:
        for i, raw_price in enumerate(live_market_ticks):
            await asyncio.sleep(2.0)  # Simulating a live tick arriving every 2 seconds
            
            #  ECE DSP Noise Filtering Math
            ema_price = (ALPHA_FILTER * raw_price) + ((1 - ALPHA_FILTER) * ema_price)
            
            #  LOOKUP CHANNEL: Read what the News AI Agent is currently broadcasting
            current_sentiment = 0.0  # Default if the News AI hasn't written anything yet
            if os.path.exists("sentiment_stream.txt"):
                with open("sentiment_stream.txt", "r") as f:
                    try:
                        current_sentiment = float(f.read().strip())
                    except ValueError:
                        pass
            
            print(f"\n[Price Agent] Tick #{i+1} Arrived -> Live Price: ${raw_price:.2f} | Filtered Trend: ${ema_price:.2f}")
            print(f"   ↳ Checking News AI Broadcast Pipeline... Current Sentiment: {current_sentiment}")
            
            # COORDINATED SWARM DECISION MATRIX
            if raw_price > ema_price and current_sentiment > 0.3 and virtual_cash > raw_price:
                shares_to_buy = int(virtual_cash // raw_price)
                shares_held += shares_to_buy
                virtual_cash -= (shares_to_buy * raw_price)
                print(f"    SWARM ACTION TRIGGERED: BUY ORDER EXECUTED for {shares_to_buy} shares.")
                
            elif raw_price < ema_price and current_sentiment < -0.3 and shares_held > 0:
                print(f"    SWARM ACTION TRIGGERED: LIQUIDATING {shares_held} SHARES immediately due to negative news context.")
                virtual_cash += (shares_held * raw_price)
                shares_held = 0
            else:
                print("      SWARM ACTION TRIGGERED: HOLDING CURRENT ALLOCATIONS (Signals do not align)")
                
            total_value = virtual_cash + (shares_held * raw_price)
            print(f"    Current Node Balance -> Cash: ${virtual_cash:.2f} | Net Portfolio Assets: ${total_value:.2f}")

    except KeyboardInterrupt:
        print("\nShutting down Price Node safely...")

if __name__ == "__main__":
    asyncio.run(start_price_node())
