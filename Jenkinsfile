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
<<<<<<< HEAD
          input 'Check Dev environment. Does it look correct?'
          milestone(1)
=======
>>>>>>> 5553153324bcbc3b2f4e8bba107ccad5855d624f
          echo "This is the Main Branch"
      }
    
    }
  }
}