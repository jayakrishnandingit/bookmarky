#!/usr/bin/env groovy

pipeline {
    agent {
        dockerfile true
    }
    stages {
        stage('build') {
            steps {
                sh 'flake8 .'
                sh '/usr/local/bin/docker-compose run web python3 manage.py makemigrations'
                sh '/usr/local/bin/docker-compose run web python3 manage.py migrate'
                sh '/usr/local/bin/docker-compose run web python3 manage.py test'
            }
        }
    }
}
