pipeline {
    agent {
        node {
            label 'host-server'
        }
    }

    stages {
        stage('Clone-code') {
            steps {
                git branch: 'main', url: 'https://github.com/Jolomi2k9/DevOpsSec_App.git'
            }
        }
    }
}