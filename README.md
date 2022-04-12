# Telegram Bot: Even Steven [![CI](https://github.com/andrewscwei/telegram-bot-even-steven/workflows/CI/badge.svg?branch=master)](https://github.com/andrewscwei/telegram-bot-even-steven/actions/workflows/cd.yml?query=branch%3Amaster)

## Setup

Ensure that you have the intended Python version installed for this project, i.e. by using `pyenv`:

```sh
$ brew install pyenv
$ pyenv install -s

# Verify correct version is being used
$ python --version
```

## Usage

### Local Development

To begin developing locally, you need to first prepare a `.env` file containing minimum environment variables for this project:

```sh
# .env

FLASK_DEBUG="1"
TELEGRAM_BOT_TOKEN="<token>"
```

```sh
# Install production and dev dependencies
$ pipenv install -d

# Activate the virtual environment
$ pipenv shell

# Run the app locally on 8080
$ make dev
```

### Running in Docker

```sh
# Build the Docker image
$ make

# Run the Docker image
$ make run
```
