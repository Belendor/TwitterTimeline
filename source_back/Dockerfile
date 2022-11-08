FROM python:3.8.3
ENV MONGO_DB_USERNAME=admin \
    MONGO_DB_PWD=password
RUN pip install flask pymongo flask_cors pycron
ADD . /app
WORKDIR /app
CMD [ "python", "app.py" ]


 
