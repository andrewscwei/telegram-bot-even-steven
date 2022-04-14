.PHONY: all clean dev test build run

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
name = $(shell basename ${PWD})
tag = latest

all: help

help:
	@echo
	@echo "Usage: "$(COLOR_BLUE)"make "$(COLOR_CYAN)"<command>"$(COLOR_RESET)
	@echo
	@echo "  where "$(COLOR_CYAN)"<command>"$(COLOR_RESET)" is one of:"
	@echo $(COLOR_CYAN)"    clean"$(COLOR_RESET)" - Removes all built Docker images related to this app ("$(COLOR_CYAN)"$(name):*"$(COLOR_RESET)")"
	@echo $(COLOR_CYAN)"      dev"$(COLOR_RESET)" - Builds and runs the app in developpment mode ("$(COLOR_CYAN)"$(name):dev"$(COLOR_RESET)")"
	@echo $(COLOR_CYAN)"     test"$(COLOR_RESET)" - Builds and runs tests on the Docker image ("$(COLOR_CYAN)"$(name):test"$(COLOR_RESET)")"
	@echo $(COLOR_CYAN)"    build"$(COLOR_RESET)" - Builds the production Docker image ("$(COLOR_CYAN)"$(name):latest"$(COLOR_RESET)")"
	@echo $(COLOR_CYAN)"      run"$(COLOR_RESET)" - Runs the production Docker image ("$(COLOR_CYAN)"$(name):latest"$(COLOR_RESET)")"
	@echo

clean:
	@IMAGES=$$(docker images | awk '$$1 ~ /^'$$(echo $(name) | sed -e "s/\//\\\\\//g")'$$/ {print $$3}') && if [ "$${IMAGES}" != "" ]; then docker rmi -f $${IMAGES}; fi
	@docker system prune -f

dev: tag = dev
dev:
	@docker build --build-arg BUILD_NUMBER=$(build) --target dev -t $(name):$(tag) .
	@IMAGE_NAME=$(name) IMAGE_TAG=$(tag) docker compose -f docker-compose.dev.yml up

test: tag = test
test:
	@docker build --build-arg BUILD_NUMBER=$(build) --target test -t $(name):$(tag) .
	@IMAGE_NAME=$(name) IMAGE_TAG=$(tag) docker compose run main pytest

build:
	@docker build --build-arg BUILD_NUMBER=$(build) --target release -t $(name):$(tag) .

run:
	@IMAGE_NAME=$(name) IMAGE_TAG=$(tag) docker compose up
