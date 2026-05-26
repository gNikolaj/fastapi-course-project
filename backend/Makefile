include .env
export

run:
	python -m app.main

test:
	pytest

services-start:
	brew services start postgresql@17
	brew services start redis

services-stop:
	brew services stop postgresql@17
	brew services stop redis

docker-build:
	docker build -t fastapi-app .

docker-run:
	docker run -p 8000:8000 --env-file .env fastapi-app

docker-up:
	docker-compose up -d

docker-down:
	docker-compose down