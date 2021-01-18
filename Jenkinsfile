pipeline {
    environment {
        registry = "clrosier/workout-api"
        registryCredential = "dockerhub"
    }
    node("docker-agent") {
        stages {
            stage('Build Image') {
                steps {
                    script {
                        docker.build registry + ":$BUILD_NUMBER"
                    }
                }
            }
        }
    }
}