
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Checkout the code from your version control system (e.g., Git)
                checkout scm
            }
        }

        stage('Build and Push Docker Image') {
            steps {
                script {
                    // Define your Docker image name and tag
                    def dockerImage = 'areebaayazz/p1'
                    def dockerTag = 'latest'

                    // Build the Docker image
                    bat "docker build -t ${dockerImage}:${dockerTag} ."

                    // Log in to Docker Hub (make sure to set DOCKER_HUB_USERNAME and DOCKER_HUB_PASSWORD as Jenkins credentials)
                    withCredentials([usernamePassword(credentialsId: 'docker-hub-credentials-id', usernameVariable: 'DOCKER_HUB_USERNAME', passwordVariable: 'DOCKER_HUB_PASSWORD')]) {
                        bat "docker login -u areebaayazz -p city4242!"
                    }

                    // Push the Docker image to Docker Hub
                    bat "docker push ${dockerImage}:${dockerTag}"
                }
            }
        }
    }

    post {
        success {
            echo 'Docker image built and pushed successfully!'
        }
    }
}
