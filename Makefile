.PHONY: all clean dev build run

COLOR_PREFIX = "\\033["
COLOR_RESET = "$(COLOR_PREFIX)0m"
COLOR_BLACK = "$(COLOR_PREFIX)0;30m"
COLOR_RED = "$(COLOR_PREFIX)0;31m"
COLOR_GREEN = "$(COLOR_PREFIX)0;32m"
COLOR_YELLOW = "$(COLOR_PREFIX)0;33m"
COLOR_BLUE = "$(COLOR_PREFIX)0;34m"
COLOR_PURPLE = "$(COLOR_PREFIX)0;35m"
COLOR_CYAN = "$(COLOR_PREFIX)0;36m"
COLOR_LIGHT_GRAY = "$(COLOR_PREFIX)0;37m"

build = $(shell git rev-parse --short HEAD)
name = bot
tag = latest

all: help

help:
	@echo
	@echo "Usage: "$(COLOR_BLUE)"make "$(COLOR_CYAN)"<command> [name=<image_name>] [tag=<image_tag>] [build=<build_number>]"$(COLOR_RESET)
	@echo
	@echo "  where "$(COLOR_CYAN)"<command>"$(COLOR_RESET)" is one of:"
	@echo $(COLOR_CYAN)"    clean"$(COLOR_RESET)" - Removes all built Docker images related to this app"
	@echo $(COLOR_CYAN)"      dev"$(COLOR_RESET)" - Runs the app in developpment mode"
	@echo $(COLOR_CYAN)"    build"$(COLOR_RESET)" - Builds the production Docker image"
	@echo $(COLOR_CYAN)"     test"$(COLOR_RESET)" - Builds and runs tests on the Docker image"
	@echo $(COLOR_CYAN)"      run"$(COLOR_RESET)" - Runs the production Docker image"
	@echo
	@echo "  where "$(COLOR_CYAN)"<image_name>"$(COLOR_YELLOW)"(optional)"$(COLOR_RESET)" is the target Docker image name (default: "$(COLOR_YELLOW)"$(name)"$(COLOR_RESET)")"
	@echo "  where "$(COLOR_CYAN)"<image_tag>"$(COLOR_YELLOW)"(optional)"$(COLOR_RESET)" is the target Docker image tag (default: "$(COLOR_YELLOW)"$(tag)"$(COLOR_RESET)")"
	@echo "  where "$(COLOR_CYAN)"<build_number>"$(COLOR_YELLOW)"(optional)"$(COLOR_RESET)" is the build name (default: "$(COLOR_YELLOW)"$(build)"$(COLOR_RESET)")"
	@echo

clean:
	@IMAGES=$$(docker images | awk '$$1 ~ /^'$$(echo $(name) | sed -e "s/\//\\\\\//g")'$$/ {print $$3}') && if [ "$${IMAGES}" != "" ]; then docker rmi -f $${IMAGES}; fi
	@docker system prune -f

dev:
	@FLASK_APP=main.py FLASK_ENV=development pipenv run dotenv run -- flask run --port 8080

test:
ifdef tag
	@docker build --target test -t $(name):$(tag) .
	@IMAGE_NAME=$(name) IMAGE_TAG=$(tag) docker compose -f docker-compose.yml run main pytest
else
	@docker build --target test -t $(name):test .
	@IMAGE_NAME=$(name) IMAGE_TAG=test docker compose -f docker-compose.yml run main pytest
endif

build:
	@docker build \
		--build-arg BUILD_NUMBER=$(build) \
		--target release \
		-t $(name):$(tag) \
		.

run:
ifdef tag
	@IMAGE_NAME=$(name) IMAGE_TAG=$(tag) docker compose -f docker-compose.yml up
else
	@IMAGE_NAME=$(name) IMAGE_TAG=latest docker compose -f docker-compose.yml up
endif
