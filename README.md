# Banking DevSecOps CI/CD Platform

A production-style DevOps portfolio project that demonstrates how a banking payment microservice can be containerized, tested, scanned, and deployed using CI/CD, Docker, Kubernetes, Helm, Terraform, and monitoring.

> This project is designed from a DevOps / Cloud Platform Engineering perspective. The application is a lightweight mock banking API for UPI, NEFT, RTGS, and NPCI-style transaction validation workflows.

## Why this project?

This repository shows practical skills required for product-based DevOps roles:

- CI/CD pipeline design with Jenkins and GitHub Actions
- Docker image build and container security scanning
- Kubernetes deployment using manifests and Helm charts
- Infrastructure provisioning for AWS ECR using Terraform
- API health checks, readiness checks, and Prometheus metrics
- DevSecOps practices using unit tests, dependency scan, and image scan
- Banking domain context: UPI, NEFT, RTGS, transaction validation, payment status tracking

## Tech Stack

| Area | Tools / Technologies |
|---|---|
| Application | Python, FastAPI |
| CI/CD | Jenkins, GitHub Actions |
| Containerization | Docker, Docker Compose |
| Orchestration | Kubernetes, Helm |
| IaC | Terraform |
| Security | Bandit, pip-audit, Trivy-ready workflow |
| Monitoring | Prometheus metrics endpoint |
| Domain | Banking payments, UPI, NEFT, RTGS, NPCI-style flow |

## Architecture

```text
Developer Push
    ↓
GitHub Actions / Jenkins
    ↓
Unit Test + Security Scan + Docker Build
    ↓
Container Registry / AWS ECR
    ↓
Kubernetes Deployment / Helm Release
    ↓
FastAPI Banking Payment Service
    ↓
Health Check + Metrics + Logs
```

## API Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/health` | Application health check |
| GET | `/ready` | Readiness check |
| GET | `/metrics` | Prometheus-compatible metrics |
| POST | `/api/v1/payments/upi` | Create mock UPI payment |
| POST | `/api/v1/payments/neft` | Create mock NEFT payment |
| POST | `/api/v1/payments/rtgs` | Create mock RTGS payment |
| GET | `/api/v1/transactions/{transaction_id}` | Check transaction status |

## Run Locally

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Open:

```text
http://localhost:8000/docs
http://localhost:8000/health
http://localhost:8000/metrics
```

## Run with Docker

```bash
docker build -t banking-devsecops-api:latest .
docker run -p 8000:8000 banking-devsecops-api:latest
```

Or:

```bash
docker-compose up --build
```

## Run Tests

```bash
pip install -r requirements-dev.txt
pytest -v
```

## Kubernetes Deployment

```bash
kubectl apply -f k8s/namespace.yaml
kubectl apply -f k8s/configmap.yaml
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
kubectl apply -f k8s/hpa.yaml
```

## Helm Deployment

```bash
helm upgrade --install banking-devsecops ./helm/banking-devsecops -n banking-devsecops --create-namespace
```

## Terraform AWS ECR

```bash
cd terraform/aws-ecr
terraform init
terraform plan
terraform apply
```

## Resume Project Description

**Banking DevSecOps CI/CD Platform**  
Built a DevOps project for a banking payment microservice supporting mock UPI, NEFT, RTGS, and NPCI-style transaction workflows. Implemented CI/CD pipelines, Docker containerization, Kubernetes manifests, Helm chart, Terraform-based AWS ECR provisioning, automated testing, security scanning, and Prometheus-compatible monitoring endpoints.

## Resume Bullets

- Built a FastAPI-based mock banking payment service for UPI, NEFT, RTGS, and transaction status workflows.
- Implemented CI/CD automation using Jenkins and GitHub Actions for test execution, security checks, Docker image build, and deployment workflow.
- Created Dockerfile, Docker Compose, Kubernetes manifests, and Helm chart for containerized microservice deployment.
- Added Terraform configuration for AWS ECR provisioning and container image management.
- Designed health, readiness, and Prometheus metrics endpoints to demonstrate observability and production-readiness.

## Author

Satyam Raut  
DevOps | Cloud Platform | CI/CD | Kubernetes | Banking Domain
