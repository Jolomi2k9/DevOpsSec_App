def registry = 'https://volun2k9.jfrog.io/'
def imageName = 'volun2k9.jfrog.io/vol2k9-docker-local/volun2k9app'
def version   = '0.1.0'
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

        stage('Build Wheel') {
            steps {
                script {
                    echo '<--------------- Wheel Build Start --------------->'
                    sh '''#!/bin/bash
                    source venv/bin/activate
                    pip install wheel
                    python setup.py bdist_wheel
                    '''
                    echo '<--------------- Wheel Build Complete --------------->'
                }
            }
        } 

        stage("Flask app Publish") {
            steps {
                script {
                    echo '<--------------- Flask app Publish Start --------------->'
                    def server = Artifactory.newServer(url: registry + "/artifactory", credentialsId: "artifact-cred")
                    def properties = "buildid=\${env.BUILD_ID};commitid=\${GIT_COMMIT}"
                    def uploadSpec = """{
                        "files": [
                            {
                            "pattern": "dist/*.whl",
                            "target": "vol-pypi-local/",
                            "flat": "true",
                            "props" : "${properties}"
                            }
                        ]
                    }"""
                    def buildInfo = server.upload(uploadSpec)
                    buildInfo.env.collect()
                    server.publishBuildInfo(buildInfo)
                    echo '<--------------- Flask app Publish Ends --------------->'  
                }
            }   
        }

        
        stage(" Docker Build ") {
            steps {
                script {
                echo '<--------------- Docker Build Started --------------->'
                app = docker.build(imageName+":"+version)
                echo '<--------------- Docker Build Ends --------------->'
                }
            }
        }

        stage (" Docker Publish "){
            steps {
                script {
                echo '<--------------- Docker Publish Started --------------->'  
                    docker.withRegistry(registry, 'artifact-cred'){
                        app.push()
                    }    
                echo '<--------------- Docker Publish Ended --------------->'  
                }
            }
        }

        stage("Deploy") {
            steps {                
                script {                  
                    sh '''#!/bin/bash
                    ./deploy.sh
                '''                  
                }                                
            }
        }    
    }
}
