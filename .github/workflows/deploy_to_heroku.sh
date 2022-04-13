#!/bin/bash

# Required environment variables:
# - HEROKU_API_KEY: Heroku long-lived user authorization key

set -e

BASE_DIR=$(cd $(dirname $0); cd ../../; pwd -P)

# In order to log into the Heroku Container Registry, you need a long-lived user authorization key.
# To create one, run `heroku authorizations:create` and set the key to the environment variable
# `HEROKU_API_KEY`, which will be automatically picked up by the Heroku CLI.

heroku container:login
heroku container:push --arg BUILD_NUMBER=$(echo $GITHUB_SHA | head -c7) -a $HEROKU_APP_NAME web
heroku container:release -a $HEROKU_APP_NAME web

echo
echo "Successfuly deployed to Heroku"
