#!/usr/bin/env groovy

pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                if [ ! -d "env" ] ; then
                    py -m venv env
                fi
                env\Scripts\activate
                pip install -r ./requirements.txt
                pip freeze
            }
        }
    }
}
