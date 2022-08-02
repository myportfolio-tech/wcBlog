pipeline {
    agent any 
    stages {
        stage('Build') { 
            steps {
               echo "Building Dev"
            }
        }
        stage('Test') { 
            steps {
               echo "Testing Dev"
            }
        }
        stage('Deploy') { 
            steps {
               echo "Deploying Dev"
               echo "Here goes Kubernetes"
            }
        }
    }
}