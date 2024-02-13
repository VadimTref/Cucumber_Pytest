pipeline {
    agent {
      docker {
        image 'python:3'
        label 'my-build-agent'
      }
    }
    stages {
        stage('build') {
            steps {
              sh """
              python --version
              """
            }
        }
    }
}
