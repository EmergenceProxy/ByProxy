#!/bin/bash


# Use this for your user data (script from top to bottom)
#if running manually from CLI
#sudo su

# install httpd (Linux 2 version)
runDate=`date +"%Y-%m-%d-%T"`
yum update -y
yum install -y httpd
systemctl start httpd
systemctl enable httpd
echo "<h1>Hello World from the RustDesk Server @ $(hostname -f)</h1>" > /var/www/html/index.html
#clone httpd code to html dir


# install docker
#yum install docker -y
#service docker start
#Verify docker installation
#docker --version

#install git
yum install git

#Create directories for apps to run and store data.
#mkdir proxyApps
git clone https://github.com/EmergenceProxy/ByProxy.git proxyApps
mkdir proxyHome

cd proxyApps
mkdir appData


htmlFilesDir="/var/www/html"
appScriptsDir="/home/proxyApps"
appDataDir="/home/proxyApps/appData"
userDataDir="/home/proxyHome"
ytcDLWorkingDir="/home/proxyApps/appData/ytcData"


python3 -m venv proxy_test_env

#Activate virtual env
source proxy_test_env/bin/activate
#Deactivate virtual env
#


#Python modules to install in the proxy_test_env virtual python environment
pip install Flask
pip install dominate
pip install urllib3==1.26.6
pip install youtube_comment_downloader


#touch hello.py

#Create test pages:
echo "from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello world!'" > /home/proxyApps/hello.py

echo "from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello():
	return 'Hello from Flask on EC2!'

if __name__ == '__main__':
	app.run(host='0.0.0.0', port=5000)"> /home/proxyApps/helloEC2.py


#5 Load test page into flask
export FLASK_APP=helloEC2.py

#6 Load app page into flask, and run listening to any/httpd for requests.
export FLASK_APP=proxyFlaskApp.py; flask run --host=0.0.0.0 &> $appDataDir/flaskOutput.log;
# export FLASK_APP=proxyFlaskApp.py; flask run --host=0.0.0.0 --debug


# When testing wwith no httpd:
# look for log similar to "Running on http://123.0.0.1:5000"
# Copy the actual ipAddress:" Running on <yourFoundIP>"