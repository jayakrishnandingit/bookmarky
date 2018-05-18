#!/usr/bin/env groovy

pipeline {
    agent {
        dockerfile true
    }
    stages {
        stage('build') {
            steps {
                sh 'flake8 .'
                sh 'sudo docker-compose run web python3 manage.py makemigrations'
                sh 'sudo docker-compose run web python3 manage.py migrate'
                sh 'sudo docker-compose run web python3 manage.py test'
            }
        }
    }
}
