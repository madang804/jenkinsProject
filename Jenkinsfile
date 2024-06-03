pipeline {
  agent {
      node {
          label 'docker-agent-python'
      }
  }
  stages {
    stage('Build') {
      steps {
        echo "Building"
        sh'''
        pip install -r requirements.txt
        python3 weather-web-api.py
        '''
      }
    }
    stage('Test') {
      steps {
        echo "Testing"
        sh'''
        curl http://localhost:5000/api/v1.0/weather?location=london
        curl http://localhost:5000/api/v1.0/temperature?location=london
        curl http://localhost:5000/api/v1.0/wind?location=london
        '''
      }
    }
    stage('Deliver') {
      steps {
        echo "Delivering"
        sh'''
        echo "doing delivery stuff.."
        '''
      }
    }

  }
}
