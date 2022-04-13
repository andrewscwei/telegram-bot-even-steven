# Telegram Bot: Even Steven [![CI](https://github.com/andrewscwei/telegram-bot-even-steven/workflows/CI/badge.svg)](https://github.com/andrewscwei/telegram-bot-even-steven/actions/workflows/ci.yml) [![CD](https://github.com/andrewscwei/telegram-bot-even-steven/workflows/CD/badge.svg)](https://github.com/andrewscwei/telegram-bot-even-steven/actions/workflows/cd.yml)

A simple Telegram bot for splitting expenses within a group.

This is a webhook-based Telegram bot powered by [Flask](https://flask.palletsprojects.com) and [`python-telegram-bot`](https://github.com/python-telegram-bot/python-telegram-bot), and deployed to [Heroku Container Registry](https://www.heroku.com/deploy-with-docker).

## Usage

### Prerequisites

This project assumes the following are already installed in your local machine:
- [`pyenv`](https://github.com/pyenv/pyenv): To easily switch between Python versions
- [`pipenv`](https://pipenv.pypa.io/en/latest/): To manage `pip` dependencies and virtual environments
- [`ngrok`](https://ngrok.com/download): Optional, but required in order to test the bot locally from Telegram

### Environment

Prepare `.env` file containing minimum environment variables for the bot:

```sh
# .env

TELEGRAM_BOT_TOKEN="<token>"
```

### Development

To run the bot locally with file watching and live reload:

```sh
# Install Python version specified in .python-version
$ pyenv install -s

# Install production and dev dependencies
$ pipenv install -d

# Run the app locally on 8080
$ make dev
```

### Production

To run the bot locally in production mode:

```sh
# Build the Docker image
$ make build

# Run the Docker image
$ make run
```

### Unit Tests

```sh
# Running unit tests locally
$ pipenv run pytest

# Running unit tests against Docker image
$ make test
```

### Testing Local Bot on Telegram

First, run [`ngrok`](https://ngrok.com/download) to expose the bot to the public, make note of the public URL:

```sh
$ ngrok http 8080
```

Next, set the webhook URL of the bot to the public URL generated by `ngrok`:

```sh
$ curl https://api.telegram.org/bot<bot_token>/setWebhook?url=<ngrok_url>
```

You should now be able to communicate directly with your local bot from Telegram.
