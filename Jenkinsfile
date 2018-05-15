#!/usr/bin/env groovy

pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                bat 'if not exist "env" py -m venv env'
                bat 'cd env'
                bat 'Scripts\\activate'
                bat 'cd ..'
                bat 'pip freeze'
            }
        }
    }
}
