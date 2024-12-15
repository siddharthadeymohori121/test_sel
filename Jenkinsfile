pipeline {
    agent any
    stages {
        stage('Clone Repository') {
            steps {
                // Clone the Git repository
                git url: 'https://github.com/siddharthadeymohori121/test_sel.git', branch: 'master'
            }
        }
        stage('Run Selenium Test') {
            steps {
                // Run the Python script
                bat 'python test_login.py'
            }
        }
    }
}
