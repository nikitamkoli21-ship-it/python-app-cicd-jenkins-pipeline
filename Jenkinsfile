pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out source code...'
                checkout scm
            }
        }
        stage('Setup Python Environment') {
            steps {
                echo 'Setting up Python virtual environment...'
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install flask pytest pytest-html pytest-cov
                '''
            }
        }
        stage('Build / Compile Check') {
            steps {
                echo 'Checking Python syntax...'
                sh '''
                    . venv/bin/activate
                    python3 -m py_compile app.py
                    echo "Syntax check passed!"
                '''
            }
        }
        stage('Unit Test') {
            steps {
                echo 'Running unit tests with pytest...'
                sh '''
                    . venv/bin/activate
                    mkdir -p test-reports
                    pytest --junitxml=test-reports/results.xml \
                           --html=test-reports/report.html \
                           --self-contained-html \
                           -v
                '''
            }
            post {
                always {
                    junit 'test-reports/results.xml'
                    publishHTML(target: [
                        allowMissing: false,
                        alwaysLinkToLastBuild: true,
                        keepAll: true,
                        reportDir: 'test-reports',
                        reportFiles: 'report.html',
                        reportName: 'Pytest HTML Report'
                    ])
                }
            }
        }
    }
    post {
        success {
            echo 'Python CI Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Please check the test results.'
        }
    }
}
```

4. Scroll down → **Commit changes**

---

## Also update requirements.txt

1. Click on `requirements.txt`
2. Click **pencil icon ✏️**
3. **Delete everything** and paste:
```
flask
pytest
pytest-html
pytest-cov
