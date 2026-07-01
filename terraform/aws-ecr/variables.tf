variable "aws_region" {
  description = "AWS region for ECR repository"
  type        = string
  default     = "ap-south-1"
}

variable "repository_name" {
  description = "ECR repository name"
  type        = string
  default     = "banking-devsecops-api"
}

variable "environment" {
  description = "Environment tag"
  type        = string
  default     = "dev"
}
