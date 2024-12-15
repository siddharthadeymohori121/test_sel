pipeline {
    agent any
    stages {
        stage('Checkout Code') {
            steps {
                git 'https://github.com/<your-repo>/selenium-jenkins-demo.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'pip install selenium'
            }
        }
        stage('Run Tests') {
            steps {
                sh 'python test_login.py'
            }
        }
    }
}
