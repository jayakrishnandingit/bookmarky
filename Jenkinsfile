#!/usr/bin/env groovy

pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                bat 'if not exist "env" py -m venv env'
                bat 'cd .\\env'
                bat 'dir'
                bat 'cd'
                bat 'cd ..'
                bat 'pip freeze'
            }
        }
    }
}
