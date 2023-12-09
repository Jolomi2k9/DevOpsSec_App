pipeline {
    agent {
        node {
            label 'host-server'
        }
    }

    stages {
        
        stage("Setup python env") {
            steps {
                echo "Setting up Python virtual environment"
                sh '''#!/bin/bash
                python3 -m venv venv
                source venv/bin/activate
                '''
            }
        }

        stage("Install Dependencies") {
            steps {
                echo "Installing dependencies"
                sh '''#!/bin/bash
                source venv/bin/activate
                pip install -r requirements.txt
                '''                
            }
        }        

        // stage('SonarQube analysis') {
        //     environment{
        //      scannerHome = tool 'vol-sonar-scanner'             
        //     }
        //     steps{
        //     withSonarQubeEnv('vol-sonarqube-server') {
        //         sh '''#!/bin/bash
        //             source venv/bin/activate
        //             ${scannerHome}/bin/sonar-scanner
        //             '''        
        //     }
        //     }            
        // }  

        // stage("Quality Gate"){
        //     steps{
        //         script{
        //             timeout(time: 1, unit: 'HOURS') { 
        //                 def qg = waitForQualityGate() 
        //                 if (qg.status != 'OK') {
        //                 error "Pipeline aborted due to quality gate failure: ${qg.status}"
        //                 }
        //             }
        //         }   
        //     }
        // }

        stage("Deploy") {
            steps {
                echo "Deploying Flask application"
                sh '''#!/bin/bash
                source venv/bin/activate
                # Run Gunicorn server with flask app
                gunicorn --bind 0.0.0.0:5000 main:app               
                '''                                
            }
        }    
    }
}
