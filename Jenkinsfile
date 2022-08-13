pipeline {
  agent any
  stages {
    stage('Build') {
      steps{
          echo "Testing"
      }
    
    }
    stage('DeploymentToDev') {
      when {
        branch 'dev'
      }
      steps{
          echo "This is the Dev Branch"
      }
    
    }
  }
}