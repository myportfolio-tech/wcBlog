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
    
    stage('DeploymentToProd') {
      when {
        branch 'main'
      }
      steps{
          input 'Check Dev environment. Does it look correct?'
          milestone(1)
          echo "This is the Main Branch"
      }
    
    }
  }
}