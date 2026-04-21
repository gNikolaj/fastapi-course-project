run:
	uvicorn main:app --reload

test:
	pytest

docker-build:
	docker build -t fastapi-app .

docker-run:
	docker run -p 8000:8000 fastapi-app