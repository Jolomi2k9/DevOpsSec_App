pipeline {
    agent {
        node {
            label 'host-server'
        }
    }

    stages {
        
        // stage("Setup python env") {
        //     steps {
        //         echo "Setting up Python virtual environment"
        //         sh '''
        //         python3 -m venv venv
        //         source venv/bin/activate
        //         '''
        //     }
        // }

        // stage("Install Dependencies") {
        //     steps {
        //         echo "Installing dependencies"
        //         sh 'pip install -r requirements.txt'
        //     }
        // }


        stage("Test") {
            steps {
                echo "Running tests"
                // Add your Python test commands here
            }
        }

        stage('SonarQube analysis') {
            environment{
             scannerHome = tool 'vol-sonar-scanner'
            }
            steps{
            withSonarQubeEnv('vol-sonarqube-server') { 
            sh "${scannerHome}/bin/sonar-scanner"
            }
            }
        }        

    //     stage("Deploy") {
    //         steps {
    //             echo "Deploying Flask application"
    //             sh '''
    //             source venv/bin/activate
    //             flask run --host=0.0.0.0
    //             '''                
    //         }
    //     }
    // }
}
