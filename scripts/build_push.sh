#!/usr/bin/env bash
set -euo pipefail

IMAGE_NAME=${IMAGE_NAME:-banking-devsecops-api}
IMAGE_TAG=${IMAGE_TAG:-local}
REGISTRY=${REGISTRY:-}

docker build -t "${IMAGE_NAME}:${IMAGE_TAG}" .

if [[ -n "${REGISTRY}" ]]; then
  docker tag "${IMAGE_NAME}:${IMAGE_TAG}" "${REGISTRY}/${IMAGE_NAME}:${IMAGE_TAG}"
  docker push "${REGISTRY}/${IMAGE_NAME}:${IMAGE_TAG}"
fi
