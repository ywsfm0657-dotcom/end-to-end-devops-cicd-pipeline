pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps { checkout scm }
        }
        stage('Test') {
            steps {
                sh '''
                    python3 -m venv .venv
                    . .venv/bin/activate
                    pip install -r app/requirements.txt
                    cd app
                    python -m unittest -v
                '''
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t devops-demo-app:${BUILD_NUMBER} .'
            }
        }
        stage('Run Container Smoke Test') {
            steps {
                sh '''
                    set +e
                    docker rm -f devops-demo-smoke >/dev/null 2>&1
                    set -e
                    docker run -d --name devops-demo-smoke -p 5001:5000 devops-demo-app:${BUILD_NUMBER}
                    sleep 5
                    curl --fail http://127.0.0.1:5001/health
                    docker rm -f devops-demo-smoke
                '''
            }
        }
    }
    post {
        always {
            sh 'docker ps -a --filter name=devops-demo-smoke || true'
        }
    }
}
