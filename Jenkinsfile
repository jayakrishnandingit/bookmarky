#!/usr/bin/env groovy

pipeline {
    agent {
        dockerfile true
    }
    stages {
        stage('install_docker_compose') {
            steps {
                sh "pip install docker-compose"
            }
        }
        stage('build') {
            steps {
                sh "flake8 ."
                sh "ls -l /usr/local/bin/"
            }
        }
    }
}
