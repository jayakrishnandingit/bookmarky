#!/usr/bin/env groovy

pipeline {
    agent { docker 'python:3.6.3' }
    stages {
        stage('build') {
            steps {
                bat 'echo "Hello World!"'
                bat 'py --version'
            }
        }
    }
}
