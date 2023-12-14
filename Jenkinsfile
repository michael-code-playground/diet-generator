pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
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
