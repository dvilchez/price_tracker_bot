# My Telegram Bot

This is a Telegram bot that receives a code, checks an external service regularly, and sends a message to the user if a condition is met.

## Setup

1. Create a virtual environment and activate it:

```
python -m venv .env
source .env/bin/activate  # On Windows use `.env\Scripts\activate`
```

2. Install the dependencies:

```
pip install -r requirements.txt
```

3. Set up pre-commit hooks:

```
pre-commit install
```

4. Set your Telegram bot token as an environment variable:

```
export TELEGRAM_TOKEN=your_telegram_bot_token  # On Windows use `set TELEGRAM_TOKEN=your_telegram_bot_token`
```

5. Run the bot:

```
python bot.py
```

## Testing
To run the tests, use:

```
pytest
```
