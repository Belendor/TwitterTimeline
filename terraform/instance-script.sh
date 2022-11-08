#!/bin/bash
sudo apt-get update -y
sudo apt install python3-pip
sudo sudo apt-get install apache2 -y
sudo sudo apt-get install apache2 -y
sudo sudo systemctl enable apache2
sudo systemctl start apache2
echo "${file_content}!" > /var/www/html/index.html
sudo apt-get install docker.io
sudo docker run -d -p 8080:80  belendor/twittertimeline:0.1