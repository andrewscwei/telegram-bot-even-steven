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
tag =
port = 8080

all: build

help:
	@echo
	@echo "Usage: "$(COLOR_BLUE)"make "$(COLOR_CYAN)"<command> [name=<image_name>] [tag=<image_tag>] [build=<build_number]"$(COLOR_RESET)
	@echo
	@echo "  where "$(COLOR_CYAN)"<command>"$(COLOR_RESET)" is one of:"
	@echo $(COLOR_CYAN)"    clean"$(COLOR_RESET)" - Removes all local Docker images related to this app"
	@echo $(COLOR_CYAN)"      dev"$(COLOR_RESET)" - Runs the app locally"
	@echo $(COLOR_CYAN)"    build"$(COLOR_RESET)" - Builds the Docker image"
	@echo $(COLOR_CYAN)"      run"$(COLOR_RESET)" - Runs the Docker image"
	@echo
	@echo "  where "$(COLOR_CYAN)"<image_name>"$(COLOR_YELLOW)"(optional)"$(COLOR_RESET)" is the target Docker image name (defaults to "$(COLOR_YELLOW)"$(name)"$(COLOR_RESET)")"
	@echo "  where "$(COLOR_CYAN)"<image_tag>"$(COLOR_YELLOW)"(optional)"$(COLOR_RESET)" is the target Docker image tag (defaults to target name)"
	@echo "  where "$(COLOR_CYAN)"<build_number>"$(COLOR_YELLOW)"(optional)"$(COLOR_RESET)" is the build name (defaults to "$(COLOR_YELLOW)"current short SHA, i.e. $(build)"$(COLOR_RESET)")"
	@echo

clean:
	@IMAGES=$$(docker images | awk '$$1 ~ /^'$$(echo $(name) | sed -e "s/\//\\\\\//g")'$$/ {print $$3}') && if [ "$${IMAGES}" != "" ]; then docker rmi -f $${IMAGES}; fi
	@docker system prune -f

dev:
	@FLASK_APP=main.py FLASK_ENV=development pipenv run dotenv run -- flask run --port $(port)

build: tag = latest
build:
	@docker build \
		--build-arg BUILD_NUMBER=$(build) \
		-t $(name):$(tag) \
		.

run:
ifdef tag
	@IMAGE_NAME=$(name) IMAGE_TAG=$(tag) docker-compose -f docker-compose.yml up
else
	@IMAGE_NAME=$(name) IMAGE_TAG=latest docker-compose -f docker-compose.yml up
endif
