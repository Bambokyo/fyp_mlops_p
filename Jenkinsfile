   agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build and Push Docker Image') {
            steps {
                script {
                    $dockerImage = 'bilali20187/p1'
                    $dockerTag = 'latest'

                    // Build the Docker image
                    bat "docker build -t ${dockerImage}:${dockerTag} ."

                    // Log in to Docker Hub
                    sh 'docker login -u bilali201877 -p fast2011351'

                    // Push the Docker image to Docker Hub
                    sh "docker push ${dockerImage}:${dockerTag}"
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
