pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                script {
                        checkout([$class: 'GitSCM', branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: '9bdbdb10-b9c9-4788-8447-187b76790749', url: 'https://github.com/shanvino85/PythonFrameWorkBDD.git']]])
                }
            }
        }
        stage('Allure Report') {
            steps {
                script {
                    sh 'allure serve reports'
                }
            }
        }
    }
}