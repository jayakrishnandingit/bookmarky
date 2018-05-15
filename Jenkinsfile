#!/usr/bin/env groovy

pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                bat 'if not exist "env" py -m venv env'
                bat 'env/Scripts/activate'
                bat 'pip freeze'
                bat 'pip install -r requirements.txt'
                bat 'pip freeze'
            }
        }
    }
}
