#!/usr/bin/env groovy

pipeline {
    agent { docker 'python:3.6.3' }
    stages {
        stage('build') {
            steps {
                sh 'echo "Hello World!"'
                sh 'python --version'
            }
        }
    }
}
