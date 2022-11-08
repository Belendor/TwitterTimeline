Building docker image for app:

sudo docker login

sudo docker build -t twittertimeline:0.1 .

sudo docker tag twittertimeline:0.1 belendor/twittertimeline:0.1

sudo docker push belendor/twittertimeline:0.1
