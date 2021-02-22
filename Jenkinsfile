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
            steps {
                script {
                    app = docker.build(DOCKER_IMAGE_NAME)
                }
            }
        }
         
        stage('Push Docker Image'){
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
            steps {
                echo 'Deploying to production'
                sshagent(credentials: ['prod_server']) {
                    sh 'ssh idiaz01@35.188.103.75 whoami; uptime;'
                }
            }
        }
    }
}
