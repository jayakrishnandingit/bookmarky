#!/usr/bin/env groovy

pipeline {
    agent {
        dockerfile true
    }
    stages {
        stage('build') {
            steps {
                sh 'flake8 .'
                sh 'python3 manage.py makemigrations'
                sh 'python3 manage.py migrate'
                sh 'python3 manage.py test'
            }
        }
    }
}
