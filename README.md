# Rogue Traveler

A smart travel agent application built with Streamlit that helps users plan their trips based on their preferences, budget, and dates.

## Features

- Input origin city, budget, and travel dates
- AI-powered travel recommendations
- Interactive user interface
- Budget-friendly travel planning

## Setup

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Set up Streamlit secrets:
   - For local development, go to `.streamlit/secrets.toml` file in your project root to modify the Key:
     ```toml
     OPENAI_API_KEY = "your_api_key_here"
     ```
   - For Streamlit Cloud deployment, add the secret in the dashboard under "Secrets"

4. Run the application:
   ```bash
   streamlit run home.py
   ```

## Requirements

- Python 3.8+
- OpenAI API key, Google Custon Search key, Google Custom Search engine
- Internet connection

### keys.py

create a file called keys.py
google_search_key = '<>'
google_engine = '<>>'
open_api_key = '<>'
