#!/usr/bin/env groovy

pipeline {
    agent {
        dockerfile true
    }
    environment {
        PATH = "${env.PATH}:/usr/local/bin/docker-compose;"
    }
    stages {
        stage('build') {
            steps {
                sh "flake8 ."
                sh "docker-compose run web python3 manage.py test -k"
            }
        }
    }
}
