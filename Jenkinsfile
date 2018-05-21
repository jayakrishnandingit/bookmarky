#!/usr/bin/env groovy

pipeline {
    agent {
        dockerfile true
    }
    environment {
        PATH=$PATH:/usr/local/bin/docker-compose;
    }
    stages {
        stage('build') {
            steps {
                sh 'flake8 .'
                sh 'echo env.PATH'
            }
        }
    }
}
