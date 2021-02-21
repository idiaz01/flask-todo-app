pipeline {
    agent any

    environment {
        DOCKER_IMAGE_NAME="idiaz01/flask-todo-app"
    }
    stages {
        stage('Execute Test') {
            steps {
                echo 'Here is where the tests will run.'
            }
        }
        
        stage('Build Docker Image'){
            when {
                branch 'master'
            }
            steps {
                script {
                    app = docker.build(DOCKER_IMAGE_NAME)
                }
            }
        }
        
        stage('Push Docker Image'){
            when {
                branch 'master'
            }
            steps {
                script {
                    docker.withRegistry('https://registry.hub.docker.com', 'login_dockerhub') {
                        app.push("${env.BUILD_NUMBER}")
                        app.push("latest")
                    }
                }
            }
        }
        
        stage('Deploy') {
            when {
                branch 'master'
            }
            
            steps {
                echo 'Deploying to production'
                echo '-----------------------'
            }
        }
    }
}
