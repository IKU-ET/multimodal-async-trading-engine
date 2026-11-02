import asyncio
import random

# A mock pipeline simulating incoming live global financial headlines
incoming_news_stream = [
    "Tech giants announce massive new orders for hardware scaling infrastructure.",
    "Logistics delays impact components shipping across global shipping lines.",
    "Quarterly financial metrics beat analyst consensus targets by twelve percent.",
    "Market competitors launch aggressive alternative lower-cost processing units."
]

def analyze_text_sentiment(headline):
    headline_lower = headline.lower()
    if "launch" in headline_lower or "beat" in headline_lower or "massive" in headline_lower:
        return 0.85
    elif "delay" in headline_lower or "competitor" in headline_lower:
        return -0.70
    return 0.0

async def start_news_node():
    print(" [News Agent Node] Powered Up. Broadcasting text metrics...")
    index = 0
    
    try:
        while True:
            await asyncio.sleep(3.0)  # The Text Agent scans an article every 3 seconds
            current_headline = incoming_news_stream[index % len(incoming_news_stream)]
            index += 1
            
            # The AI scores the text
            vibe_score = analyze_text_sentiment(current_headline)
            print(f" [News Agent] Scraped Headline: '{current_headline[:40]}...' | Score Broadcast: {vibe_score}")
            
            #  BACKUP LOG STEP: We write the value to a localized tracking file 
            # This acts as our network channel so the other agent can read it!
            with open("sentiment_stream.txt", "w") as f:
                f.write(str(vibe_score))
                
    except KeyboardInterrupt:
        print("\nShutting down News Node safely...")

if __name__ == "__main__":
    asyncio.run(start_news_node())
