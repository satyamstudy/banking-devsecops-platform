# Architecture

This project represents a banking payment API delivered through a DevSecOps pipeline.

## Flow

1. Developer commits code to GitHub.
2. GitHub Actions or Jenkins runs linting, security checks, and unit tests.
3. Docker image is built and scanned.
4. Image can be pushed to AWS ECR.
5. Kubernetes or Helm deploys the application.
6. Health, readiness, and metrics endpoints support production observability.

## Banking Domain Context

The API simulates payment flows commonly seen in Indian banking platforms:

- UPI payment initiation
- NEFT payment initiation
- RTGS payment initiation
- Transaction status lookup
- NPCI-style transaction validation concept

## DevOps Focus

This project is not intended to be a complete banking product. It is a DevOps project that demonstrates how a microservice in a regulated domain can be packaged, scanned, deployed, monitored, and maintained.
