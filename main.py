from src.config_loader import load_config
from src.fetch_news import fetch_headlines
from src.llm_sentiment import analyze_sentiment

def main():
    config = load_config("config.yaml")
    headlines = fetch_headlines(config)
    results = analyze_sentiment(headlines, config)
    positive = 0
    negative = 0
    neutral = 0
    for r in results:
        print(f"[{r['sentiment'].upper()}] {r['headline']}")
        if r['sentiment'].upper() == 'POSITIVE':
            positive += 1
        if r['sentiment'].upper() == 'NEGATIVE':
            negative += 1
        if r['sentiment'].upper() == 'NEUTRAL':
            neutral += 1 

    print(f' POSITIVE = {positive}-times \n NEUTRAL = {neutral}-times \n NEGATIVE = {negative}-times ')

if __name__ == "__main__":
    main()

