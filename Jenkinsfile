pipeline { 
    environment { 
        registry = "clrosier/workout-api" 
        registryCredential = 'dockerhub' 
        dockerImage = '' 
    }
    agent {
        label "docker-agent"
    }
    stages { 
        stage('Checkout') { 
            steps { 
                git 'https://github.com/clrosier/workout-api.git' 
            }
        } 
        stage('Building Image') { 
           steps { 
                script { 
                    dockerImage = docker.build registry + ":0.0.$BUILD_NUMBER" 
                }
            } 
        }
        stage('Deploy Image') { 
            steps { 
                script { 
                    docker.withRegistry('', registryCredential) { 
                        dockerImage.push() 
                    }
                } 
            }
        } 
        stage('Clean Up') { 
            steps { 
                sh "docker rmi $registry:$BUILD_NUMBER" 
            }
        } 
    }
}

