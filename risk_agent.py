import asyncio
import os

# STRICT RISK PARAMETERS
MAX_CAPITAL_PER_TRADE_PERCENT = 0.20  # Risk Officer only allows investing 20% of cash at a time
MAX_POSITION_LIMIT = 500              # Maximum total shares the system is allowed to hold

async def start_risk_node():
    print("[Risk Officer Node] Powered Up. Monitoring transaction validation pipes...")
    
    try:
        while True:
            await asyncio.sleep(0.5)  # Constantly listen for order validation requests
            
            # Look for an incoming request file dropped by the price agent
            if os.path.exists("order_request.txt"):
                with open("order_request.txt", "r") as f:
                    data = f.read().strip().split(",")
                    if len(data) < 4:
                        continue
                    
                    action, order_price, current_cash, current_shares = data[0], float(data[1]), float(data[2]), int(data[3])
                
                # Clean the order file immediately so we don't process it twice
                os.remove("order_request.txt")
                
                print(f"\n[Risk Audit] Intercepted {action} Request | Price: ${order_price:.2f} | Current Shares: {current_shares}")
                
                # --- RISK RULES MATRIX (IF-ELSE ENFORCEMENT) ---
                approved = True
                reason = "All risk parameters cleared successfully."
                
                if action == "BUY":
                    proposed_cost = order_price  # Cost of 1 share for basic testing
                    max_allowed_spending = current_cash * MAX_CAPITAL_PER_TRADE_PERCENT
                    
                    # Rule A: Position Cap Check
                    if current_shares >= MAX_POSITION_LIMIT:
                        approved = False
                        reason = f"REJECTED: Holding limit of {MAX_POSITION_LIMIT} shares reached."
                    
                    # Rule B: Capital Risk Concentration Check
                    elif proposed_cost > max_allowed_spending:
                        approved = False
                        reason = f"REJECTED: Order cost exceeds the max 20% capital limit (${max_allowed_spending:.2f})."
                
                # Broadcast the verdict out to the system channel
                verdict = "APPROVED" if approved else "DENIED"
                print(f"[Risk Verdict] Status: {verdict} | Reason: {reason}")
                
                with open("risk_verdict.txt", "w") as f:
                    f.write(f"{verdict},{reason}")
                    
    except KeyboardInterrupt:
        print("\nShutting down Risk Officer Node safely...")

if __name__ == "__main__":
    asyncio.run(start_risk_node())
