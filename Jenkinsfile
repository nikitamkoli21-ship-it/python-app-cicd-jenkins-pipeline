pipeline {
 agent any

 stages {

  stage('Checkout') {
   steps { checkout scm }
  }

  stage('Setup Python Environment') {
   steps {
    sh '''
    python3 -m venv venv
    . venv/bin/activate
    pip install -r requirements.txt
    pip install pytest pytest-html
    '''
   }
  }

  stage('Run Tests') {
   steps {
    sh '''
    . venv/bin/activate
    pytest test.py --junitxml=result.xml --html=report.html --self-contained-html
    '''
   }
   post {
    always {
     junit 'result.xml'
     publishHTML(target: [
      reportDir: '.',
      reportFiles: 'report.html',
      reportName: 'Pytest Report'
     ])
    }
   }
  }
 }
}
