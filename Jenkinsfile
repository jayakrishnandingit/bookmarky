pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                sh "docker-compose run web flake8 ."
                sh "docker-compose run web python3 manage.py test -k"
            }
        }
    }
}
