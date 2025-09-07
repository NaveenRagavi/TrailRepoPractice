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
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r Filpkart/requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    . venv/bin/activate
                    pytest Filpkart/tests/ --maxfail=1 --disable-warnings -q
                '''
            }
        }
    }

    post {
        always {
            junit '**/test-results/*.xml'  // if you later add XML reporting
        }
    }
}
