.PHONY: help
help:
	@echo "+------------------+"
	@echo "| Makefile Targets |"
	@echo "+------------------+"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-12s\033[0m %s\n", $$1, $$2}'

.PHONY: build
build: ## Build docker image
	@echo ------------------
	@echo - Building image -
	@echo ------------------
	docker-compose build && docker image prune -f

.PHONY: up
up: ## Run a container in the foreground to stream logs
	@echo ----------------------------------------
	@echo - Starting app container in foreground -
	@echo ----------------------------------------
	docker-compose up

.PHONY: server
server: ## Run a container in the background
	@echo ----------------------------------------
	@echo - Starting app container in background -
	@echo ----------------------------------------
	docker-compose up -d

.PHONY: shell
shell: ## Open a bash shell on running container
	@echo ----------------------------
	@echo - Entering container shell -
	@echo ----------------------------
	docker-compose exec app bash

.PHONY: down
down: ## Stop and remove running container
	@echo -------------------------------------
	@echo - Stop and Remove running container -
	@echo -------------------------------------
	docker-compose down
