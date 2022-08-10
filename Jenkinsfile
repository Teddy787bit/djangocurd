pipeline {
  agent any
  stages {
    stage('One') {
      parallel {
        stage('One') {
          steps {
            build 'job1'
          }
        }

        stage('Two') {
          steps {
            build 'job2'
          }
        }

      }
    }

  }
}