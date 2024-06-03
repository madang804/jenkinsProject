pipeline {
  agent {
      node {
          label 'docker-agent-python'
      }
  }
  stages {
    stage('Install Modules') {
      steps {
        echo "Installing Modules"
        sh'''
        cd myapp
        python3 -m venv venv
        source venv/bin/activate
        pip install -r requirements.txt
        python3 weather-web-api.py
        curl http://localhost:5000/api/v1.0/weather?location=london
        curl http://localhost:5000/api/v1.0/temperature?location=london
        curl http://localhost:5000/api/v1.0/wind?location=london
        '''
      }
    }
    
  }
}
