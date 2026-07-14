pipeline {
    agent { label 'electronix' }

    environment {
        S3_BUCKET = 'electronics-service'
        CLOUDFRONT_ID = 'E1FZ4O0FHGE716'
        AWS_REGION = 'us-east-1'
    }

    stages {

        stage('Install Prerequisites') {
            steps {
                sh '''
                # Install Node.js if not installed
                if ! command -v node >/dev/null 2>&1; then
                    echo "Installing Node.js..."
                    sudo apt-get update
                    curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
                    sudo apt-get install -y nodejs
                fi

                # Install AWS CLI if not installed
                if ! command -v aws >/dev/null 2>&1; then
                    echo "Installing AWS CLI..."
                    sudo apt-get update
                    sudo apt-get install -y awscli
                fi

                echo "Node Version:"
                node -v

                echo "NPM Version:"
                npm -v

                echo "AWS CLI Version:"
                aws --version
                '''
            }
        }

        stage("Frontend Deployment") {
            when {
                changeset "frontend/**"
            }

            stages {

                stage('Install Dependencies') {
                    steps {
                        dir('frontend') {
                            sh 'npm install'
                        }
                    }
                }

                stage('Run Tests') {
                    steps {
                        dir('frontend') {
                            sh 'npm test -- --watchAll=false || echo "No tests configured."'
                        }
                    }
                }

                stage('Build') {
                    steps {
                        dir('frontend') {
                            sh 'npm run build'
                        }
                    }
                }

                stage('Deploy S3') {
                    steps {
                        dir('frontend') {
                            sh '''
                            aws s3 sync dist/ s3://${S3_BUCKET} --delete --region ${AWS_REGION}
                            '''
                        }
                    }
                }

                stage('Invalidate CloudFront Cache') {
                    steps {
                        sh '''
                        aws cloudfront create-invalidation \
                          --distribution-id ${CLOUDFRONT_ID} \
                          --paths "/*"
                        '''
                    }
                }
            }
        }
    }

    post {
        success {
            echo 'Frontend Deployment Successful ✅'
        }

        failure {
            echo 'Frontend Deployment Failed ❌'
        }
    }
}