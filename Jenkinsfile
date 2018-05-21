#!/usr/bin/env groovy

pipeline {
    agent {
        dockerfile true
    }
    stages {
        stage('build') {
            steps {
                sh "flake8 ."
                sh "cd /usr/local/bin"
                sh "ls -l"
            }
        }
    }
}
