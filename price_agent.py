import asyncio
import os

ALPHA_FILTER = 0.8
STARTING_CAPITAL = 50000.0
live_market_ticks = [150.20, 151.45, 152.10, 149.80, 148.50, 153.25, 154.10, 152.00]

async def start_price_node():
    print("[Price Agent Node] Powered Up. Ingesting market signals...")
    virtual_cash = STARTING_CAPITAL
    shares_held = 450  # Start with an aggressive position to test the Risk Officer's limits!
    ema_price = live_market_ticks[0]
    
    try:
        for i, raw_price in enumerate(live_market_ticks):
            await asyncio.sleep(2.5)
            ema_price = (ALPHA_FILTER * raw_price) + ((1 - ALPHA_FILTER) * ema_price)
            
            # Read News AI Agent Broadcast
            current_sentiment = 0.0  
            if os.path.exists("sentiment_stream.txt"):
                with open("sentiment_stream.txt", "r") as f:
                    try: current_sentiment = float(f.read().strip())
                    except ValueError: pass
            
            print(f"\n[Price Agent] Tick #{i+1} -> Price: ${raw_price:.2f} | Trend: ${ema_price:.2f} | Sentiment: {current_sentiment}")
            
            # Generate local strategy breakout trade signal
            if raw_price > ema_price and current_sentiment > 0.3:
                print("   --- Strategy triggered a BUY. Sending order to Risk Officer for review...")
                
                # Write a transaction request record to drop in the Risk pipe
                with open("order_request.txt", "w") as f:
                    f.write(f"BUY,{raw_price},{virtual_cash},{shares_held}")
                
                # Pause briefly to allow the Risk Agent to process the request
                await asyncio.sleep(0.6)
                
                # Check for the Risk Officer's verdict broadcast
                if os.path.exists("risk_verdict.txt"):
                    with open("risk_verdict.txt", "r") as f:
                        verdict, reason = f.read().strip().split(",")
                    os.remove("risk_verdict.txt")
                    
                    print(f"   --- Risk Response Received: [{verdict}] -> {reason}")
                    
                    if verdict == "APPROVED":
                        shares_to_buy = int(virtual_cash // raw_price)
                        shares_held += shares_to_buy
                        virtual_cash -= (shares_to_buy * raw_price)
                        print(f"    ORDER EXECUTED: Bought shares successfully.")
                    else:
                        print("    ORDER BLOCKED: The strategy was overridden by the Risk Officer.")
            else:
                print("   >>> STRATEGY ARCHITECTURE: SIGNAL HOLD")
                
            total_value = virtual_cash + (shares_held * raw_price)
            print(f"   [Ledger] Cash: ${virtual_cash:.2f} | Active Shares: {shares_held} | Total Net Assets: ${total_value:.2f}")

    except KeyboardInterrupt:
        print("\nShutting down Price Node safely...")

if __name__ == "__main__":
    asyncio.run(start_price_node())
