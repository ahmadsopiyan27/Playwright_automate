pipeline {
    agent any

    environment {
        TELEGRAM_BOT_TOKEN = '8625524856:AAEgT02-6VMV8Oxpa6HQhRLhFIiixPxI4XY'
        TELEGRAM_CHAT_ID   = '1277076599'
        DOCKER_IMAGE       = 'mcr.microsoft.com/playwright/python:v1.58.0-noble'
    }

    options {
        timestamps()
        timeout(time: 60, unit: 'MINUTES')
        buildDiscarder(logRotator(numToKeepStr: '10'))
    }

    stages {

        stage('Checkout Source') {
            steps {
                checkout scm
            }
        }

        stage('Run Tests in Docker') {
            steps {
                script {
                    docker.image("${DOCKER_IMAGE}").inside('-u root -e HOME=/tmp') {

                        sh '''
                        cd /var/jenkins_home/workspace/${JOB_NAME}

                        echo "=== Installing system dependencies ==="
                        apt-get update && apt-get install -y \
                            libgl1 \
                            libglib2.0-0 \
                            libsm6 \
                            libxext6 \
                            libxrender-dev \
                            libgomp1 \
                            libglvnd0 \
                            libglx0 \
                            curl \
                            && rm -rf /var/lib/apt/lists/*

                        echo "=== Installing Python dependencies ==="
                        pip install --upgrade pip
                        pip install opencv-python-headless==4.12.0.88
                        pip install -r requirements.txt

                        echo "=== Installing Playwright Browser ==="
                        playwright install --with-deps

                        echo "=== Running tests ==="
                        pytest tests -v --alluredir=allure-results
                        '''
                    }
                }
            }
        }

        stage('Generate Allure Report') {
            steps {
                allure(
                    includeProperties: false,
                    jdk: '',
                    results: [[path: 'allure-results']]
                )
            }
        }

        stage('Send Telegram Success') {
            steps {
                script {

                    def allureReportUrl = "${env.BUILD_URL}allure/"
                    def status = currentBuild.currentResult ?: 'SUCCESS'
                    def summary = ''

                    try {
                        if (fileExists('allure-report/widgets/summary.json')) {

                            def summaryJson = readJSON file: 'allure-report/widgets/summary.json'

                            summary = """
Total   : ${summaryJson.statistic.total}
Passed  : ${summaryJson.statistic.passed}
Failed  : ${summaryJson.statistic.failed}
Broken  : ${summaryJson.statistic.broken}
Skipped : ${summaryJson.statistic.skipped}
"""
                        }
                    } catch (Exception e) {
                        echo "Summary not found"
                    }

                    def message = """
✅ Test Automation Report

Job      : ${env.JOB_NAME}
Build    : #${env.BUILD_NUMBER}
Status   : ${status}
Duration : ${currentBuild.durationString}
Date     : ${new Date().format('dd-MM-yyyy HH:mm')}

${summary}

📊 Allure Report:
${allureReportUrl}

🔗 Jenkins Build:
${env.BUILD_URL}
"""

                    sh """
                    curl -s -X POST https://api.telegram.org/bot${TELEGRAM_BOT_TOKEN}/sendMessage \
                    -d chat_id=${TELEGRAM_CHAT_ID} \
                    --data-urlencode text='${message}'
                    """
                }
            }
        }
    }

    post {

        failure {
            script {

                def message = """
❌ Build Failed

Job   : ${env.JOB_NAME}
Build : #${env.BUILD_NUMBER}

📄 Console:
${env.BUILD_URL}console
"""

                sh """
                curl -s -X POST https://api.telegram.org/bot${TELEGRAM_BOT_TOKEN}/sendMessage \
                -d chat_id=${TELEGRAM_CHAT_ID} \
                --data-urlencode text='${message}'
                """
            }
        }

        always {
            archiveArtifacts artifacts: '**/*.png', allowEmptyArchive: true
            archiveArtifacts artifacts: '**/*.jpg', allowEmptyArchive: true
            archiveArtifacts artifacts: 'allure-results/**', allowEmptyArchive: true
        }
    }
}