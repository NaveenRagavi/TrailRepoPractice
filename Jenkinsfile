pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/NaveenRagavi/TrailRepoPractice.git'
            }
        }

        stage('Set up Python') {
            steps {
                bat '''
                    python -m venv venv
                    call venv\\Scripts\\activate
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                bat '''
                    call venv\\Scripts\\activate
                    pytest --junitxml=results.xml
                '''
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished (success or failure)'
            junit 'results.xml'   // publish test report if it exists
        }
        success {
            echo '✅ Job succeeded!'
        }
        failure {
            echo '❌ Job failed!'
        }
        unstable {
            echo '⚠️ Job unstable (some tests failed).'
        }
        changed {
            echo '🔄 Build result changed from last run!'
        }
    }
}
