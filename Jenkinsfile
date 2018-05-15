#!/usr/bin/env groovy

pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                bat 'if not exist "env" py -m venv env'
                bat 'env\\Scripts\\activate'
                bat 'pip freeze'
                bat 'python -m pip install --upgrade pip'
            }
        }
    }
}
