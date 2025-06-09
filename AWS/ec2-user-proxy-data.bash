#!/bin/bash

# Use this for your user data (script from top to bottom)
# install httpd (Linux 2 version)
yum update -y
yum install -y httpd
systemctl start httpd
systemctl enable httpd
echo "<h1>Hello World from $(hostname -f)</h1>" > /var/www/html/index.html



#sudo su	#if manual
yum install docker -y
service docker start
docker --version



#install docker compose:
sudo curl -L https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
#Verify
docker-compose version


#If this doesn't work for you for whatever reason, add it to PATH

sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose
docker-compose version

#create docker-compose.yml

#run docker compose
docker-compose up -d


#Create directories for apps to run and store data.
mkdir proxyApps
mkdir proxyHome
