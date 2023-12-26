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
                    

                    // Install dependencies
                    sh 'pip3 install PyPDF2==3.0.1'
                }
            }
        }


	stage('Execute the script') {
            steps {
                script {
                    // Run your Python program with automated input
                    sh 'chmod +x meal_plan_generator.py'

                    sh 'echo 2500 | ./meal_plan_generator.py'
                }
            }
        }



	stage('Run Tests') {
    	    steps {
        	    // Install pytest
        	    sh 'pip install pytest'

        	    // Run pytest
        	    sh 'pytest tests'
    }                 
}



    }




	post {
        success {
            // Archive and rename the artifact in the workspace
            archiveArtifacts 'recipe.txt'
            script {
                
		   
		def buildTimestamp = env.BUILD_ID
		def newName = "recipe-${buildTimestamp}.txt"

		sh "cp recipe.txt recipe-${newName}"
            }

	}
	}
}

