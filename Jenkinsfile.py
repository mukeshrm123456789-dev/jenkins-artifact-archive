pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/<your-username>/jenkins-artifact-archive.git'
            }
        }
        stage('Generate Report') {
            steps {
                bat 'python app.py'
            }
        }
        stage('Archive Report') {
            steps {
                archiveArtifacts artifacts: 'report.txt', fingerprint: true
            }
        }
    }
}
