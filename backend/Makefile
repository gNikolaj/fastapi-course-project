include .env
export

run:
	python -m app.main

test:
	pytest

docker-build:
	docker build -t fastapi-app .

docker-run:
	docker run -p 8000:8000 fastapi-app