pipeline {
    agent any

    environment {
        IMAGE_NAME = 'banking-devsecops-api'
        IMAGE_TAG = "${BUILD_NUMBER}"
        REGISTRY = 'replace-with-your-ecr-or-dockerhub-registry'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'python -m pip install --upgrade pip'
                sh 'pip install -r requirements-dev.txt'
            }
        }

        stage('Lint and Security Scan') {
            steps {
                sh 'ruff check app tests || true'
                sh 'bandit -r app || true'
                sh 'pip-audit || true'
            }
        }

        stage('Unit Tests') {
            steps {
                sh 'pytest -v'
            }
        }

        stage('Docker Build') {
            steps {
                sh 'docker build -t ${IMAGE_NAME}:${IMAGE_TAG} .'
            }
        }

        stage('Container Scan') {
            steps {
                sh 'trivy image ${IMAGE_NAME}:${IMAGE_TAG} || true'
            }
        }

        stage('Push Image') {
            when { expression { return env.REGISTRY != 'replace-with-your-ecr-or-dockerhub-registry' } }
            steps {
                sh 'docker tag ${IMAGE_NAME}:${IMAGE_TAG} ${REGISTRY}/${IMAGE_NAME}:${IMAGE_TAG}'
                sh 'docker push ${REGISTRY}/${IMAGE_NAME}:${IMAGE_TAG}'
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh 'echo "Deploy using Helm or kubectl after updating image registry and cluster context"'
                sh 'helm upgrade --install banking-devsecops ./helm/banking-devsecops -n banking-devsecops --create-namespace || true'
            }
        }
    }

    post {
        always {
            echo 'Pipeline completed. Check test, scan, build, and deployment logs.'
        }
    }
}
