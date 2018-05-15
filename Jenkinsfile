#!/usr/bin/env groovy

pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                if not exist "env" py -m venv env
                env\Scripts\activate
                pip freeze
                pip install -r ./requirements.txt
                pip freeze
            }
        }
    }
}
