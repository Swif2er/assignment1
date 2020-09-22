pipeline {
    agent any 
    triggers {
        cron('H/10 * * * *')
    }
    stages {
        stage('Test') { 
            steps {
                script {
                    url = "http://localhost:8080"
                    response = sh(script: "curl -s $url", returnStdout: true).trim()
                    echo response
                    if (response == "server1") {
                        currentBuild.result = 'FAILURE'
                    }
                }
            }
        }
    }
}