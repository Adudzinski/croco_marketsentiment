from openai import OpenAI
from dotenv import load_dotenv
from pathlib import Path
import os
import random

# Load .env from root folder
env_path = Path(__file__).resolve().parent.parent / '.env'
load_dotenv(dotenv_path=env_path)

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

MOCK_RESPONSES = ["POSITIVE", "NEGATIVE", "NEUTRAL"]

def analyze_sentiment(headlines, config):
    model = config["llm"].get("model", "gpt-3.5-turbo")
    mock_mode = config["llm"].get("mock", False)
    results = []

    for item in headlines:
        if mock_mode:
            sentiment = random.choice(MOCK_RESPONSES)
        else:
            prompt = f"""
Classify the sentiment of the following news headline as POSITIVE, NEGATIVE, or NEUTRAL regarding the company '{config['company']['name']}'.

Headline: "{item['headline']}"

Answer only with: POSITIVE / NEGATIVE / NEUTRAL
"""
            try:
                response = client.chat.completions.create(
                    model=model,
                    messages=[{"role": "user", "content": prompt}],
                    temperature=0
                )
                sentiment = response.choices[0].message.content.strip().upper()
            except Exception as e:
                sentiment = "ERROR"
                print(f"LLM error: {e}")

        results.append({**item, "sentiment": sentiment})
    
    return results


