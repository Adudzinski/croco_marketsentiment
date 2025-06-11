# 📰 Headline Sentiment Analyzer

This project uses a **Large Language Model (LLM)** to analyze recent news headlines related to a specific company and estimate the **overall market sentiment** — _positive_, _negative_, or _neutral_.

It's designed to be lightweight, configurable, and extensible for anyone interested in finance, trading, or news-based sentiment analysis.

---

## 🔍 What It Does

- Fetches recent news headlines using the [NewsAPI](https://newsapi.org)
- Analyzes the sentiment of each headline with an LLM (e.g. OpenAI's GPT-3.5)
- Outputs a list of headlines with corresponding sentiment labels
- Optional: Run in mock mode to test the pipeline without using real API credits

---

## 📦 Project Structure

```
headline-sentiment-analyzer/
├── main.py
├── config.yaml
├── .env
├── data/
├── src/
│   ├── fetch_news.py
│   ├── llm_sentiment.py
│   ├── config_loader.py
│   └── utils.py
```

---

## ⚙️ How to Use

### 1. Clone the Repository

```bash
git clone https://github.com/adudzinski/croco_marketsentiment.git
cd headline-sentiment-analyzer
```

### 2. Set Up Your Environment

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file in the root directory with:

```env
OPENAI_API_KEY=your_openai_key
NEWSAPI_KEY=your_newsapi_key
```

### 3. Configure Settings

Edit `config.yaml`:

```yaml
company:
  name: "Albemarle"
  keywords:
    - "Albemarle"
    - "lithium"
    - "battery metals"

newsapi:
  language: "en"
  max_results: 25
  sort_by: "publishedAt"

llm:
  provider: "openai"
  model: "gpt-3.5-turbo"
  mock: true  # Set to false to use real OpenAI API
```

### 4. Run the Analyzer

```bash
python main.py
```

---

## 📤 Output

Example console output:

```
[POSITIVE] Albemarle expands lithium production amid global EV boom
[NEGATIVE] Lithium price crash raises concerns for battery sector
[NEUTRAL] Market analysts weigh in on battery metals demand
```

---

## ✅ Features

- Modular code with easy-to-edit configuration
- Environment-safe API usage with `.env`
- Mock mode for free testing
- Ready for future integration with stock price prediction or dashboards

---

## 🛡 License

This project is licensed under the MIT License.
