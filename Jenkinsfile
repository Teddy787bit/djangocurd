pipeline {
  agent any
  stages {
    stage('Test') {
      parallel {
        stage('Windwos Test') {
          steps {
            build 'job1'
          }
        }

        stage('Linux Test') {
          steps {
            build 'job1'
          }
        }

      }
    }

  }
}