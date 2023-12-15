pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        
	stage('Install Dependencies') {
            steps {
                script {
                    // Create and activate virtual environment
                    sh 'python3 -m venv venv'
                    sh 'source venv/bin/activate'

                    // Install dependencies
                    sh 'pip3 install PyPDF2'
                }
            }
        }


	stage('Run Tests') {
            steps {
                script {
                    // Run your Python program with automated input
                    sh 'chmod +x meal_plan_generator.py'

                    sh 'echo 2500 | ./meal_plan_generator.py'
                }
            }
        }

    }
}
