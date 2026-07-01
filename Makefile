.PHONY: install test run docker-build docker-run helm-template

install:
	pip install -r requirements-dev.txt

test:
	pytest -v

run:
	uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

docker-build:
	docker build -t banking-devsecops-api:latest .

docker-run:
	docker run -p 8000:8000 banking-devsecops-api:latest

helm-template:
	helm template banking-devsecops ./helm/banking-devsecops
