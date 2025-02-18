pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                script {
                    sh 'pip install -r requirements.txt'
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    sh 'pytest tests/'
                }
            }
        }
        stage('Docker Build') {
            steps {
                script {
                    sh 'docker build -t market-demand-prediction .'
                }
            }
        }
        stage('Deploy to Kubernetes') {
            steps {
                script {
                    sh 'kubectl apply -f k8s/deployment.yaml'
                }
            }
        }
    }
} 