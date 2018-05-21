pipeline {
    agent {
        dockerfile true
    }
    stages {
        stage('build') {
            steps {
                sh "flake8 ."
                sh "ls -l /usr/local/bin/"
                sh "docker-compose run web python3 manage.py test -k"
            }
        }
    }
}
