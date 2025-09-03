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


# install docker
yum install docker -y
service docker start
#Verify docker installation
docker --version

#install rust desk?
sudo docker image pull rustdesk/rustdesk-server
sudo docker run --name hbbs -v ./data:/root -td --net=host --restart unless-stopped rustdesk/rustdesk-server hbbs
sudo docker run --name hbbr -v ./data:/root -td --net=host --restart unless-stopped rustdesk/rustdesk-server hbbr


#all of this may not be needed.
	#install docker compose:
	sudo curl -L https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose
	sudo chmod +x /usr/local/bin/docker-compose
	#Verify docker compose installation
	docker-compose version

	#If this doesn't work for you for whatever reason, add it to PATH
	sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose
	docker-compose version
	#create docker-compose.yml
	#run docker compose
	docker-compose up -d