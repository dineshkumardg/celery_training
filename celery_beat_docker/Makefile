DATE = $(shell date +%Y-%m-%d_%H%M)

#include environment.secret

.PHONY: help

help: ## This help.
        @awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

.DEFAULT_GOAL := help

compose-pro:
	ln -sf docker-compose-pro.yml docker-compose.yml
	ls -lah docker-compose.yml
compose-dev:
	ln -sf docker-compose-dev.yml docker-compose.yml
	ls -lah docker-compose.yml

test1:  ## Run test1. Add one tasks and show results.
	docker-compose exec celeryworker python /app/test1.py

test2:  ## Run test2. Add 100 simple tasks.
	docker-compose exec celeryworker python /app/test2.py
