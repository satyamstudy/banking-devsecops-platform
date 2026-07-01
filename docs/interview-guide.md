# Interview Explanation

## How to explain this project

I built this project to demonstrate DevOps practices in a banking domain scenario. The application is a mock payment service for UPI, NEFT, RTGS and transaction status workflows. My main focus was CI/CD, Dockerization, Kubernetes deployment, Helm packaging, Terraform-based ECR provisioning, automated testing, security scanning and monitoring.

## Why FastAPI?

FastAPI is lightweight and useful for building REST APIs quickly. In this project it helps represent a real microservice that can be containerized and deployed through a DevOps pipeline.

## Why Kubernetes and Helm?

Kubernetes handles deployment, scaling, service discovery and health checks. Helm helps template Kubernetes resources and makes deployments easier across environments.

## Why Terraform?

Terraform is used to provision cloud infrastructure such as AWS ECR. It keeps infrastructure repeatable and version-controlled.

## What is DevSecOps here?

The pipeline includes testing, dependency security checks, code scanning and container image scanning before deployment. This helps catch issues earlier in the CI/CD lifecycle.
