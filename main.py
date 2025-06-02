from src.config_loader import load_config
from src.fetch_news import fetch_headlines
from src.llm_sentiment import analyze_sentiment

def main():
    config = load_config("config.yaml")
    headlines = fetch_headlines(config)
    results = analyze_sentiment(headlines, config)
    
    for r in results:
        print(f"[{r['sentiment'].upper()}] {r['headline']}")

if __name__ == "__main__":
    main()

